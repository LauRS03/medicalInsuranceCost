import logic.insuranceservice as ics
import matplotlib.pyplot as mplot
class plotc:
    def plotfun():   
     xaxis= ics.insuranceservice.inscost().keys()
     yaxis= ics.insuranceservice.inscost().values()
     mplot.plot(xaxis,yaxis)
     mplot.show()
