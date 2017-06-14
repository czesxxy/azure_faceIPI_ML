import httplib, urllib, base64, json

#create person group

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'a7f1241ed0b34a91a420a16d56dde6c3'
}

'''
body = {
    "name":"soa",
    "userData":"user-provided data attached to the person group"
}

try:
    print 'aa'
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    print 'bb'
    conn.request("PUT", "/face/v1.0/persongroups/2", json.dumps(body), headers)
    print 'sent'
    response = conn.getresponse()
    print response
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print e
'''

def createPerson(name):

    body = {
        "name":name,
        "userData":"User-provided data attached to the person"
    }
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/2/persons", json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        data = json.loads(data)
        conn.close()
        return data['personId']
    except Exception as e:
        print e

def addFace(personId):
    print "add a person: "
    print personId
    body = {
        "url":"image/" + str(personId) + ".png"
    }
    try:
        body['url'] = 'http://183.172.137.163/image/' + personId ;
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/2/persons/%s/persistedFaces?"%personId, json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print e

def trainGroup():
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/2/train", '' , headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print e

def detectFace():
    body = {"url":'http://183.172.137.163/image/tmp'}
    params = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false'
    })
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        data = eval(data)
        conn.close()
        return data[0]['faceId']
    except Exception as e:
        print e

def checkFace():
    faceId = detectFace()
    body = {
        "faceIds":[faceId],
        "personGroupId":'2',
        "maxNumOfCandidatesReturned":1,
        "confidenceThreshold":0.4
    }

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/identify", json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        data = eval(data)
        if len(data[0]['candidates']) == 0:
            return None
        personId = data[0]['candidates'][0]['personId']
        print "find person Id :"
        print personId
        conn.close()
    except Exception as e:
        print e
    return getPersonName(personId)

def getPersonName(personId):
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("GET", "/face/v1.0/persongroups/2/persons/%s"%personId, '', headers)
        response = conn.getresponse()
        data = response.read()
        data = eval(data)
        print data
        name = data['name']
        print(name)
        conn.close()
        return name
    except Exception as e:
        print e
        return ''

