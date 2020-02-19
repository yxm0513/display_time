FROM python:3


WORKDIR /usr/src
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
CMD [ "python3", "time.py" ]
