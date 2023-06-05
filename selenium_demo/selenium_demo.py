from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    time.sleep(3)
    f_name = mydriver.find_element(By.NAME, "first_name")
    l_name = mydriver.find_element(By.NAME, "last_name")
    b_name = mydriver.find_element(By.NAME, "business_name")
    email = mydriver.find_element(By.NAME, "email")    
    num1 = mydriver.find_element(By.ID, "numb1").text
    num2 = mydriver.find_element(By.ID, "numb2").text
    mysum = int(num1) + int(num2)
    res = mydriver.find_element(By.ID, "number")
    btn = mydriver.find_element(By.ID, "demo")

    f_name.send_keys("Dwayne")
    l_name.send_keys("Johnson")
    b_name.send_keys("The Rock")
    email.send_keys("dtrj@example.com")
    res.send_keys(str(mysum))

    time.sleep(3)
    btn.click()
    time.sleep(3)
    mydriver.refresh()
    time.sleep(2)
    mydriver.find_element(By.LINK_TEXT, "Pricing").click()
    time.sleep(3)
    mydriver.close()

def phptrav_test_spam(https:str)->None:
    mydriver = open_chrome(https)
    mydriver.get(https)
    while True:
        time.sleep(3)
        f_name = mydriver.find_element(By.NAME, "first_name")
        l_name = mydriver.find_element(By.NAME, "last_name")
        b_name = mydriver.find_element(By.NAME, "business_name")
        email = mydriver.find_element(By.NAME, "email")    
        num1 = mydriver.find_element(By.ID, "numb1").text
        num2 = mydriver.find_element(By.ID, "numb2").text
        mysum = int(num1) + int(num2)
        res = mydriver.find_element(By.ID, "number")
        btn = mydriver.find_element(By.ID, "demo")

        f_name.send_keys("Dwayne")
        l_name.send_keys("Johnson")
        b_name.send_keys("The Rock")
        email.send_keys("dtrj@example.com")
        res.send_keys(str(mysum))
        
        time.sleep(3)
        btn.click()
        time.sleep(3)
        mydriver.refresh()

if __name__ == '__main__':
    # phptrav_test("https://phptravels.com/demo")
    phptrav_test_spam("https://phptravels.com/demo")