import os
import time

import telepot

bot = telepot.Bot(os.environ['TELEGRAM_TOKEN'])

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
    text, id = msg['text'], msg['from']['id']
    #TODO: move to yml
    if 'hola' in text:
        response = hi()
    elif 'disk' in text:
        response = Disk()
    elif 'temp' in text:
        response = Temp()
    elif 'restart' in text:
        response = Restart()
    else:
        response = 'What was that?'
    bot.sendMessage(id, response) # reply_markup=show_keyboard)
    time.sleep(10)

bot.message_loop(handle)

while True:
    time.sleep(10)

#bot.sendMessage(samar, 'Good morning!')

#show_keyboard = {'keyboard': [['Yes','No']]}

#TODO: move to twisted
