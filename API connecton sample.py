import requests

API_BASE_URL = "http://SERVER_IP:3001/api/v1" #Replace SERVER_IP with your server IP
AUTHTOKEN = "API_TOKEN"  # Replace API_TOKEN with API token
WORKSPACE_SLUG = "WS_NAME"  # Replace WS_NAME with workspace name in lower case, e.g., workspace name "myWS" will be "myws"

def send_chat_message(message, mode="chat"):
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "message": message,
        "mode": mode
    }
    response = requests.post(f"{API_BASE_URL}/workspace/{WORKSPACE_SLUG}/chat", json=data, headers=headers)
    if response.status_code == 200:
        print("Message sent successfully.")
        print("Response:", response.json().get('textResponse'))
    else:
        print("Failed to send message.")
        print("Response:", response.json())

if __name == "__main":
    print("Chatbot is running. Type 'exit' to stop.")
    while True:
        user_input = input("Enter your message: ")
        if user_input.lower() == 'exit':
            print("Exiting chatbot.")
            break
        send_chat_message(user_input) 
