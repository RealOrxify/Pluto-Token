import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="PlutoSphere username")
parser.add_argument("-p", "--password", help="PlutoSphere password")
parser.add_argument("-t", "--tokens", type=int, help="Number of tokens to add")
args = parser.parse_args()

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open the PlutoSphere login page
driver.get("https://my.plutosphere.com/login")

# Enter username and password from command-line arguments
username_field = driver.find_element_by_id("username")
username_field.send_keys(args.username)

password_field = driver.find_element_by_id("password")
password_field.send_keys(args.password)

# Click the login button
login_button = driver.find_element_by_id("login-button")
login_button.click()

# Wait for the tokens page to load
tokens_page_loaded = False
while not tokens_page_loaded:
    try:
        driver.find_element_by_id("tokens-tab")
        tokens_page_loaded = True
    except:
        pass

# Open the tokens tab
tokens_tab = driver.find_element_by_id("tokens-tab")
tokens_tab.click()

# Enter the token amount from command-line arguments
token_amount_field = driver.find_element_by_id("token-amount")
token_amount_field.send_keys(args.tokens)

# Click the add tokens button
add_tokens_button = driver.find_element_by_id("add-tokens-button")
add_tokens_button.click()

# Wait for the confirmation message
confirmation_message_displayed = False
while not confirmation_message_displayed:
    try:
        driver.find_element_by_id("tokens-added-message")
        confirmation_message_displayed = True
    except:
        pass

# Close the browser window
driver.quit()
