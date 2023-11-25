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
            return match.group(1)
        else:
            return "User ID not found."
    finally:
        # Close the browser
        driver.quit()

def create_twitter_action_url(choice, username=None, message=None, headless=False):
    user_id = None
    if choice in ['1', '2']:
        user_id = get_user_id_from_twitvd(username, headless=headless)

    if choice == '1' and user_id:
        return f"https://twitter.com/intent/follow?user_id={user_id}"
    elif choice == '2' and user_id:
        encoded_message = urllib.parse.quote_plus(message)
        return f"https://twitter.com/messages/compose?recipient_id={user_id}&text={encoded_message}"
    elif choice == '3':
        encoded_message = urllib.parse.quote_plus(message)
        return f"https://twitter.com/intent/tweet?text={encoded_message}"

    return None
