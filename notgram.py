from lib import http_request
from bs4 import BeautifulSoup
import json
import re
import subprocess
import os
import time

def main():
    f = open("list_content.txt", "r+")
    f2 = open("list_title.txt", "r+")
    list_title =json.loads(f2.read())
    list_content = json.loads(f.read())
    f.seek(0)
    f2.seek(0)
    url = "http://securityaffairs.co/"
    content = BeautifulSoup(http_request.html_get(url), 'html.parser')
    links = content.select('h3 > a')
    for link in links:
        title = re.sub(r'<.*?>', "", str(link))
        if link['href'] not in list_content:
            print("New Judul: {} Url: {}".format(title, link['href']))
            list_title.insert(0, title)
            list_content.insert(0,link['href'])
            time.sleep(5)
            proc = subprocess.Popen(["bash", "telegram.sh"], stdout=subprocess.PIPE)
            (out, err) = proc.communicate()

    f.write(json.dumps(list_content))
    f2.write(json.dumps(list_title))
    f.truncate()
    f2.truncate()
    

if __name__ == '__main__':
    main()
