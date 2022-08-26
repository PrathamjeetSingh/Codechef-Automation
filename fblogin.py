import selenium
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


import time
driver = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))
driver.get("https://www.facebook.com")
name = driver.find_element(By.ID, "email")
name.send_keys("aaryanpratap11@gmail.com")
pass_element = driver.find_element(By.NAME, "pass")
pass_element.send_keys("aaa6af9bd")
driver.find_element(By.NAME, "login").click()
