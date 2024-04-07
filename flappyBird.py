from twilio.rest import Client

# Your Twilio account SID and authentication token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Your Twilio phone number and the recipient's phone number
twilio_phone_number = 'your_twilio_phone_number'
recipient_phone_number = 'recipient_phone_number'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send a message
message = client.messages.create(
    body='Hello, this is a test message from Twilio!',
    from_=twilio_phone_number,
    to=recipient_phone_number
)

# Print the message SID
print(message.sid)
