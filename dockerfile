FROM python:3
ADD script.py /
RUN pip install pystrich
COPY crypto_data.csv .
CMD ["python","./script.py"]
