import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options


edge_options = Options()
edge_options.add_experimental_option("detach",True)
driver = webdriver.Edge(edge_options,None,True)
driver.maximize_window()
driver.get("https://qa/Spotlight/Reporting/Build ")

driver.find_element(By.ID,"details-button").click()
driver.find_element(By.ID,"proceed-link").click()


try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"Username")))
except:
    print("elements not found, or error occur")

email = driver.find_element(By.ID,"Username")
email.send_keys("spotca_qa_std")
passWord = driver.find_element(By.ID,"Password")
passWord.send_keys("Qwe!234")
loginButton = driver.find_element(By.ID,"button")
loginButton.click()

driver.implicitly_wait(5000)
driver.find_element(By.ID,"previous-year").click()
time.sleep(2)
##find the report and select
driver.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div/div[1]/form/div[2]/div[17]/span[1]/i").click()
driver.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div/div[1]/form/div[2]/div[18]/span[1]/i").click()



driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.ID,"btn-wiz-next").click()
time.sleep(2)
driver.find_element(By.ID,"btnShowInputSelection").click()
time.sleep(2)
#seeding report
driver.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div/div[3]/div[3]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]/i").click()
driver.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div/div[3]/div[3]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[1]/i").click()
driver.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div/div[3]/div[3]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr[3]/td[1]/i").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.ID,"btn-wiz-next").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div/div[5]/div/div/a").click()
time.sleep(20)


#driver.implicitly_wait(5000)
driver.find_element(By.XPATH,"/html/body/div/div[1]/nav/div/div[2]/ul[1]/li[4]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[2]/div/div/table/tbody/tr[1]/td[3]/span").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/a[2]/i[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[1]/div[1]/div[2]/div[1]/h4/a").click()
time.sleep(2)
##Batch PDF download
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/a/div[2]/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]").click()
driver.find_element(By.NAME,"Filename").clear()
driver.find_element(By.NAME,"Filename").send_keys("Executive Dashboard--batch")
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[3]/form/div[2]/button[1]").click()
#Batch EXCEL download
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/a/div[2]/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]").click()
driver.find_element(By.NAME,"Filename").clear()
driver.find_element(By.NAME,"Filename").send_keys("Executive Dashboard--batch")
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[3]/form/div[2]/button[1]").click()
#SBS EXCEL download
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/a/div[2]/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[2]").click()
driver.find_element(By.NAME,"Filename").clear()
driver.find_element(By.NAME,"Filename").send_keys("Executive Dashboard--SBS")
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[3]/form/div[2]/button[1]").click()
#LF CSV download
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/a/div[2]/div[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]").click()
driver.find_element(By.NAME,"Filename").clear()
driver.find_element(By.NAME,"Filename").send_keys("Executive Dashboard--LF")
driver.find_element(By.XPATH,"/html/body/div/section[1]/div[4]/div[2]/div/div[3]/form/div[2]/button[1]").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div/div[1]/form/div[2]/div[18]/span[1]/i").click()
driver.quit()