install:
	# install commands
	pip install --upgrade pip && pip install -r requirements.txt

format:
	# format code
	black src/. tests/. 

lint:
	# flake8 or pylint
	pylint --disable=too-many-locals,R,C src/. tests/.  
test:
	# test
	# python -m pytest --cov=mylib -r tests/
build:
	# build build
	docker build -t fastapi-arxiv-hunter .
run:
	# docker run
	# docker run -p 127.0.0.1:8080:8080 710189aade17
	docker run -t -d -p 9000:9000 81f2ea45a53d
deploy:
	# deploy
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	# docker build -t fastapi-wiki .
	# docker tag fastapi-wiki:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
	# docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
install-local:
	# use this to work with poetry in your local environment, github actions were throwing error
	# poetry install --no-root
all: format lint build run deploy
run-fastapi:
	# Run fastapi
	uvicorn src.app.main:app --reload

run-extractor:
	black src/business_logic/arxiv_extractor.py
	pylint src/business_logic/arxiv_extractor.py