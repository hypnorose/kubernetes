FROM python:3.8-slim-buster
ENV FLASK_APP=/app/main.py
ENV FLASK_ENV=development
RUN pip3 install flask
RUN pip3 install psycopg2-binary
COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]