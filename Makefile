venv:
	virtualenv -p /usr/bin/python3.5 .venv

init:
	python -m pip install --upgrade pip setuptools wheel
	pip install -r requirements.txt