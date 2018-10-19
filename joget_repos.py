import urllib.request
import  re
from sys import argv

def  open_url(url, token):
	Cookies={'Cookie':token}
	Request=urllib.request.Request(url=url,headers=Cookies)
	response=urllib.request.urlopen(Request,timeout=100)
	return  response.read().decode("utf-8")

lines = open_url("https://git.ulisboa.pt", argv[1]).split("\n")


out = open("joget_repos","w")
directory = ""
project = ""
a = 0
for line in lines:
	if a == 1:
		a = 0
		directory = line.strip().replace(" ","")
	if "namespace-name" in line:
		a = 1
	if "project-name" in line:
		project = line.split('name">')[1].split("<")[0]
		out.write("https://git.ulisboa.pt/" + directory + "/" +project + ".git\n")
out.close()