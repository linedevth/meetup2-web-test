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
sh$ source venv/bin/active
sh$ pip install -r requirements.txt
```
### Run Test Locally
```
sh$ docker build -t . webtest:latest
sh$ docker network create testing_network
sh$ docker pull elgalu/selenium:3.13.0-p3
sh$ docker pull dosel/zalenium:3.13.0a
sh$ docker run -ti -d --network testing_network --name zalenium \
    -p 4444:4444 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /tmp/videos:/home/seluser/videos --privileged \
    dosel/zalenium:3.13.0a start --debugEnabled true --videoRecordingEnabled true --maxDockerSeleniumContainers 4 --desiredContainers 2 --maxTestSessions 10
```
