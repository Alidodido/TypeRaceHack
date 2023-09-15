from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get(f"https://play.typeracer.com")
sleep(10)

enter = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/div[1]/div[2]/a")
enter.click()

sleep(20)
sentence = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div")
matn = sentence.text
print(matn)


matn = matn.split()

entry =  driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input")
for word in matn:
    for alph in word:
        entry.send_keys(alph)
        sleep(0.1)
    entry.send_keys(" ")
