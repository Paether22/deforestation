from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get(
    "https://www.theworldcounts.com/challenges/forests-and-deserts/why-is-deforestation-a-problem"
)

while True:
    counter = driver.find_elements(
        "xpath", "//div[contains(@class, 'counter-ticker is-size-2-mobile')]"
    )
    x = ""
    for text in counter:
        x = text.get_attribute("innerHTML").replace("<!---->", "")

        print(x)

    time.sleep(10)
