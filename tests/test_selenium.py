import pytest
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class TestSelenium():
    @pytest.fixture(scope="session")
    def test_setup(self):
        path : str = r"C:\Linux_haladó\zips\google_driver\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True) #Without these the browser automatically closes
        driver = wd.Chrome(path, options=chrome_options)
        driver.maximize_window()
        yield driver

    def test_fill_the_boxes(self, test_setup):
        test_setup.get('https://phptravels.com/demo')
        # time.sleep(3)
        test_setup.find_element(By.NAME, "first_name").send_keys("Dwayne")
        test_setup.find_element(By.NAME, "last_name").send_keys("Johnson")
        test_setup.find_element(By.NAME, "business_name").send_keys("The Rock")
        test_setup.find_element(By.NAME, "email").send_keys("dtrj@example.com")
        test_setup.find_element(By.ID, "number").send_keys(str(int(test_setup.find_element(By.ID, "numb1").text) + int(test_setup.find_element(By.ID, "numb2").text)))
        test_setup.find_element(By.ID, "demo").click()
        # time.sleep(3)

    def test_correct_web(self, test_setup):
        assert 'Book Your Free' in test_setup.title

    def test_tearndown(self, test_setup):
        test_setup.close()
        test_setup.quit()
        print('Test complited')
