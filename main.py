from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import re

def get_user_id_from_twitvd(username, headless=False):
    # Configure Chrome options
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")

    # Initialize Selenium WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open twitvd.com
        driver.get("https://twitvd.com/twitter-id/")

        # Find the input field and submit button by CSS selector
        input_field = driver.find_element(By.CSS_SELECTOR, "#username")
        submit_button = driver.find_element(By.CSS_SELECTOR, "#convertBtn")

        # Enter the username and click the submit button
        input_field.clear()
        input_field.send_keys(username)
        submit_button.click()

        # Wait for the result to be displayed
        wait = WebDriverWait(driver, 10)
        result_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#result")))

        # Extract the text from the result field
        result_text = result_field.text

        # Extract the user ID using regular expression
        match = re.search(r'is (\d+)', result_text)
        if match:
            user_id = match.group(1)
            return user_id
        else:
            return "User ID not found."
    finally:
        # Close the browser
        driver.quit()

def create_twitter_url(headless=False):
    print("Choose the action:")
    print("1) Follow a user")
    print("2) DM a user")
    print("3) Tweet out a pre-populated tweet")
    
    choice = input("Enter your choice (1, 2, or 3): ")

    user_id = None
    if choice in ['1', '2']:
        username = input("Enter the Twitter username: ")
        user_id = get_user_id_from_twitvd(username, headless=headless)

    if choice == '1':
        url = f"https://twitter.com/intent/follow?user_id={user_id}"
    elif choice == '2':
        message = input("Enter the message to send (optional, press enter to skip): ")
        encoded_message = urllib.parse.quote_plus(message)
        url = f"https://twitter.com/messages/compose?recipient_id={user_id}&text={encoded_message}"
    elif choice == '3':
        message = input("Enter the text to tweet (optional, press enter to skip): ")
        encoded_message = urllib.parse.quote_plus(message)
        url = f"https://twitter.com/intent/tweet?text={encoded_message}"
    else:
        return "Invalid choice. Please enter 1, 2, or 3."

    return url

# Set headless to True or False based on your preference
headless_mode = True

# Example usage
print(create_twitter_url(headless=headless_mode))
