import os
import time

import telepot
import aiml

bot = telepot.Bot(os.environ['TELEGRAM_TOKEN'])

kernel = aiml.Kernel()

RUN_TIME = 5
kernel.setBotPredicate('name', 'Sirius')
kernel.setBotPredicate('master', 'Samar')

if os.path.isfile("aiml/bot_brain.brn"):
    kernel.bootstrap(brainFile = "aiml/bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "aiml/std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("aiml/bot_brain.brn")

def Restart():
    os.system("sudo reboot")
    return 'Rebooted'

def Temp():
    t=float(subprocess.check_output(["/opt/vc/bin/vcgencmdmeasure_temp | cut -c6-9"], shell=True)[:-1])
    ts=str(t)
    return "My temperature is "+ts+" C"

def Disk():
    result=subprocess.check_output("df -h .", shell=True)
    output=result.split()
    return "Disk space:\nTotal: "+output[8]+"\nUsed:"+output[9]+" ("+output[11]+")\nFree: "+output[10]

def hi():
    return 'Hola amigo!!!'

def handle(msg):                                                  
    print msg
    message, id = msg['text'], msg['from']['id']
    if 'disk' in message:
        response = Disk()
    elif message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        response = kernel.respond(message)

    bot.sendMessage(id, response) # reply_markup=show_keyboard)
    time.sleep(RUN_TIME)

bot.message_loop(handle)

while True:
    time.sleep(RUN_TIME)

#bot.sendMessage(samar, 'Good morning!')

#show_keyboard = {'keyboard': [['Yes','No']]}

#TODO: move to twisted
