import csv
import models.person as p

class DataManager:

    def getDataExcel():
        data=[]
        with open('insurance.csv') as csvfile:
            tdatar= csv.reader(csvfile)
            for row in tdatar:
                data.append(p.Person(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    
        
        return data

    