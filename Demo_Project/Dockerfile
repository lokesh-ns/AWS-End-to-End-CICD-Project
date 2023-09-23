FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
EXPOSE 9000
CMD ["python", "manage.py", "runsever", "0.0.0.0:9000"]

