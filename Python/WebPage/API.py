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
from Measurements.MeasureUS import MeasureDistancePR

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
            for singleshelf  in ShelfList:
                measureUS.MeasureDistanceUS(singleshelf, XYGridList) 
                measureUS.MeasureDistancePR(singleshelf, XYGridList)
                a = []
                for b in XYGridList:
                    if b.shelflocation == singleshelf.location:
                        c = stockpercentages.CalculateConfidence(singleshelf.height, b.USdistance, b.PRCovered)
                        a.append(c)
                print("value of a is", a)
                if -1 in a:
                    singleshelf.confidenceLevel = -1
                else:
                    singleshelf.confidenceLevel = 1
                   
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
                    
            return numberOfGaps                
    
    class photo_resistor(Resource):
        def get(self):
            ProductList = ProductObject.makeProductGrid()
            XYGridList = XYGridObject.MakeXYGrid()
            ShelfList = ShelfObject.makeShelfGrid()
            a =[]
            for singleshelf in ShelfList:
                MeasureDistancePR(singleshelf, XYGridList)
                
            for b in XYGridList:
                a.append((int(b.PRCovered), stockpercentages.PRFullness(int(b.PRCovered))))
            return a
             
    api.add_resource(Departmental_Salary, '/measurements/')
    api.add_resource(list_priority, '/list/')
    api.add_resource(gap_scan, '/gap/')
    api.add_resource(photo_resistor, '/pr/')
    
    app.run()