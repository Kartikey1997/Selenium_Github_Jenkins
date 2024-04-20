import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class Test_Login():

    def test_validLogin_scenario(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.rahulshettyacademy.com/locatorspractice/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='inputUsername']").send_keys("KarryBoy")
        driver.find_element(By.XPATH, "//input[@name='inputPassword']").send_keys("rahulshettyacademy123")
        driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
        time.sleep(2)
        succesMessage = driver.find_element(By.XPATH, "//p[text()='* Incorrect username or password']").text
        assert succesMessage.__eq__("* Incorrect username or password123")
        driver.close()
