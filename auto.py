from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse
import re
import time

def get_twitter_user_id(username):
    # Initialize a Selenium WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the Twitter profile page
        driver.get(f"https://twitter.com/{username}")

        # Wait for the page to load
        time.sleep(5)  # Adjust time as necessary

        # Get the page source
        page_source = driver.page_source

        # Use BeautifulSoup to parse the page source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Search for the user ID using a regular expression
        user_id = re.search(r'\"userId\":\"(\d+)\"', str(soup))

        if user_id:
            return user_id.group(1)
        else:
            return "User ID not found."
    finally:
        # Close the browser
        driver.quit()

def create_twitter_url():
    print("Choose the action:")
    print("1) Follow a user")
    print("2) DM a user")
    print("3) Tweet out a pre-populated text")
    
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        username = input("Enter the Twitter username of the user to follow: ")
        user_id = get_twitter_user_id(username)
        if user_id.isdigit():
            url = f"https://twitter.com/intent/follow?user_id={user_id}"
        else:
            return user_id

    elif choice == '2':
        username = input("Enter the username of the recipient: ")
        user_id = get_twitter_user_id(username)
        if user_id.isdigit():
            message = input("Enter the message to send (optional, press enter to skip): ")
            encoded_message = urllib.parse.quote_plus(message)
            url = f"https://twitter.com/messages/compose?recipient_id={user_id}&text={encoded_message}"
        else:
            return user_id

    elif choice == '3':
        message = input("Enter the text to tweet (optional, press enter to skip): ")
        encoded_message = urllib.parse.quote_plus(message)
        url = f"https://twitter.com/intent/tweet?text={encoded_message}"

    else:
        return "Invalid choice. Please enter 1, 2, or 3."

    return url

# Example usage
print(create_twitter_url())
