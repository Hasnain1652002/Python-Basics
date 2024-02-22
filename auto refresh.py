import time
from selenium import webdriver
import random

# setup webdriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shorcuts")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

# open Fiverr dashboard page
driver.get("https://www.fiverr.com/dashboard")

# refresh the page every 6 to 7 minutes
while True:
    user_input = input("Press 'q' or 'quit' to exit: ")
    if user_input.lower() == "q" or user_input.lower() == "quit":
        break
    driver.refresh()
    time.sleep(360 + random.randint(0, 60))

# close the driver
driver.close()
