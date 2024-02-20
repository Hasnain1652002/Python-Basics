# import os 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# os.environ['PATH'] += r'E:\selenium_drivers'
# driver = webdriver.Chrome()

# driver.get('https://www.facebook.com/')
# driver.implicitly_wait(5)

# ## if we want to check the task we have performed is done or not
# # progress_element = driver.find_element_by_class_name('wo cheez jo hame search krni hogi')
# # print (f"{progress_element.text == 'Completed!'}") #(but this is not a correct way to do)

# # WebDriverWait(driver,30).until(
# #     EC.text_to_be_present_in_element(
# #         (By.CLASS_NAME, 'class name of the text to be checked'), # Element Filtration
# #         'text to be checked' # The Expected text
# #     )
# # ) # this is the correct way to do 

# # # if some pop up comes to avoid it we can apply exceptional handling
# # try:
# #     button = driver.find_element_by_class_name('is mai hum wo id ya class likhte hy jis ko hame hatana ho')
# #     button.click()
# # except:
# #     print("wo msg jo print krwainge agr pop up na aya to") 

# email = driver.find_element_by_id('email')
# pas = driver.find_element_by_id('pass')

# email.send_keys('hassnainshabbir@hotmail.com')
# pas.send_keys('i love my')

# button = driver.find_element_by_name('login')
# button.click()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open the website in a new Chrome window
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Find the "Create Account" button and click it
create_account_button = driver.find_element_by_id("create-account-button")
create_account_button.click()

# Enter user information into the registration form
first_name_input = driver.find_element_by_id("first-name-input")
first_name_input.send_keys("John")
last_name_input = driver.find_element_by_id("last-name-input")
last_name_input.send_keys("Doe")
email_input = driver.find_element_by_id("email-input")
email_input.send_keys("johndoe@example.com")
password_input = driver.find_element_by_id("password-input")
password_input.send_keys("password")
confirm_password_input = driver.find_element_by_id("confirm-password-input")
confirm_password_input.send_keys("password")

# Submit the registration form
submit_button = driver.find_element_by_id("submit-button")
submit_button.click()

# Wait for the registration process to complete
time.sleep(5)

# Close the Chrome window
driver.close()
  
# -----------------------------------------------------------------


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# List of websites to sign up for
websites = [
    'https://www.urbanoutfitters.com/',
    'https://www.burlington.com/',
    'https://shop.nordstrom.com/',
    # Add more websites here
]

# User information
first_name = 'John'
last_name = 'Doe'
email = 'johndoe@example.com'
password = 'password123'

# Loop through the websites list
for website in websites:
    # Open the website
    driver = webdriver.Chrome()
    driver.get(website)

    # Find and click the sign up button/link
    signup_button = driver.find_element_by_xpath('//button[contains(text(), "Sign up")]')
    signup_button.click()

    # Enter user information into the sign up form
    first_name_field = driver.find_element_by_name('first_name')
    first_name_field.send_keys(first_name)
    last_name_field = driver.find_element_by_name('last_name')
    last_name_field.send_keys(last_name)
    email_field = driver.find_element_by_name('email')
    email_field.send_keys(email)
    password_field = driver.find_element_by_name('password')
    password_field.send_keys(password)
    confirm_password_field = driver.find_element_by_name('confirm_password')
    confirm_password_field.send_keys(password)

    # Submit the sign up form
    signup_submit_button = driver.find_element_by_xpath('//button[contains(text(), "Sign up")]')
    signup_submit_button.click()

    # Wait for the sign up process to complete
    time.sleep(5)

    # Close the browser window
    driver.quit()



#------------------------------------------------


import requests

# List of websites to automate
websites = ['https://www.urbanoutfitters.com', 'https://www.burlington.com', 'https://www.nordstrom.com', 'https://www.talbots.com', 'https://www.forever21.com', 'https://bananarepublic.gap.com', 'https://www2.hm.com', 'https://oldnavy.gap.com', 'https://www.gap.com', 'https://www.pacsun.com', 'https://www.rue21.com', 'https://www.ae.com', 'https://www.express.com', 'https://www.hollisterco.com', 'https://www.guess.com', 'https://www.carters.com', 'https://www.childrensplace.com', 'https://www.walmart.com', 'https://www.target.com', 'https://www.beallsflorida.com', 'https://www.belk.com', 'https://www.jcpenney.com', 'https://tjmaxx.tjx.com', 'https://www.kohls.com', 'https://www.macys.com', 'https://www.bloomingdales.com', 'https://www.sears.com', 'https://www.shoes.com', 'https://www.zappos.com', 'https://www.champssports.com', 'https://www.footlocker.com', 'https://www.famousfootwear.com', 'https://www.ugg.com', 'https://www.finishline.com', 'https://www.dsw.com', 'https://www.shoecarnival.com', 'https://www.rackroomshoes.com', 'https://www.vans.com', 'https://www.llbean.com', 'https://www.columbia.com', 'https://www.thenorthface.com', 'https://www.eddiebauer.com', 'https://www.nike.com', 'https://www.ashleystewart.com', 'https://www.lanebryant.com', 'https://www.torrid.com', 'https://www.adoreme.com', 'https://www.catherines.com', 'https://www.jcrew.com', 'https://www.abercrombie.com', 'https://www.calvinklein.us', 'https://www.loft.com', 'https://www.maurices.com', 'https://www.victoriassecret.com', 'https://www.wawa.com', 'https://www.quiktrip.com', 'https://www.7-eleven.com', 'https://www.kwiktrip.com', 'https://www.sheetz.com', 'https://www.shell.us', 'https://www.caseys.com', 'https://www.cumberlandfarms.com', 'https://www.speedway.com', 'https://www.circlek.com', 'https://www.beautyencounter.com', 'https://www.sallybeauty.com', 'https://tartecosmetics.com', 'https://www.aveda.com', 'https://www.beautybrands.com', 'https://www.esteelauder.com', 'https://www.sephora.com', 'https://www.ulta.com', 'https://www.bathandbodyworks.com', 'https://www.elfcosmetics']
