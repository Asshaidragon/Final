FROM python:3.7-alpine
WORKDIR /Users
COPY requirements.txt /Users
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /Users
ENTRYPOINT ["python3"]
CMD ["logic.py"]


