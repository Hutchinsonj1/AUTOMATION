from selenium import webdriver
import time

driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
driver.get("https://www.instagram.com")
time.sleep(3)

Username=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username.send_keys("3853212847")
time.sleep(4)
  
Password=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
Password.send_keys("Bboy@thepiano10")
Password.submit()
time.sleep(5)

notNow= driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
notNow.click()
time.sleep(1)

Noti= driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
Noti.click()
time.sleep(3)

def firstPic():
    time.sleep(2)
    pic=driver.find_element_by_class_name("_9AhH0")
    pic.click()

def likepic():
    time.sleep(3)
    like=driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]/button")
    like.click()

firstPic()
likepic()

time.sleep(10)
