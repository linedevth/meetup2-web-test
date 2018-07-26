FROM kamon70/allure-python3.7

ADD ./tests /tests
WORKDIR /tests
ENV REMOTE_WEBDRIVER_URL=http://zalenium:4444/wd/hub