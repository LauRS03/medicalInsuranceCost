from asyncio.windows_events import NULL
from tkinter import E
import data.database as db

class insuranceservice():
    
    def inscost():
      va=db.DataManager.getDataExcel()
      ecost=[]
      reg=[]
      rest=[]
      for per in va:
          sexx=[]
          smok=[]
          if per.sex== "female":
              sexx.append(0)
          else:
              sexx.append(1)
          if per.smoker== "no":
              smok.append(0)
          else:
              smok.append(1)

          estimated_cost=250 * per.age-128*sexx[-1]+370*per.bmi+425*per.children+24000*smok[-1]-12500
          ecost.append(estimated_cost)
          reg.append(per.region)
      rest.append(ecost)
      rest.append(reg)
      myDic = {}  
      count = 0
      for i in reg:
          if myDic.get(i) != None:
              newValue = {i:myDic.get(i) + ecost[count]}
              myDic.update(newValue)
          else:
              newValue = {i:ecost[count]}
              myDic.update(newValue)
          count +=1

     
      return myDic