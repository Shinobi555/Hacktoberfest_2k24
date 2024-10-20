FROM python:3.10-slim

WORKDIR .

COPY /app .

RUN pip install -r requirements.txt

CMD ["fastapi","run" ,"main.py"]