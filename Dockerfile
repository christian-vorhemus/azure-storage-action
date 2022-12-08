FROM mcr.microsoft.com/cbl-mariner/base/python:3

WORKDIR /github/workspace/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python3", "/github/workspace/main.py" ]