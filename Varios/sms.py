# Sending an SMS using the Twilio API
from twilio.rest import Client
# put your own credentials here
account_sid = "AC1473cb1f850b6c3b736092397a0f4608"
auth_token = "c5f15d439a7b3768c01774fce1dab54e"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+18315316786",
  from_="+18315316786",
  body="Tomorrow's forecast in Financial District, San Francisco is Clear",
  media_url="https://climacons.herokuapp.com/clear.png")
