FROM python:3.8.9

ENV PYTHON3DONTWRITEBYTECODE 1
ENV PYTHON3BUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0.8000" ]


