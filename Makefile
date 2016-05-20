install:
	pip install telepot

remove:
	rm aiml/bot_brain.brn

run:
	$(install)
	$(remove)
	python app.py
