#!/usr/bin/env python3
import speedtest
from influxdb import InfluxDBClient
import schedule 
import time

def t():
  def speed():
    print("I am working!")
  schedule.every(15).seconds.do(speed)
schedule.every(10).seconds.do(t)
while True:
    schedule.run_pending()
    time.sleep(30)


