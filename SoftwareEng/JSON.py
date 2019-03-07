import requests
import json
import matplotlib.pyplot as plt
import csv

r = requests.get('https://api.iextrading.com/1.0/stock/aapl/chart/ytd')
#print(r.json())
stock_data = json.loads(r.text)

currentYear = "2018"
values = []
time = []
i = 0
for x in stock_data:
        time.append(stock_data[i]["date"])
        values.append(stock_data[i]["close"])
        i=i+1
i=0
#print(time)
#print(len(time))
#print(values)
#print(len(values))

with open('ytd_aapl.csv','w') as newfile:
        file = csv.writer(newfile)
        for val in values:
                file.writerow([time[i],str(val)])
                i=i+1
    




