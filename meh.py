from selenium import webdriver
from selenium.webdriver import Opera
from selenium.webdriver.chrome.webdriver import WebDriver
import requests
from bs4 import BeautifulSoup
import urllib.request



driver = webdriver.Opera(executable_path="C:\WebDriver\operadriver.exe")

url="https://www.pcdiga.com/#/embedded/query=3090&page=1&filter%5Bcategories%5D%5B0%5D=Placas%20Gráficas&query_name=match_and"

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(40)

a=driver.find_elements_by_class_name("df-card")


b=[]
for j in a:
	b.append(j.text)

c=[]

for i in b:
	if "Sem Stock" in i:
		continue
	else:
		c.append(i.split('\n')[0])



for i in c:
	l=driver.find_element_by_xpath("//span[.="\i""]")
	l.click()