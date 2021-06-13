from selenium import webdriver
from selenium.webdriver import Opera
from selenium.webdriver.chrome.webdriver import WebDriver
import requests







driver = webdriver.Opera(executable_path="C:\WebDriver\operadriver.exe")


url="https://www.pcdiga.com/placa-grafica-gigabyte-geforce-rtx-3090-aorus-gaming-box-24gb-gv-n3090ixeb-24gd-1-0?search=3090"

driver.get(url)

driver.maximize_window()



click = driver.find_element_by_xpath("/html/body/div[3]/main/div[3]/div/div[2]/div[4]")
driver.maximize_window()

click.click()

