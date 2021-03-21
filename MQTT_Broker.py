import paho.mqtt.client as paho
import paho.mqtt.client as mqtt
import random
import time
import serial

broker=""
port=1883
def on_publish(client,userdata,result):            
    print("\n data published \n")
    pass



ser = serial.Serial('COM2', 9600, timeout=1)
ser.flushInput()
while True:
    data = ser.readline()
    if (len(data)>0):
        strData = data.decode("utf-8")
        strData = strData.rstrip("\r\n")
        values = strData.split(",")

        if(len(values) == 2):
            print("",values[0])
            print("",values[1])
            
            
            client1= paho.Client("")                           
            client1.on_publish = on_publish                          
            client1.connect(broker,port)

            client2= paho.Client("")                           
            client2.on_publish = on_publish                         
            client2.connect(broker,port)


            
            ret= client1.publish("",values[0])
            
            ret= client1.publish("",values[1])
            
            