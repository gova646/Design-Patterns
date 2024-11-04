from dataAnalyticsTool import DataAnalyticsTool

class Adapter(DataAnalyticsTool):
    def __init__(self, xmlData) -> None:
        self.xmlData = xmlData
    def analyseData(self):
        print('converting xml Data into json' + self.xmlData.getXmlData())
        print('analysing json Data')