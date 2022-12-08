import requests

# define the API key and the URL of the Telegram API
api_key = "YOUR_API_KEY"
api_url = "https://api.telegram.org/bot{}/".format(api_key)

# define the recipient of the spam messages and the message text
recipient = "USERNAME"
text = "This is a spam message."

# send the first message to the recipient
response = requests.post(api_url + "sendMessage", json={
    "chat_id": recipient,
    "text": text,
})

# check the response status code to see if the message was sent successfully
if response.status_code == 200:
    print("The first message was sent successfully.")
else:
    print("An error occurred while sending the first message.")

# send additional messages to the recipient using a loop
for i in range(1, 10):
    response = requests.post(api_url + "sendMessage", json={
        "chat_id": recipient,
        "text": text,
    })

    # check the response status code to see if the message was sent successfully
    if response.status_code == 200:
        print("The {} message was sent successfully.".format(i+1))
    else:
        print("An error occurred while sending the {} message.".format(i+1))