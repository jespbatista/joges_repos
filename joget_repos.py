import urllib.request
import  re
from sys import argv

def  open_url(url, token):
	Cookies={'Cookie':token}
	Request=urllib.request.Request(url=url,headers=Cookies)
	response=urllib.request.urlopen(Request,timeout=100)
	return  response.read().decode("utf-8")

lines = open_url("https://git.ulisboa.pt/api/v4/projects?simple=true&per_page=50&scope=workflow", "_gitlab_session="+argv[1]).split("\n")
lines = lines[0].split('"id":')
lines.pop(0)

out = open("joget_repos","w")

for line in lines:
	if "workflow" in line:
		line = line.split('http_url_to_repo":"')[1]
		line = line.split('","')[0]
		out.write(line + "\n")
out.close()