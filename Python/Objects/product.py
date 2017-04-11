import json
import http.client, urllib.request, urllib.parse, urllib.error, base64
from configparser import SafeConfigParser
from mysite.personal import test2 as key

APIkey = key.api

class Product (object): 
    def __init__(self,name, tpnb, height, width, depth, weight, priority):
        self.name = name
        self.tpnb = tpnb
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.priority = priority
        
def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


def makeProductGrid():     
    MadeList = []
    MadeList.append(Product("T. British Semi Skimmed Mlk2.272Ltr 4 Pints", "5053827141529", 21.0, 13.0, 8.0, 0.293, 9))
    MadeList.append(Product("T. Free Range Medium 12 Shipper Eggs", "5051140150471", 21.0, 13.0, 8.0, 0.293, 9))
    MadeList.append(Product("Hovis Soft White Medium Bread 800G", "5010003000131", 21.0, 13.0, 8.0, 0.293, 9))
    MadeList.append(Product("Tesco British Mature Cheddar 450G", "5053526716035", 21.0, 13.0, 8.0, 0.293, 6))
    MadeList.append(Product("Tesco Ripe Bananas 5 Pack", "0000010001875", 21.0, 13.0, 8.0, 0.293, 6))
    MadeList.append(Product("Dino Prosecco", "5053947211041", 21.0, 13.0, 8.0, 0.293, 5))
    MadeList.append(Product("Tesco Low Fat Greek Style Yogurt 500G", "5000462416734", 21.0, 13.0, 8.0, 0.293, 5))
    MadeList.append(Product("Bisto Favourite Gravy Granules 170G", "5010024101381", 21.0, 13.0, 8.0, 0.293, 3))
    MadeList.append(Product("Haribo Starmix 215G", "5012035936631", 30, 23, 8, 0.450, 3))
    MadeList.append(Product("T. Eday Value Milk Choc Dgstvebiscuits 300G", "5010204427379", 30, 23, 8, 0.450, 3))
    MadeList.append(Product("Colgate Advancedwhite Toothpaste100ml", "5000209114510", 30, 23, 8, 0.450, 1))
    MadeList.append(Product("Tesco Shower Cleaner Spray 500Ml", "5000436725589", 30, 23, 8, 0.450, 1))
    
#     parser = SafeConfigParser()
#     parser.read('keys.ini')
    APIkey = key.api

    for a in MadeList:
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': APIkey,
        }
        gtin = a.tpnb
        params = urllib.parse.urlencode({
            # Request parameters
            'gtin': gtin,
        })
         
        conn = http.client.HTTPSConnection('dev.tescolabs.com')
        conn.request("GET", "/product/?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        parsed_data = json.loads(data)
        a.height = parsed_data['products'][0]['pkgDimensions'][0]['height']
        a.width = parsed_data['products'][0]['pkgDimensions'][0]['width']
        a.depth = parsed_data['products'][0]['pkgDimensions'][0]['depth']
        a.weight = parsed_data['products'][0]['pkgDimensions'][0]['weight']
     
    return MadeList