# Selenium

Elöljáróban:
--

Chrome webdrivers: https://sites.google.com/chromium.org/driver/

- fontos, hogy a chrome verziónknak megfelelő legyen a diver

Websites to practise selenium: https://www.techbeamers.com/websites-to-practice-selenium-webdriver-online/

Selenium doc: https://selenium-python.readthedocs.io/locating-elements.html

-------------
Setup
--

Importok:

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time

Korábbi tutorialokban találkozhatunk ezzel, már elavult, mert bezáródik a böngésző:

    path:str = r"C:\Linux_haladó\zips\google_driver\chromedriver.exe"
    mydriver = webdriver.Chrome(path)

Egy megoldás, hogy ne záródjon be:

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    !!!!! ezek után odafigyelni, hogy mydriver = webdriver.Chrome(path, options=chrome_options)

    ha mégis azt szeretnénk, hogy bezáródjon: mydriver.quit()


Nyitva a weblap. Hogyan érhetem el az adott részeit, amelyet használni szeretnék?
--

- Jobbclick az oldalra, vagy pedig akár egy search barra.
- Inspect
- Több dolog szerint érhetjük el ( id, name, class stb.)
  
      f_name = mydriver.find_element(By.VALAMI, 'érték')