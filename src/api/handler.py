from bs4 import BeautifulSoup
import requests
import time

country = "World"
notification_duration = 10
refresh_time = 10 #minutes
data_check= []
worldmetersLink = "https://www.worldometers.info/coronavirus/"

def get_stats(array):
    L = []
    for i in array:
        i = i.replace("+","")
        i = i.replace("-","")
        i = i.replace(",",".")
        if i == "":
            i = "0"
        L.append(i.strip())
    return L
html_page = requests.get(worldmetersLink)
bs = BeautifulSoup(html_page.content, 'html.parser')

search = bs.select("div tbody tr td")
start = -1
for i in range(len(search)):
    if search[i].get_text().find(country) !=-1:
        start = i
        break
data = []
for i in range(1,8):
    try:
        data = data + [search[start+i].get_text()]
    except:
        data = data + ["0"]
    
data= data_cleanup(data)
message = "Total infected = {}, New Case = {}, Total Deaths = {}, New Deaths = {}, Recovred = {}, Active Case = {}, Serious Critical = {}".format(*data)
print(message)

