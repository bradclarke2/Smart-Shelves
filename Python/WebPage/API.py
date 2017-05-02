import Objects.XYGrid as XYGridObject
import Objects.shelf as ShelfObject
import Calculations.stockPercentage as stockpercentages
import Measurements.MeasureUS as measureUS
import Graphing.Heatmap as heatmap
import Objects.product as ProductObject
import InsertDB as insertDB
import sqlite3
import CreateDB
from Measurements.MeasureUS import MeasureDistancePR
import threading
import multiprocessing as mp
from Calculations import stockPercentage


def makingGraphs(singleshelf, XYGridList):                    
    heatmap.MakeHeatMap(singleshelf, XYGridList)                           
    insertDB.insertShelfRecord(singleshelf)
    heatmap.MakeSalesGraph(singleshelf)

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
                stockPercentage.MeasureUSCovered(singleshelf, XYGridList)
                stockPercentage.MeasurePRCovered(singleshelf, XYGridList)
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
                makingGraphs(singleshelf, XYGridList)
                putOnCore = mp.Process(target = makingGraphs, args = (singleshelf, XYGridList))
                putOnCore.start()
                
            prioritisedFillList = stockpercentages.calculateFillListOrder(ShelfList, ProductList)
            return prioritisedFillList
    
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
            ShelfList = ShelfObject.makeShelfGrid()
            a = []            
            for shelf in ShelfList:
                db = sqlite3.connect(CreateDB.dbName)
                cursor = db.cursor()
                cursor.execute('''SELECT stockgraph, tpnb, shelfLocation, max(timestamp) FROM shelfHistoricSales WHERE shelfLocation = (?)''', (shelf.location,))
                all_rows = cursor.fetchall()
                print(all_rows)
                print(type(all_rows))
                a.append(all_rows)
            print(a)
            my_list = [l[0] for l in a]
            return my_list
        
    class box_scan(Resource):
        def get(self):
            db = sqlite3.connect(CreateDB.dbName)
            cursor = db.cursor() 
            cursor.execute('''SELECT shelfLocation, USpointscovered, PRpointscovered FROM shelfGridTable''')
            all_rows = cursor.fetchall()
            count = 0
            ShelfsWithEmptyBox = 0
            
            USGridPoints = []
            PRGridPoints = []
            for row in all_rows:
                USGridPoints.append(row[1])
                PRGridPoints.append(row[2])
                count = count + 1
            print("all=",all_rows)    
            print("initUS=",USGridPoints)
            print("initpr=",PRGridPoints)
                
            USGridPoints = USGridPoints[-1:]
            PRGridPoints = PRGridPoints[-1:]
            
            print("all=",all_rows)    
            print("initUS=",USGridPoints)
            print("initpr=",PRGridPoints)
        
            if USGridPoints[0] > PRGridPoints[0]:
                ShelfsWithEmptyBox = ShelfsWithEmptyBox + 1
                
            return ShelfsWithEmptyBox      

#             EmptyBoxShelves = 0
#             for singleshelf in ShelfList:
#                 for b in XYGridList:
#                     if b.shelflocation == singleshelf.location:
#                         c = stockpercentages.CalculateEmptyBoxes(singleshelf.height, b.USdistance, b.PRCovered)
#                         if c == 1:
#                             EmptyBoxGridPoints = EmptyBoxGridPoints + 1
#                 if EmptyBoxGridPoints > 0:
#                     EmptyBoxShelves = EmptyBoxShelves + 1
#             return EmptyBoxShelves 
        
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
            a = a[-1:]
            numberOfGaps= 0
            for b in a:
                if float(b) < 0.1:
                    numberOfGaps = numberOfGaps + 1
            return numberOfGaps      

    api.add_resource(list_priority, '/list/')
    api.add_resource(gap_scan, '/gap/')
    api.add_resource(photo_resistor, '/pr/')
    api.add_resource(stock_graph, '/stock/')
    api.add_resource(box_scan, '/box/')
    app.run()