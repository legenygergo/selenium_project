# Selenium

Links:
--

Chrome webdrivers: https://sites.google.com/chromium.org/driver/

- it is important that the diver is compatible with our chrome version

Websites to practise selenium: https://www.techbeamers.com/websites-to-practice-selenium-webdriver-online/

Selenium doc: https://selenium-python.readthedocs.io/locating-elements.html

-------------
Setup
--

Imports:

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time

You may have seen this in older tutorials, it is now obsolete because it closes the browser:

    path:str = r"C:\Linux_haladó\zips\google_driver\chromedriver.exe"
    mydriver = webdriver.Chrome(path)

A solution, to fix the closing problem:

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    !!!!! after that, pay attention to mydriver = webdriver.Chrome(path, options=chrome_options)

   if you do want it to close: mydriver.quit()


The website is open. How can I access the specific parts of the site I want to use?
--

- Rightclick on the site, or for example a search bar
- Inspect
- We can reach it in several ways (id, name, class etc.)
  
      f_name = mydriver.find_element(By.SMTHING, 'value')