import Objects.XYGrid as XYGridObject
import Objects.shelf as ShelfObject
import Calculations.stockPercentage as stockpercentages
import Measurements.MeasureUS as measureUS
import Graphing.Heatmap as heatmap
import Objects.product as ProductObject
import InsertDB as insertDB
import sqlite3
import CreateDB
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

def startfunction():
    from flask import Flask
    from flask_restful import Resource, Api
    app = Flask(__name__)
    api = Api(app)
    
    class Departmental_Salary(Resource):
        def get(self):
            ProductList = ProductObject.makeProductGrid()
            XYGridList = XYGridObject.MakeXYGrid()
            ShelfList = ShelfObject.makeShelfGrid()
            for singleshelf in ShelfList:
                measureUS.MeasureDistance(singleshelf, XYGridList) 
                stockpercentages.UnitsToFill(singleshelf, ProductList, XYGridList)
                heatmap.MakeHeatMap(singleshelf.height, XYGridList, singleshelf.location)
            print("XYGrid=")
            for XYGrid in XYGridList:
                print(XYGrid.shelflocation,",",XYGrid.idpos,",",XYGrid.xpos,",",XYGrid.ypos,",",XYGrid.distance)
            print("ShelfGrid=")
            for Shelf in ShelfList:
                print(Shelf.location,",",Shelf.height,",",Shelf.width,",",Shelf.depth,",",Shelf.volumePercentFull,",", Shelf.areaFull,",",Shelf.unitsOfSpace)
            return singleshelf.unitsOfSpace
                 
    class list_priority(Resource):
        def get(self):
            ProductList = ProductObject.makeProductGrid()
            XYGridList = XYGridObject.MakeXYGrid()
            ShelfList = ShelfObject.makeShelfGrid()
            for singleshelf in ShelfList:
                measureUS.MeasureDistanceUS(singleshelf, XYGridList) 
                #measureUS.MeasureDistancePR(singleshelf, XYGridList)
                
                #stockpercentages.CalculateConfidence(singleshelf.height, measurementCM, lumens)    
                   
                stockpercentages.UnitsToFill(singleshelf, ProductList, XYGridList)      
                print(singleshelf.location, "is", singleshelf.volumePercentFull*100, "% full and can fit", singleshelf.unitsOfSpace, "more units of X")
                
                heatmap.MakeHeatMap(singleshelf, XYGridList)           
                   
                insertDB.insertShelfRecord(singleshelf)
                heatmap.MakeSalesGraph(singleshelf)
            insertDB.printShelfDB()
            prioritisedFillList = stockpercentages.calculateFillListOrder(ShelfList)
            return prioritisedFillList
        
    class gap_scan(Resource):
        def get(self):
            db = sqlite3.connect(CreateDB.dbName)
            cursor = db.cursor()
            
            cursor.execute('''SELECT id, shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp FROM shelfGridTable''')
            all_rows = cursor.fetchall()
            count = 0
            a = []
            for row in all_rows:
                if count > (cursor.rowcount-7):
                    a.append('{0}'.format(row[4])) 
                count = count + 1
                
            a = a[-7:]
            numberOfGaps= 0
            for b in a:
                if float(b) < 0.65:
                    numberOfGaps = numberOfGaps + 1
                    
#             return numberOfGaps
            pkgarray =[]
            headers = {
        # Request headers
            'Ocp-Apim-Subscription-Key': '3ccfc504045b4d9f8f592e8590b1c757',
            }
            gtin = 5052109944841
            params = urllib.parse.urlencode({
                # Request parameters
                'gtin': gtin,
            })
            
            conn = http.client.HTTPSConnection('dev.tescolabs.com')
            conn.request("GET", "/product/?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
            parsed_data = json.loads(data)
            description = parsed_data['products'][0]['pkgDimensions'][0]['height']
            pkgarray.append(description)
            
            return pkgarray
                
         
    api.add_resource(Departmental_Salary, '/measurements/')
    api.add_resource(list_priority, '/list/')
    api.add_resource(gap_scan, '/gap/')
    
    app.run()