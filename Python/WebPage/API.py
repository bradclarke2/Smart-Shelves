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

            #insertDB.printShelfDB()
            prioritisedFillList = stockpercentages.calculateFillListOrder(ShelfList, ProductList)
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
                
            a = a[-12:]
            numberOfGaps= 0
            for b in a:
                if float(b) < 0.1:
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
    
    class stock_graph(Resource):
        def get(self):
            
            db = sqlite3.connect(CreateDB.dbName)
            cursor = db.cursor()
            
            cursor.execute('''SELECT id, shelfLocation, TPNB, unitsOfStock, percentageFull, timestamp, stockgraph, priorityscore FROM shelfGridTable''')
            all_rows = cursor.fetchall()
            a = []
            
            for row in all_rows:
                a.append([row[1], row[2]])
                              
            a = a[-12:]
            c=[]
            
            for shelfLocation in a:
                c.append(["img/StockHistory-" + shelfLocation[0] + ".png", shelfLocation[1], shelfLocation[0]])
            
            return c

    api.add_resource(list_priority, '/list/')
    api.add_resource(gap_scan, '/gap/')
    api.add_resource(photo_resistor, '/pr/')
    api.add_resource(stock_graph, '/stock/')
    
    app.run()