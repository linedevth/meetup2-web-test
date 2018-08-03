# meetup2-web-test
web ui automation test sample for linedevth meetup#2

## Prerequisite
- Python 3.6
- Docker
- Recorded Video Storage e.g. Amazon S3

## How to Run
### Setup Python Environment
```
sh$ virtualenv -p python3 venv
sh$ source venv/bin/activate
sh$ pip install -r requirements.txt
```
### Run Test Locally
```
sh$ export LOCAL_WEBDRIVER_ENABLE=true
sh$ pytest tests
```
