from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.pracuj.pl/praca/warszawa;wp?rd=30&cc=5016%2C5015&et=1%2C3&sc=0&msockid=2160f30bab3e6ac236cde785aa166be6")
offers_dict = {"oferty": [], "daty": [], "linki": []}
offers = driver.find_elements(By.CSS_SELECTOR, ".tiles_o1859gd9.tiles_o1859gd9")
offers_date = driver.find_elements(By.CSS_SELECTOR, ".tiles_bg8mbli.tiles_bg8mbli")
for i in range (len(offers)):
    time.sleep(0.1)
    akt_oferta = offers[i]
    akt_data = offers_date[2*i]
    offers_link = akt_oferta.get_attribute("href")
    offers_dict["oferty"].append(akt_oferta.text)
    offers_dict["linki"].append(offers_link)
    stripped_date = akt_data.text.strip("Opublikowana: ")
    offers_dict["daty"].append(stripped_date)
    # print(i.text,"\t",offers_link)
print("oferta", len(offers_dict["oferty"]))
print("link", len(offers_dict["linki"]))
print("data dodania", len(offers_dict["daty"]))
print(len(offers))
df_offers = pd.DataFrame(offers_dict)
# df_offers.to_excel("output.xlsx", sheet_name='Sheet_name_1')  
with pd.ExcelWriter('output.xlsx',
                    mode='a',
                    if_sheet_exists="overlay") as writer:  
    df_offers.to_excel(writer, sheet_name='Sheet_name_3')
print(df_offers)
# print(offers_dict)
driver.quit()