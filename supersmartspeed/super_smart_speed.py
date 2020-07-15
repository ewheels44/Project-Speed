#!/usr/bin/env python3
import speedtest
from influxdb import InfluxDBClient
import schedule 
import time 
import datetime 

def t():
  print("happy fathers day")
  if datetime.datetime.now().minute % 5 == 0:
    print("happy day dad")
    #connect and write to influxdb
  else:
    print("your so cool dad")
    
    d = 1 
    if d <= 300:
      def speed():
        print("hello again")
      speed()
        #connect and write to influxdb
schedule.every(1).minutes.do(t)
while True:
    schedule.run_pending()
    time.sleep(1)