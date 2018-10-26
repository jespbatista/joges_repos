import urllib.request
import  re
import json
from sys import argv

def  open_url(url, token):
	Cookies={'Cookie':token}
	Request=urllib.request.Request(url=url,headers=Cookies)
	response=urllib.request.urlopen(Request,timeout=100)
	return  response.read().decode("utf-8")

lines = json.loads(open_url("https://git.ulisboa.pt/api/v4/projects?simple=true&per_page=500&scope=workflow", "_gitlab_session="+argv[1]))

out = open("joget_repos","w")

for project in lines:
	if "workflow" in project["http_url_to_repo"] :
		out.write(project["http_url_to_repo"] + "\n")

out.close()