FROM python:3.6-slim

COPY ./requirements.txt /app/requirements.txt

COPY ./*.py /app/

COPY ./table/*.py /app/table/

COPY ./run.sh /app/run.sh

WORKDIR /app

RUN chmod +x run.sh

ENV TERM=xterm-256color

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "bs.py", "items.txt"] 
