FROM python:3
RUN mkdir /opt/pythonProjet
WORKDIR /opt/pythonProjet/
ADD script.py .
RUN pip install mysql-connector-python
COPY crypto_data.csv .
CMD ["python","./script.py"]
