import urllib.request as url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
driver = webdriver.Chrome('/home/shyam/Desktop/MyProjects/examples/Automa/WhatsApp/whatsenv/chromedriver',options=chrome_options)
driver.set_window_position(0, 0)
driver.set_window_size(564, 768)   
driver.get('https://www.hackerrank.com/auth/login?h_l=body_middle_left_button&h_r=login')
time.sleep(3)

username = driver.find_element_by_xpath("//input[@name='username']")
username.clear()
# username.send_keys("")
username.send_keys(Keys.TAB)

password = driver.find_element_by_xpath("//input[@name='password']")
password.clear()
password.send_keys("")
username.send_keys(Keys.RETURN)

time.sleep(3)
driver.get("https://www.hackerrank.com/domains/algorithms?filters%5Bstatus%5D%5B%5D=solved&badge_type=problem-solving")
driver.refresh()