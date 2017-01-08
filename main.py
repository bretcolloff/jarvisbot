import os
import random
import sys
import time
import telepot

adminuser = "<replace_me>"
apitoken = '<replace_me>'

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print msg
    if content_type == 'text':
        # Filter to only messages sent from the owner.
        if msg['from']['username'] != adminuser:
            return

        msgtext = msg['text']

        # Parrot feature.
        if msgtext.startswith("jarvis say"):
            response = msgtext.split()
            response.pop(0)
            response.pop(0)


            # Pause for a more natural response.
            waittime = random.uniform(1.0, 1.9)
            time.sleep(waittime)

            bot.sendMessage(chat_id, ' '.join(response))

bot = telepot.Bot(apitoken)
bot.message_loop(handle)
print "Booting..."

# Keep the program running.
while 1:
    time.sleep(10)
