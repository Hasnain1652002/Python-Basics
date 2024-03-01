from email import header
from bs4 import BeautifulSoup
import requests
import re

url = "https://pk.indeed.com/jobs-in-Karachi"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","Referer": "https://www.indeed.com/"}
r = requests.get(url, headers= headers)

print(r.status_code)
doc = BeautifulSoup(r.text, 'html.parser')

jobs = doc.find("ul", {"class":"jobsearch-ResultsList"}).find_all("li")
for count,job in enumerate(jobs,start=1):
    try:
        header = job.find("h2").text
    except:
        header = ""

    try:
        Salary= job.find("svg",{"aria-label":"Salary"}).parent.text.strip()
    except:
        Salary = ""

    print(count, header)
    print(f"Salary : {Salary}")
    print("----------------")
    