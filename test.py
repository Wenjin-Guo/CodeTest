from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options


edge_options = Options()
edge_options.add_experimental_option("detach",True)
driver = webdriver.Edge(edge_options,None,True)
driver.get("https://qa-envision2front.dev.eag.environics.ca/")

try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"email")))
    #element.send_Keys("simon.guo@environicsanalytics.com")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"password")))
    #passWord.send_Keys("Gwj.677895")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"next")))
    #logIn.click()
except:
    print("elements not found, or error occur")
email = driver.find_element(By.ID,"email")
email.send_keys("simon.guo@environicsanalytics.com")
passWord = driver.find_element(By.ID,"password")
passWord.send_keys("Eioq@5fJ39x!FcoK")
loginButton = driver.find_element(By.ID,"next")
loginButton.click()
#driver.implicitly_wait(10000)
#driver.find_element(By.ID,"pr_id_72_header_0").click()

driver.implicitly_wait(5000)
driver.find_element(By.XPATH,'//*[@id="pr_id_1"]/div[2]/div/button/span').click()
driver.implicitly_wait(1000)
driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[5]/button/i').click() 
driver.implicitly_wait(1000)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]/button/img').click()
driver.implicitly_wait(5000)

profile_report_data = []
#profile_report_data = driver.find_elements(By.TAG_NAME,'td')
profile_report_data_test = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[1]/div/div/div/div[4]/div/table/tbody/tr[1]/td[5]')
print(profile_report_data_test)
#print(profile_report_data.count)
driver.find_element(By.ID,"pr_id_72_header_0").click()

#/html/body/div/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[1]/div/div/div/div[4]/div/table/tbody/tr[1]/td[5]
#grid_128561338_1_content_table > tbody > tr:nth-child(1) > td:nth-child(1)
