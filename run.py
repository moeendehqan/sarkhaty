from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome( executable_path=r'C:\Users\moeen\Desktop\project\sarkhaty\chromedriver.exe')
driver.get('https://mofidonline.com//Account/Login')

start = input('عملیات رو شروع کنم؟')


while True:
    driver.find_element_by_xpath('//*[@id="send_order_btnSendOrder"]').click()
    time.sleep(0.15)
