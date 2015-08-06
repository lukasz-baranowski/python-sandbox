__author__ = 'lucek'

import urllib2
import json
import requests


url = "http://live-planettgv-cpp-r2.service.eu-west-1.maps-test.amiefarm.com/monitor;csv;norefresh"
qasup = "http://qasup-planettgv-cpp-r2.service.eu-west-1.maps-test.amiefarm.com"
branch = "0565c155-0318-4f88-ac06-64cf0c8f5753"

def main():
    # getFromProxy()
    #registerYardTag()
    registerYardTag2()
    getYardTag()

def registerYardTag():
    r = requests.put(qasup + '/ap-mediator-ws/branchids/' + branch + '/types/YARD_TAGs/tag', "1ST_CPP_TAG_EVER_666_3")
    print(r)
    print(r.content)

    if r.status_code == 200:
        print("ok")
    else:
        resp = json.loads(r.content)
        print(resp['message'])
        print(resp['status'])

def registerYardTag2():
    print("Urllib2 second try")
    try:
        req = urllib2.Request(qasup + '/ap-mediator-ws/branchids/' + branch + '/types/YARD_TAG/tag')
        req.add_header('Content-Type', 'application/json; charset=UTF-8')
        req.get_method = lambda: 'PUT'
        response = urllib2.urlopen(req, 'lucifer_666')
        if response.code == 200:
            print(response.msg)
    except Exception, e:
        print("Failed to create tag with status: " + str(e.code) + ", message: " + e.msg)


def getYardTag():
    print("Getting YARD_TAG...")
    yard_tag_url = qasup + "/ap-mediator-ws/branchids/" + branch + "/types/YARD_TAG/tag"
    response = urllib2.urlopen(yard_tag_url, timeout=1)
    result = str(response.read())
    print(result)


def getFromProxy():
    print('check if services under ' + url + ' are available')
    services_available = False
    # while not services_available:
    #    try:
    response = urllib2.urlopen(url, timeout=1)
    result = str(response.read())
    print(result)
    result = result.splitlines()
    result.pop(0)
    result.pop(0)
    hosts = map(lambda x: x.split(",")[0], result)
    print(hosts)
    print(url.replace("live-", "qasup-"))


if __name__ == '__main__':
    main()
