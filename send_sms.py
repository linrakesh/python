from twilio.rest import Client

# put your own credentials here
account_sid = "AC8d34c126510c1a0f143b3e86d3f52a51"
auth_token = "baf27d709fa8832617b8c97dfa33b429"

client = Client(account_sid, auth_token)
client.messages.create(
    to="+919871816901",
    from_="09871816901",
    body="This sms is received via python script" )