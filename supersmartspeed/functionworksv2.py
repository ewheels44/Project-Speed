#!/usr/bin/env python3
import speedtest
import schedule 
import time 

#runs every 5 min
def function(): 
  speedtester = speedtest.Speedtest()
  speedtester.get_best_server()
  speedtester.download()
  speedtester.upload()
  res = speedtester.results.dict()
  print(res["download"], res["upload"], res["ping"])
function()

#get data from last query 
#testing purposed I set data

data = 685494472.5316864/1000000

if data <= 800:
  def speed(): 
    speedtester = speedtest.Speedtest()
    speedtester.get_best_server()
    speedtester.download()
    speedtester.upload()
    res = speedtester.results.dict()
    print(res["download"], res["upload"], res["ping"])
  speed()
else:
  print("your speed is okay")