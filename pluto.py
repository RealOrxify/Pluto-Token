import requests

# PlutoSphere API URL
api_url = "https://api.plutosphere.com/"

# Prompt for username and token amount
username = input("Enter your PlutoSphere username: ")
token_amount = int(input("Enter the amount of tokens to add: "))

# Login to PlutoSphere
login_data = {"username": username, "password": password}
login_response = requests.post(api_url + "auth/login", json=login_data)

if login_response.status_code == 200:
    # Get user ID from login response
    user_id = login_response.json()["user"]["id"]

    # Add tokens to user account
    add_tokens_data = {"userId": user_id, "amount": token_amount}
    add_tokens_response = requests.post(api_url + "users/addTokens", json=add_tokens_data)

    if add_tokens_response.status_code == 200:
        print("Tokens added successfully.")
    else:
        print("Error adding tokens:", add_tokens_response.status_code)
else:
    print("Login failed:", login_response.status_code)
