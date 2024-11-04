from client import Client
from dataAnalyticsTool import DataAnalyticsTool
from xmlData import XmlData
from adapter import Adapter

xmlData = XmlData('This is xml Data')
dataAnalysisTool = Adapter(xmlData)
client = Client()
client.processData(dataAnalysisTool)