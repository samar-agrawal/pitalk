import os
import aiml

KERNEL = aiml.Kernel()
KERNEL.setBotPredicate('name', 'Sirius')
KERNEL.setBotPredicate('master', 'Samar')

if os.path.isfile("pitalk/aiml/bot_brain.brn"):
    KERNEL.bootstrap(brainFile="pitalk/aiml/bot_brain.brn")
else:
    KERNEL.bootstrap(learnFiles="pitalk/aiml/std-startup.xml", commands="load aiml b")
    KERNEL.saveBrain("pitalk/aiml/bot_brain.brn")
