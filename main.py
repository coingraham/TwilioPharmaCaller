import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Start

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER'] # This is the twilio number I'm calling from
pharma = os.environ['PHARMA']  # This is the pharmacy phone number
script = os.environ['SCRIPT_NUMBER']  # This is my prescription number e.g. "4, 5, 6, 2, 1"
my_number = os.environ['PHONE_VERIFICATION']  # This is my cell number to verify my script

client = Client(account_sid, auth_token)
response = VoiceResponse()
start = Start()

response.append(start)
response.pause(length=30)

response.say("refill a prescription")
response.pause(length=5)

response.say(script)
response.pause(length=5)

response.say("yes")
response.pause(length=5)

response.say(my_number)
response.pause(length=10)
response.hangup()

call = client.calls.create(twiml=str(response), record=True, to=pharma, from_=twilio_number)

print(call.sid)
