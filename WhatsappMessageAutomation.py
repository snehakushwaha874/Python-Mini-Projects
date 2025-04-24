import pywhatkit as kit
import datetime

# User input
phone_number = "+91XXXXXXXXXX"  #number of recipent (with country code)
message = "Hello, this is automated message sent using python"
now = datetime.datetime.now()
send_hour = now.hour
send_minute = now.minute + 2  #to send after 2 minutes 

# Send message
kit.sendwhatmsg(phone_number, message, send_hour, send_minute)
