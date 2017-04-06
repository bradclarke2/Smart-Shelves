import json
import http.client, urllib.request, urllib.parse, urllib.error, base64

class Product (object): 
    def __init__(self,name, tpnb, height, width, depth, weight):
        self.name = name
        self.tpnb = tpnb
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight

def makeProductGrid():     
    MadeList = []
    MadeList.append(Product("Quaker Oats", "5000108810988", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Pancake Mix", "5449000958938", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Cat Food", "8410136002885", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Water 500ml", "5060108450324", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Caviar", "5701263907864", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Dino Prosecco", "5053947211041", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Stawberry Jam", "5000119002501", 21.0, 13.0, 8.0, 0.293))
    MadeList.append(Product("Peanuts 200g", "5052109944841", 21.0, 13.0, 8.0, 0.293))
    #MadeList.append(Product("Kellogs Cornflakes", "050060399", 30, 23, 8, 0.450))
    
    for a in MadeList:
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '3ccfc504045b4d9f8f592e8590b1c757',
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
     
        print("product dimension are", a.height )
    return MadeList