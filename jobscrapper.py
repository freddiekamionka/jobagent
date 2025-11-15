from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.pracuj.pl/praca/warszawa;wp?rd=30&cc=5016%2C5015&et=1%2C3&sc=0&msockid=2160f30bab3e6ac236cde785aa166be6")
offers_dict = {"oferty": [], "linki": []}
offers = driver.find_elements(By.CSS_SELECTOR, ".tiles_o1859gd9.tiles_o1859gd9")
for i in offers:
    time.sleep(0.1)
    offers_link = i.get_attribute("href")
    offers_dict["oferty"].append(i.text)
    offers_dict["linki"].append(offers_link)
    # print(i.text,"\t",offers_link)
df_offers = pd.DataFrame(offers_dict)
# df_offers.to_excel("output.xlsx", sheet_name='Sheet_name_1')  
with pd.ExcelWriter('output.xlsx',
                    mode='a',
                    if_sheet_exists="overlay") as writer:  
    df_offers.to_excel(writer, sheet_name='Sheet_name_3')
print(df_offers)
# print(offers_dict)
driver.quit()