import urllib.parse
import requests

def get_twitter_user_id(username, bearer_token):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and 'data' in response.json():
        return response.json()['data']['id']
    else:
        return None

def create_twitter_url():
    bearer_token = input("Enter your Bearer Token: ")
    print("Choose the action:")
    print("1) Follow a user")
    print("2) DM a user")
    print("3) Tweet out a pre-populated text")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        username = input("Enter the Twitter username of the user to follow: ")
        user_id = get_twitter_user_id(username, bearer_token)
        if user_id:
            url = f"https://twitter.com/intent/follow?user_id={user_id}"
        else:
            return "User ID not found or request failed."

    elif choice == '2':
        username = input("Enter the username of the recipient: ")
        user_id = get_twitter_user_id(username, bearer_token)
        if user_id:
            message = input("Enter the message to send (optional, press enter to skip): ")
            encoded_message = urllib.parse.quote_plus(message)
            url = f"https://twitter.com/messages/compose?recipient_id={user_id}&text={encoded_message}"
        else:
            return "User ID not found or request failed."

    elif choice == '3':
        message = input("Enter the text to tweet (optional, press enter to skip): ")
        encoded_message = urllib.parse.quote_plus(message)
        url = f"https://twitter.com/intent/tweet?text={encoded_message}"

    else:
        return "Invalid choice. Please enter 1, 2, or 3."

    return url

# Example usage
print(create_twitter_url())
