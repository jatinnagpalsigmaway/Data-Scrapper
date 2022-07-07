from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = "https://collegedunia.com"
# url = "https://selenium.dev"
chromeService=Service(r"C:\Users\Mohit\Documents\Driver\chromedriver_win32\chromedriver.exe")

options = Options()

browser = webdriver.Chrome(service=chromeService,options=options)

browser.get(url)

links = browser.find_elements(By.TAG_NAME,"a")

print("Following are the link present in the webpage")
linkdat = []
for link in links:
    linkdat.append(link.get_attribute('href'))
    print(link.text,' : ' ,link.get_attribute('href'))

browser.quit()
MyFile=open('output.txt','w')

for element in linkdat:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()