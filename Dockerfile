FROM mcr.microsoft.com/cbl-mariner/base/python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT [ "python3", "main.py" ]