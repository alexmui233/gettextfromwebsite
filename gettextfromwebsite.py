from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://docs.oracle.com/en/industries/communications/billing-revenue/12.0/restapi/quick-start.html")

dlist = {}
for i in range(26):
  idname = "tree2-node" + str(i)
  print("idname: ", idname)
  foundelement = driver.find_element(By.ID, idname)
  
  arrow = foundelement.find_element(By.TAG_NAME, "div")
  arrowstr = arrow.click()
  
  foundelement_clicked = driver.find_element(By.ID, idname)
  
  functext = foundelement_clicked.text
  # print("type(funclist): ", type(functext))
  funclist = functext.split("\n")
  # print("funclist: ", funclist)
  list_temp = {funclist[0]: funclist[1:]}
  dlist.update(list_temp)
  print(functext, "\n")

time.sleep(5)
driver.close()
driver.quit()

df = pandas.DataFrame(dict(
          [(key, pandas.Series(value))
          for key, value in dlist.items()]
        ))
# print(df)

writer = pandas.ExcelWriter('billingcare function feature.xlsx')
df.to_excel(writer)
writer._save()