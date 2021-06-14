from selenium import webdriver
from selenium.webdriver import Opera
from selenium.webdriver.chrome.webdriver import WebDriver
import requests
from bs4 import BeautifulSoup
import urllib.request
import schedule
import time
from time import time,sleep

while True:
	try:

		sleep(2-time()%2)

		driver = webdriver.Opera(executable_path="C:\WebDriver\operadriver.exe")

		url="https://www.pcdiga.com/#/embedded/query=3090&page=1&filter%5Bcategories%5D%5B0%5D=Placas%20Gráficas&query_name=match_and"

		driver.get(url)
		driver.maximize_window()
		driver.implicitly_wait(40)

		allcards=driver.find_elements_by_class_name("df-card")


		allcards_text=[]
		for j in allcards:
			allcards_text.append(j.text)

		only_available=[]

		for i in allcards_text:
			if "Sem Stock" in i:
				continue
			else:
				only_available.append(i.split('\n')[0])

		

		for i in only_available:
			l=driver.find_element_by_xpath("//span[.='"+i+"']")
			l.click()






		driver.find_element_by_id("product-addtocart-button").click()

		l.click()

		time.sleep(2)
	
	except: 
		pass





