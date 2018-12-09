FROM python:3.6
COPY . /tests
ARG chrome_driver
ENV CHROME_DRIVER $chrome_driver
WORKDIR /tests 
RUN pip install -r requirements.txt
CMD ["python","test.py"]