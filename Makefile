install:
	pip install telepot
	pip install pyaiml

remove:
	rm aiml/bot_brain.brn

run:
	$(install)
	$(remove)
	python -m pitalk.app
