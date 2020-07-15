#!/usr/bin/env python3
import speedtest
from influxdb import InfluxDBClient
import schedule 
import time 
import datetime 

def t():
  client = InfluxDBClient(host='localhost', port=8086, username='grafana', password='28Kgum&zkTY', database='home')
  measurement_name = "speedtest"
  if datetime.datetime.now().minute % 5 == 0:
    # take a timestamp for this measurement
    time = datetime.datetime.utcnow()

    speedtester = speedtest.Speedtest()
    speedtester.get_best_server()
    speedtester.download()
    speedtester.upload()
    res = speedtester.results.dict()
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

  else:
    result3 = client.query("select last(download) from speedtest")

    points = result3.get_points()
    for item in points:
        data = item['last']
    data1 = data/1000000

    if data1 <= 300:
      def speed():
        # take a timestamp for this measurement
        time = datetime.datetime.utcnow()
        
        speedtester = speedtest.Speedtest()
        speedtester.get_best_server()
        speedtester.download()
        speedtester.upload()
        res = speedtester.results.dict()
        #connect and write to influxdb
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
      speed()
schedule.every(1).minutes.do(t)
while True:
    schedule.run_pending()
    time.sleep(1)

    
