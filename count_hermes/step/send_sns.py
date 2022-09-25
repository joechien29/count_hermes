from twilio.rest import Client
from setting import account_sid
from setting import auth_token
from setting import my_phone
from setting import from_phone


def send_sns():
    sid = account_sid
    token = auth_token
    body = 'New Products for Sale at Hermes'
    client = Client(sid, token)
    message = client.messages.create(
        from_=from_phone,
        body=body,
        to=my_phone
    )
    print(message.sid)
