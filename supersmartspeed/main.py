#!/usr/bin/env python3
import speedtest
from influxdb import InfluxDBClient
import schedule 
import time 

def job():
# influx configuration - edit these
  ifuser = "grafana"
  ifpass = "28Kgum&zkTY"
  ifdb   = "home_v2"
  ifhost = "localhost"
  ifport = 8086
  measurement_name = "speedtest"

# take a timestamp for this measurement
  time = datetime.datetime.utcnow()

  speedtester = speedtest.Speedtest()
  speedtester.get_best_server()
  speedtester.download()
  speedtester.upload()
  res = speedtester.results.dict()
  print(res["download"], res["upload"], res["ping"])
# format the data as a single measurement for influx
  body = [
      {
          "measurement": measurement_name,
          "time": time,
          "fields": {
              "download": res["download"],
              "upload": res["upload"],
              "ping": res["ping"]
          }
      }
  ]

# connect to influx
  ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

# write the measurement
  ifclient.write_points(body)

schedule.every(30).seconds.do(job)
#schedule.every(5).minutes.do(job)
while True: 
  schedule.run_pending()
  time.sleep(1)

client = InfluxDBClient(host='localhost', port=8086, username='grafana', password='28Kgum&zkTY', database='home')

result3 = client.query("select last(download) from speedtest")

points = result3.get_points()
for item in points:
    print(item['last'])
data = item['last']


if data <= 300:
  def function(): 
    speedtester = speedtest.Speedtest()
    speedtester.get_best_server()
    speedtester.download()
    speedtester.upload()
    res = speedtester.results.dict()
    #print(res["download"], res["upload"], res["ping"])
  function()
else:
  print("your speed is okay")

