FROM python:3.12-alpine
WORKDIR /sitio
COPY servidor.py .
COPY index.html .
COPY img ./img
COPY audio ./audio
CMD ["python3", "servidor.py"]
