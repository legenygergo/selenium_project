from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_chrome(https:str)->None:
    path:str = r"C:\Linux_haladó\zips\google_driver\chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) #Without these the browser automatically closes

    mydriver = webdriver.Chrome(path, options=chrome_options)
    return mydriver

def phptrav_test(https:str)->None:
    mydriver = open_chrome(https)
    mydriver.get(https)

    f_name = mydriver.find_element(By.NAME, "first_name")
    l_name = mydriver.find_element(By.NAME, "last_name")
    b_name = mydriver.find_element(By.NAME, "business_name")
    email = mydriver.find_element(By.NAME, "email")    
    num1 = mydriver.find_element(By.ID, "numb1").text
    num2 = mydriver.find_element(By.ID, "numb2").text
    mysum = int(num1) + int(num2)
    res = mydriver.find_element(By.ID, "number")
    # btn = mydriver.find_element(By.ID, "demo")

    f_name.send_keys("Dwayne")
    l_name.send_keys("Johnson")
    b_name.send_keys("The Rock")
    email.send_keys("dtrj@example.com")
    res.send_keys(str(mysum))

if __name__ == '__main__':
    # open_chrome("https://phptravels.com/demo")
    # open_chrome("https://open.spotify.com/")
    phptrav_test("https://phptravels.com/demo")