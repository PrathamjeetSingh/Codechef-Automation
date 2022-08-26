import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
browser = webdriver.Edge(
    "D:\\Codes\\Web Automation\\Selenium\\Codechef Automation\\msedgedriver.exe")  # for MS Edge browser
# browser = webdriver.Chrome(r"<PATH TO DRIVER (EXE) >") #for chrome broswer
browser.get('https://www.codechef.com/login?destination=/')
time.sleep(5)
username_element = browser.find_elements(By.ID, 'edit-name')[1]
username_element.clear()  # clears the field
# username_element.send_keys(input("Enter User id:  "))
username_element.send_keys("zafyre69")
password_element = browser.find_elements(By.ID, 'edit-pass')[1]
password_element.clear()
# password_element.send_keys(getpass("Enter Password:  "))
password_element.send_keys("Z@fyre123")
browser.find_elements(By.ID, 'edit-submit-button')[1].click()
time.sleep(3)
question_id = input('Enter Question ID:  ')
browser.get('https://www.codechef.com/submit-old/{}'.format(question_id))
time.sleep(3)
if(browser.find_elements(By.ID, "edit_area_toggle_checkbox_edit-program") == []):
    switch_text = browser.find_elements(By.ID, 'edit-submit')[0]
    switch_text.click()
code_element = browser.find_element(By.ID, 'edit-program')
if code_element.is_displayed() == False:
    browser.find_element(By.ID,
                         'edit_area_toggle_checkbox_edit-program').click()
code_element = browser.find_element(By.ID, 'edit-program')
with open('file.cpp', 'r') as f:
    code = f.read()
code_element.clear()
code_element.send_keys(code)
select_language_element = browser.find_element(By.XPATH,
                                               '//*[@id="edit-language"]/option[1]').click()
submit_button_element = browser.find_element(By.ID, 'edit-submit-1').click()
