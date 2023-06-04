from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_setup():
    global driver
    path : str = r"C:\Linux_haladó\zips\google_driver\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) #Without these the browser automatically closes
    driver = wd.Chrome(path, options=chrome_options)
    driver.maximize_window()

def test_fill_the_boxes():
    driver.get('https://phptravels.com/demo')
    # time.sleep(3)
    driver.find_element(By.NAME, "first_name").send_keys("Dwayne")
    driver.find_element(By.NAME, "last_name").send_keys("Johnson")
    driver.find_element(By.NAME, "business_name").send_keys("The Rock")
    driver.find_element(By.NAME, "email").send_keys("dtrj@example.com")
    driver.find_element(By.ID, "number").send_keys(str(int(driver.find_element(By.ID, "numb1").text) + int(driver.find_element(By.ID, "numb2").text)))
    driver.find_element(By.ID, "demo").click()
    time.sleep(3)
    time.sleep(1)

def test_tearndown():
    driver.close()