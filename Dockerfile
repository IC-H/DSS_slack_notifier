FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /slack_to_line_notifier
WORKDIR /slack_to_line_notifier
COPY requirements.txt /slack_to_line_notifier/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /slack_to_line_notifier/

