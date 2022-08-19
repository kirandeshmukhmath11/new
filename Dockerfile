#Dockerfile, Image, Container
FROM python:3.9

ADD main.py .

RUN pip install gspread pyinstaller 

CMD [ "python","./main.py" ]