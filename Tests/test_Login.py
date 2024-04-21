import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
from allure_commons.types import AttachmentType


class Test_Login():

    def test_validLogin_scenario(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--remote-debugging-port=9222')
        driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        driver.get("https://www.rahulshettyacademy.com/locatorspractice/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//input[@id='inputUsername']").send_keys("KarryBoy")
        driver.find_element(By.XPATH,"//input[@name='inputPassword']").send_keys("rahulshettyacademy")
        driver.find_element(By.XPATH,"//button[text()='Sign In']").click()
        time.sleep(2)
        succesMessage = driver.find_element(By.XPATH,"//p[text()='You are successfully logged in.']").text
        assert succesMessage.__eq__("You are successfully logged in.")
        driver.close()

    def test_invalidLogin_scenario(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--remote-debugging-port=9222')
        driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        driver.get("https://www.rahulshettyacademy.com/locatorspractice/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='inputUsername']").send_keys("KarryBoy")
        driver.find_element(By.XPATH, "//input[@name='inputPassword']").send_keys("rahulshettyacademy123")
        driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        time.sleep(2)
        succesMessage = driver.find_element(By.XPATH, "//p[text()='* Incorrect username or password']").text
        assert succesMessage.__eq__("* Incorrect username or password123"),allure.attach(driver.get_screenshot_as_png(),"Login Failed", attachment_type=AttachmentType.PNG)
        driver.close()
