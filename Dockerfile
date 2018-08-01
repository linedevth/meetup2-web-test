FROM kamon70/allure-python3.7

ADD ./tests /tests
ADD requirements.txt /tests/requirements.txt
WORKDIR /tests
RUN pip install -r requirements.txt

ENV REMOTE_WEBDRIVER_URL=http://zalenium:4444/wd/hub