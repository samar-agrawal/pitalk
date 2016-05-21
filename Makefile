install:
	pip install telepot
	pip install pyaiml
	python setup.py develop	

remove:
	rm pitalk/aiml/bot_brain.brn

run:
	python -m pitalk.app
