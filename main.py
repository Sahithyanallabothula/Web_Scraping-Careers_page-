from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import database1
def extractData(tableName):
    database1.Jobs.truncateTable(tableName)
    driver=webdriver.Chrome()
    driver.get('https://www.deshawindia.com/careers/work-with-us')
    driver.implicitly_wait(30)
    driver.maximize_window()
    my_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'more-amount' )]"))
    )
    driver.find_element(By.XPATH,"//div[contains(@class,'accept-button')]").click()
    element1=driver.find_element(By.XPATH,"//span[contains(@class,'more-amount' )]")
    driver.execute_script("arguments[0].scrollIntoView();",element1)
    driver.find_element(By.XPATH,"//span[contains(@class,'more-amount' )]").click()
    
    joid = driver.find_elements(By.XPATH,"//div[@class='job-wrapper']/div[@data-job-id]")
    joid1 = driver.find_elements(By.XPATH,"//div[@class='extra-wrapper']/div[@data-job-id]")
    cat=driver.find_elements(By.XPATH,"//p[contains(@class,'category')]")
    loc=driver.find_elements(By.XPATH,"//span[contains(@class,'location')]")
    pos=driver.find_elements(By.XPATH,"//a/p/span")
    lin = driver.find_elements(By.XPATH,"//div[@class='description-wrapper']/a[@href]")
    jobid=[]
    category=[]
    location=[]
    position=[]
    links=[]
    for ids in joid:
        jobid.append(ids.get_attribute("data-job-id"))
    for ids1 in joid1:
        jobid.append(ids1.get_attribute("data-job-id"))
    for ca in cat:
        category.append(ca.text)
    for lo in loc:
        location.append(lo.text)
    for po in pos:
        position.append(po.text)
    for li in lin:
        links.append(li.get_attribute("href"))
    for i in range(len(jobid)):
        database1.Jobs.insertData(jobid[i],category[i],location[i],position[i],links[i],tableName)
    df=pd.DataFrame({'JobId':jobid, 'Category':category, 'Location':location, 'Position':position, 'Links':links})
    df.to_csv('Jobs_Site.csv', index=False)
    
extractData('public.Jobs')





