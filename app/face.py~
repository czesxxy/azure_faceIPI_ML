import httplib, urllib, base64, json

#create person group

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'b5305d275700491eb82c5ff82573eab4'
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
    conn.request("PUT", "/face/v1.0/persongroups/1", json.dumps(body), headers)
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
        conn.request("POST", "/face/v1.0/persongroups/1/persons", json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        data = json.loads(data)
        conn.close()
        print data['personId']
        return data['personId']
    except Exception as e:
        print e

def addFace(personId):
    print personId
    body = {
        "url":"image/" + str(personId) + ".png"
    }
    try:
        body['url'] = 'http://img1.gtimg.com/ent/pics/hv1/217/14/1910/124201537.png'
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/1/persons/%s/persistedFaces?"%personId, json.dumps(body), headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print e

def trainGroup():
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/persongroups/1/train", '' , headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print e

def detectFace():
    body = {"url":"image/tmp.png"}
    body = {"url":'http://img1.gtimg.com/ent/pics/hv1/217/14/1910/124201537.png'}
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
        print(data[0]['faceId'])
        conn.close()
        return data[0]['faceId']
    except Exception as e:
        print e

def checkFace():
    faceId = detectFace()
    body = {
        "faceIds":[faceId],
        "personGroupId":'1',
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
        print personId
        conn.close()
    except Exception as e:
        print e
    return getPersonName(personId)

def getPersonName(personId):
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("GET", "/face/v1.0/persongroups/1/persons/%s"%personId, '', headers)
        response = conn.getresponse()
        data = response.read()
        data = eval(data)
        name = data['name']
        print(name)
        conn.close()
    except Exception as e:
        print e

    return name

