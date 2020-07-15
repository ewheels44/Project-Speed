#!/usr/bin/env python3
import speedtest
import schedule 
import time 

def function(): 
  speedtester = speedtest.Speedtest()
  speedtester.get_best_server()
  speedtester.download()
  speedtester.upload()
  res = speedtester.results.dict()
  print(res["download"], res["upload"], res["ping"])
  data = res['download']
  print(data)
function()

