'''Perform action / respond using aiml through telegram '''

import os
import sys
import telepot

from telepot.delegate import per_chat_id, create_open
from telepot.namedtuple import Message

from . import KERNEL
from .utils import perform_action, ACTION_DICT

TOKEN = os.environ['TELEGRAM_TOKEN'] or sys.argv[1]

class MessageProcessor(telepot.helper.ChatHandler):
    '''Initiate chat socket for a client and respond to the input query'''

    def __init__(self, seed_tuple, timeout):
        super(MessageProcessor, self).__init__(seed_tuple, timeout)

    def on_chat_message(self, msg):
        '''process and response message'''

        ntuple = Message(**msg)

        if telepot.glance(msg)[0] == 'text':

            if any(q in ntuple.text for q in ACTION_DICT.keys()):
                response = perform_action(ntuple.text, ntuple.from_.id)
            else:
                response = KERNEL.respond(ntuple.text)

        #if not response:
            #response = self.sender.sendMessage(
               # chat_id, 'I do not understand your last message.', reply_to_message_id=msg_id)
        self.sender.sendMessage(response)


BOT = telepot.DelegatorBot(TOKEN, [
    (per_chat_id(), create_open(MessageProcessor, timeout=10)),
])

BOT.message_loop(run_forever=True)
