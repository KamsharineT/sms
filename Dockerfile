FROM python:3.8.2

RUN pip install mysql-connector-python

WORKDIR C:\Users\kamsharine\Documents\Flotech\2022\Task04(Sms)\SMSDocker\Docker\pub\sms
# directory of python file

#have to install eveyrhing , installed and used in the python dfile
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /input/recipients.csv recipients.csv 

COPY sms.py ./

CMD ["python3","./sms.py"]