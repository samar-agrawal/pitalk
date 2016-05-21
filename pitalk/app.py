'''Perform action / respond using aiml through telegram '''

import os
import time

import telepot
from . import KERNEL
from utils import restart, temperature, disk_space, perform_action, ACTION_DICT

BOT = telepot.Bot(os.environ['TELEGRAM_TOKEN'])

RUN_TIME = 5

def handle(msg):
    '''handle user input and perform some action '''
    print msg

    message, username, user_id = msg['text'], msg['from']['first_name'], msg['from']['id']

    if any(q in message for q in ACTION_DICT.keys()):
       response = perform_action(message, user_id)
    else:
        response = KERNEL.respond(message)

    if not response:
        response = KERNEL.respond('exit')

    BOT.sendMessage(user_id, response)
    time.sleep(RUN_TIME)

BOT.message_loop(handle)

while True:
    time.sleep(RUN_TIME)
