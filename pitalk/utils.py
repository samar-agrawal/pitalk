'''Performing some actions'''

import os
import subprocess

def restart():
    '''Restart the system'''

    #from .app import BOT

#    show_keyboard = {'keyboard': ['Yes','No']}
#    response = BOT.sendMessage(user_id, "Are you sure?", reply_markup=show_keyboard)
#    print(response)
#    os.system("sudo reboot")
    return 'Rebooted'

def temperature():
    '''Check the temperature of pi'''

    temp = float(subprocess.check_output(
        ["/opt/vc/bin/vcgencmdmeasure_temp | cut -c6-9"], shell=True)[:-1])
    return 'My temperature is {temp} C'.format(temp=str(temp))

def disk_space():
    '''Check available disk space'''

    result = subprocess.check_output("df -h .", shell=True)
    output = result.split()
    formatted_output = {
        'total':output[8],
        'used':output[9],
        'used_percentage':output[11],
        'free':output[10]}
    return 'Disk space:\nTotal: {total}\nUsed:{used} ({used_percentage})\nFree:{free}'.format(
        **formatted_output)

def load_aiml():
    '''reload aiml files'''

    from . import KERNEL
    KERNEL.respond('load aiml b')
    return 'Data crammed...brain reloaded..shoot'

def save():
    '''save brain file'''

    from . import KERNEL
    KERNEL.saveBrain("bot_brain.brn")
    return 'brain saved'

def perform_action(message, user_id):
    '''perform user actions '''

    if user_id != int(os.environ['BOT_CREATOR_ID']):
        return 'My creator has not authorized you to perform this action'

    action_index = [c in message for c in ACTION_DICT.keys()].index(True)
    try:
        response = ACTION_DICT[ACTION_DICT.keys()[action_index]]()
    except ValueError:
        response = 'Insufficient Permissions to execute actions'

    return response

ACTION_DICT = {
    'disk':disk_space,
    'temperarure':temperature,
    'load_aiml':load_aiml,
    'space':disk_space,
    'hot':temperature,
    'restart':restart,
    'reboot':restart,
    'save':save}
