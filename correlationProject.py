import csv
import plotly.express as px
import numpy as np

def getSourceOfDataAndShowChart(data_path):
    daysPresent = []
    marks = []

    with open(data_path) as file1:
        df = csv.DictReader(file1)
        for row in df:
            daysPresent.append(float(row['Days-Present']))
            marks.append(float(row['Marks']))
        
        return {'x':daysPresent,'y':marks}
        
def figureShow():
    with open('Student Marks vs Days Present.csv') as file1:
        df = csv.DictReader(file1)
        figure = px.scatter(df,x='Days-Present',y='Marks')
        figure.show()


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print('Correlation between Days Present and Marks is ',correlation[0,1])

def setup():
    data_path = 'Student Marks vs Days Present.csv'
    data_source = getSourceOfDataAndShowChart(data_path)
    findCorrelation(data_source)
    figureShow(x)

setup()
