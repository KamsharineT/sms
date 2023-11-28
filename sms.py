##########################################################################################################
##Developer : Kamsharine Thayananthan                                                                   ##
##Purpose   : This is written to send sms to the respective persons if there are any alarms                     ##
##Date      : 2022/11/14                                                                                ##
##########################################################################################################

import mysql.connector
from wavecell import Wavecell
import time
import csv
from datetime import datetime,timedelta
from pytz import utc
import os
import requests
import json
import messagebird
import psycopg2


conn = mysql.connector.connect(user = 'root', password = 'root' ,host='localhost', port = "3306", database="alarms") #local machine- testing purpose
# conn = mysql.connector.connect(user = os.environ['MYSQL_USER'], password = 'root' ,host=os.environ['MYSQL_HOST'], port = "3310", database="alarms")
print("DB Connected")

cursor = conn.cursor()

fetchapi = ""
email = "admin@gmail.com"
password = "123123"
Headers = {'Authorization': 'jwt ' + ''}


def alarm(devicetag,chl,cond,Do,ph,tur,status,rectime,depth,device_type):
    connection = psycopg2.connect(
    host="",
    database="",
    port="",
    user="",
    password="")
    maincur = connection.cursor()

    sqlcom = "Select stname,pH_min,pH_max,Chladj_min,Chladj_max,DO_min,DO_max,Conductivity_min,Conductivity_max,Turbidity_min,Turbidity_max from stations_det where stnameid = %s"
    cursor.execute(sqlcom, (devicetag,))
    limits = cursor.fetchall()

    print(limits)
    print(devicetag," depths ",depth)
    body = ""
    if (len(limits))>0:
        # for x in range(depth):
            # print("x ",x)
            # if x <= 2:
                for i in limits:
                    ilist = list(i)
                    print("ilist ",ilist)
                    #GET THE minimum and maximum value of sensor values

                    stnnamedet = ilist[0]
                    print(stnnamedet,"stnnamedet")
                    pH_min = ilist[1]
                    pH_max = ilist[2]
                    Chladj_min = ilist[3]
                    Chladj_max = ilist[4]
                    DO_min = ilist[5]
                    DO_max = ilist[6]
                    Conductivity_min = ilist[7]
                    Conductivity_max = ilist[8]
                    Turbidity_min = ilist[9]
                    Turbidity_max = ilist[10]
                    rectime = datetime.strptime(rectime,'%Y-%m-%d %H:%M:%S')
                    # if(x==0):
                    rectime =  rectime + timedelta(hours=(+8)) # get local time(+08:00)
                    rectime = datetime.strftime(rectime,'%Y-%m-%d %H:%M:%S')

                    if(Chladj_max is not None):
                        if float(chl) < 100 and float(chl) > float(Chladj_max):
                            if(devicetag) in (""):
                                smsbody = "\n"+"Chl-Adj:"+str(chl)+" ug/l"+"\n"+str(rectime)+"\n"+"UL:"+str(Chladj_max)+"\n"+"LL:"+str(Chladj_min)+"\n1) Site check"+"\n2) MRRS2/aeration/boat churning/SPC"
                                body = body+smsbody
                            else:
                                if(devicetag) not in (""):
                                    smsbody = "\n"+"Chl-Adj:"+str(chl)+" ug/l"+"\n"+str(rectime)+"\n"+"UL:"+str(Chladj_max)+"\n"+"LL:"+str(Chladj_min)+"\n1) Site check"+"\n2) aeration/boat churning/SPC"
                                    body = body+smsbody
                        if float(chl) > 100:
                            if(devicetag) in (""):
                                smsbody = "\n"+"Chl-Adj:"+str(chl)+" ug/l"+"\n"+str(rectime)+"\n"+"UL:"+str(Chladj_max)+"\n"+"LL:"+str(Chladj_min)+"\n1) Site check"+"\n2) MRRS/ aeration/boat churning/scum removal"
                                body = body+smsbody
                            else:
                                if(devicetag) not in (""):
                                    smsbody = "\n"+"Chl-Adj:"+str(chl)+" ug/l"+"\n"+str(rectime)+"\n"+"UL:"+str(Chladj_max)+"\n"+"LL:"+str(Chladj_min)+"\n1) Site check"+"\n2) aeration/boat churning/scum removal"
                                    body = body+smsbody

                    if float(ph) < float(pH_min):
                            smsbody = "\n"+"pH:"+str(ph)+"\n"+str(rectime)+"\n"+"UL:"+str(pH_max)+"\n"+"LL:"+str(pH_min)+"\n1) Check by WQ probe"+"\n2) Chemical smell/illegal discharges?"+"\n3) Fish kill?"
                            body = body+smsbody
                    if float(ph) > float(pH_max):
                            smsbody = "\n"+"pH:"+str(ph)+"\n"+str(rectime)+"\n"+"UL:"+str(pH_max)+"\n"+"LL:"+str(pH_min)+"\n1) Check by WQ probe"+"\n2) Algal scum/aquatic plant/smell/discharge/fish kill?"
                            body = body+smsbody
                    print('dox',Do,'Domin',DO_min)
                    if float(Do) < float(DO_min) :
                        print("do")
                        smsbody = "\n"+"DO:"+str(Do)+" mg/l"+"\n"+str(rectime)+"\n"+"UL:"+str(DO_max)+"\n"+"LL:"+str(DO_min)+"\n1) Check by WQ probe"+"\n2) Aerator working?"+"\n3) Decayed matters/bubbles/smell/fish kill?"
                        body = body+smsbody
                    else:
                        # smsbody = str(stnnamedet)+"\n"+"DO:"+str(dox)+"mg/l"+"\n"+str(createdn)+"\n"+"UL:"+str(DO_max)+"\n"+"LL:"+str(DO_min)+"\n1) Check by WQ probe"+"\n2) Aerator working?"+"\n3) Decayed matters/bubbles/smell/fish kill?"
                        # print(smsbody)
                        print("Do fine")
                    if float(cond) > float(Conductivity_max):
                        smsbody = "\n"+"Cond:"+str(cond)+" uS/cm"+"\n"+str(rectime)+"\n"+"UL:"+str(Conductivity_max)+"\n"+"LL:"+str(Conductivity_min)+"\n1) Check by WQ probe"+"\n2) Due to high tide/no rain?"+"\n3) Illegal discharges?"
                        body = body+smsbody
                    else:
                        # smsbody = str(stnnamedet)+"\n"+"Cond:"+str(cond)+"uS/cm"+"\n"+str(createdn)+"\n"+"UL:"+str(Conductivity_max)+"\n"+"LL:"+str(Conductivity_min)+"\n1) Check by WQ probe"+"\n2) Due to high tide/no rain?"+"\n3) Illegal discharges?"
                        # print(smsbody)
                        print("con fine")

                    if(Turbidity_max is not None):
                        if(devicetag) not in ("SE540","SE533","SE544"):
                            if float(tur) > float(Turbidity_max):
                                smsbody = "\n"+"Turb:"+str(tur)+" NTU"+"\n"+str(rectime)+"\n"+"UL:"+str(Turbidity_max)+"\n"+"LL:"+str(Turbidity_min)+"\n1) Recent rain?"+"\n2) Abnormal discharges?"
                                body = body+smsbody
                            else:
                                # smsbody = str(stnnamedet)+"\n"+"Turb:"+str(tur)+" NTU"+"\n"+str(createdn)+"\n"+"UL:"+str(Turbidity_max)+"\n"+"LL:"+str(Turbidity_min)+"\n1) Recent rain?"+"\n2) Abnormal discharges?"
                                # body = body+smsbody
                                # print(smsbody)
                                print("tur fine")

                                        # if device_type == "pontoon" and body != "":
                    #     depthbody = "\n"+"depth :"+str(depth)+"\n"
                    #     body = body + depthbody

                    if rectime is not None:
                        print(rectime)
                        #if the last transmission time is less than 1.5 hrs of the current time
                        lasttime = datetime.strptime(rectime,"%Y-%m-%d %H:%M:%S") + timedelta(minutes=(+90))
                        lasttime = datetime.strftime(lasttime,"%Y-%m-%d %H:%M:%S")
                        lasttime = datetime.strptime(lasttime,"%Y-%m-%d %H:%M:%S")

                    # print('lasttime',lasttime)

                    current_time = datetime.now(utc) +timedelta(hours=(+8))  #current date time
                    current_time = datetime.strftime(current_time,"%Y-%m-%d %H:%M:%S")
                    # print('current_time',current_time)
                    current_time = datetime.strptime(current_time,"%Y-%m-%d %H:%M:%S")

                    print('current_time',current_time," ",lasttime," ",devicetag)
                    # cnt = 0
                    if(rectime is not None):
                        print("last time is not none")
                        # print(lasttime , "  ",current_time)
                        # try:
                        if(1 == 1):
                            print("yes")
                            if lasttime < current_time :
                                print('current_time',current_time," ",lasttime," ",devicetag)
                                print("offline")
                                status = "offline"

                    if device_type == "pontoon" and status != "offline":
                        cnt = 0
                        # status = "online"
                        sensors = ["pH","DO_Concentration","Temperature","Chlorophyll-a","Turbidity","Conductivity"]

                        for j in sensors:
                                sensorq = ("SELECT value_float,record_time FROM ( SELECT parameter_tag,value_float,record_time, ROW_NUMBER () OVER (ORDER BY record_time desc) FROM device_data where device_tag = '"+devicetag+"' and parameter_tag = '"+j+"' order by record_time desc) x WHERE ROW_NUMBER<=6 and ROW_NUMBER >= 0 ")

                                maincur.execute(sensorq)
                                sensordata = maincur.fetchall()

                                for l in range(len(sensordata)):
                                    val =  (all(x == sensordata[l][0] for x in sensordata))
                                    if val:
                                        cnt = cnt+1

                                    if cnt > 5:
                                        status = "fault"



                    if status in ("offline","fault"):
                        smsbody = "\n"+"Station "+status+"\n"+str(rectime)
                        body = body+smsbody
                    else:
                        status = "online"


                # body = body+"\n"

    print("body",body)

    if (body != ""):
        today = datetime.now(utc) + timedelta(hours=(+8)) # get local time(+08:00)
        today = datetime.strftime(today,'%Y-%m-%dT%H:%M:%S.%f+08:00')
        todaycon = datetime.strptime(today,'%Y-%m-%dT%H:%M:%S.%f+08:00')

        #fetch the old alarm details where sms sent already to the recipients
        outersql = "SELECT stnameid FROM alarms_det where smssent = 'No' and stnameid ='"+devicetag+"'"
        cursor.execute(outersql)
        out = cursor.fetchall()

        print(today," today")
        #fetch the old alarm details where sms sent already to the recipients
        innersql = "SELECT stnameid FROM alarms_det where smssent = 'yes' and stnameid ='"+devicetag+"'"
        cursor.execute(innersql)
        inout = cursor.fetchall()

        print(inout," inout")
        if len(inout)==0:
            q="INSERT INTO alarms_det (stnameid, alarmname,alarmcreated, date,smssent) VALUES(%s,%s,%s,%s,%s)"
            val = (devicetag,"None",rectime,todaycon,"No")
            cursor.execute(q,val)
            conn.commit()

            print("sentsms body")
            print(body)
            sentsms(body,stnnamedet,devicetag) # commented for testing

    connection.close()
    # else:
    #     smsbody = str(stnnamedet)+"\n"+"Device Status is"+status+"\n"+str(createdn)
    #     body = body+smsbody

def sentsms(body,stnnamedet,devicetag):

    client = messagebird.Client('')

    source = "Kamsharine"

    body = str(stnnamedet)+body
    print(body," ",source)
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("dir",files)
    print("Files in %r: %s" % (cwd, files))

    with open("recipients.csv",'r') as csv_file:
        filereader = csv.reader(csv_file)
        print('filereader')
        next(filereader)
        for i in filereader:
            if i[2] == devicetag:

                print("**************** body")
                # print(i[1])
                # print(body," ",source)
                print(str(i[1]))
                # p = {"source": str(source),"destination": str(i[1]),"text": str(body)}
                # p = {"source": str(source),"destination": str(+6580135448),"text": str("testing sms")}
                # result = w.send_sms_single(param=p) # to sent sms //commented for testing purpose
                # smscnt = smscnt+1


                # if output is not None:
                #######################################################################
                msg = client.message_create(str(source), str(i[1]), str(body))
                print(msg.__dict__)
                # print(p)
                print(msg)
                ########################################################################

     #update smssent to YES once all the sms were sent
        # for i in range(len(res)):
        # print(smscnt)
        print("update")
        updsql = "UPDATE alarms_det SET smssent='Yes'  WHERE smssent = 'No'"
        cursor.execute(updsql)
        conn.commit()


############################
#class
############################

class sms():

    while True:

        connection = psycopg2.connect(
        host="",
        database="",
        port="",
        user="",
        password="")
        maincur = connection.cursor()


        timenow = datetime.now(utc) +timedelta(hours=(+8))  #current date time
        timenow = datetime.strftime(timenow,"%H:%M:00")
        # print('current_time',current_time)
        timenow = datetime.strptime(timenow,"%H:%M:00")

        # print("Not equal")
        smstime = datetime.strptime("07:30:00","%H:%M:00")
        print(smstime)

        # if(1==1):
        if(smstime == timenow):#commented for testing
            print(timenow)
            ##########################
            cursor.execute("delete from alarms_det")
            conn.commit()
            #############################
            # maincur.execute("select id,device_id,created from alarms_alarm where sms_sent is null")
            # stations = maincur.fetchall()

            # # print((stations))

            # for q in range(len(stations)):
            #     # print(stations[q])
            #     alarmid = stations[q][0]
            #     device_id = stations[q][1]
            #     alarmcreated = stations[q][2]


            maincur.execute("select device_type,tag,status,id from devices_device ")
            query = maincur.fetchall()
            print(query)
            print(len(query))

            for l in range(len(query)):
                # try:
                if(1==1):
                    # print(l)
                    
                    device_type = query[l][0]
                    # print(device_type)
                    
                    devicetag = query[l][1]
                    print("station ",devicetag)
                    # print(devicetag)
                    status = query[l][2]
                    # print(status)
                    device_id = query[l][3]
                    # print(device_id)
                    # ####################Testing purpose##################
                    # device_id = "106"
                    # device_type = "pontoon"
                    # devicetag = "SE517"
                    # status = "online"
                    # ######################
                    maincur.execute("select max(record_time) from device_data where parameter_tag = 'Temperature' and device_tag = '"+devicetag+"'")
                    rectime = maincur.fetchall()
                    print(rectime," ",devicetag)

                    try:
                        rectime = rectime[0][0]
                        print(rectime," ",devicetag)
                        rectime = datetime.strftime(rectime,'%Y-%m-%d %H:%M:%S')

                    except:
                        rectime = None



                    if(rectime is not None):

                        # sensors = ["pH","DO_Concentration","Chlorophyll-a","Turbidity","Conductivity"]
                        # cnt = 0
                        print(device_type)
                        if device_type == "pontoon":

                            depthquery = ("select depth from depths_depth a,devices_device_depth b where a.id = b.depth_id and b.device_id = '"+str(device_id)+"'")
                            maincur.execute(query=depthquery)

                            depthslist = maincur.fetchall()

                            # print(depthslist)

                            # for z in range(len(depthslist)):
                            #     if z <= 1:
                            sensorquery = ("Select value_float from device_data where device_tag = '"+devicetag+"' and parameter_tag in('pH','Conductivity','Do_Concentration','Turbidity','Chlorophyll-a','DO_Concentration') and record_time >= '"+rectime+"' and depth= '0.5' order by parameter_tag asc")
                            # print(sensorquery)
                            maincur.execute(query=sensorquery)

                            sensordata = maincur.fetchall()
                            print(sensordata)
                            try:
                                if (len(sensordata)>6):
                                    print("fault")
                                else:

                                    pH = sensordata[3][0]
                                    dox = sensordata[2][0]
                                    cond = sensordata[1][0]
                                    tur = sensordata[4][0]
                                    chl = sensordata[0][0]

                                    # print(chl," ",cond," ",dox," ",pH," ",tur)
                            except:
                                pH = '0.0'
                                dox = '0.0'
                                cond = '0.0'
                                tur = '0.0'
                                chl = '0.0'

                                # print(chl," ",cond," ",dox," ",pH," ",tur)

                            alarm(devicetag,chl,cond,dox,pH,tur,status,rectime,len(depthslist),"pontoon")

                        elif device_type == "waterway":
                            sensorquery = ("Select value_float from device_data where device_tag = '"+devicetag+"' and parameter_tag in('pH','Conductivity','Do_Concentration','Turbidity','Chlorophyll-a','DO_Concentration') and record_time >= '"+rectime+"' order by parameter_tag asc")

                            maincur.execute(query=sensorquery)
                            sensordata = maincur.fetchall()
                            print(sensordata)
                            try:
                                if (len(sensordata)>6):
                                    print("fault")
                                else:

                                    pH = sensordata[3][0]
                                    dox = sensordata[2][0]
                                    cond = sensordata[1][0]
                                    tur = sensordata[4][0]
                                    chl = sensordata[0][0]

                                    # print(chl," ",cond," ",dox," ",pH," ",tur)
                            except:
                                pH = '0.0'
                                dox = '0.0'
                                cond = '0.0'
                                tur = '0.0'
                                chl = '0.0'

                                # print(chl," ",cond," ",dox," ",pH," ",tur)

                            alarm(devicetag,chl,cond,dox,pH,tur,status,rectime,1,"waterway")
            # except:
            #     print("error")
        connection.close()

        # time.sleep(21600)