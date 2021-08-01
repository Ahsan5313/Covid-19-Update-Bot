import requests
import json
from win10toast import ToastNotifier
import time


response = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
data = response.json()
confimed_case = data[26]['country']
cases = data[26]['cases']
deaths = data[26]['deaths']
todayCase = data[26]['todayCases']
todayDeath = data[26]['todayDeaths']
recoved = data[26]['recovered']
text = f"Confimed : {confimed_case} \n Totall : {cases} \n Deaths : {deaths} \n TodayCase : {todayCase} \n TodayDeath : {todayDeath} \n  Reccover : {recoved}"


toast = ToastNotifier()
toast.show_toast('Covid-19 in Bangladesh', text, duration=15)
time.sleep(8)
print(text)
