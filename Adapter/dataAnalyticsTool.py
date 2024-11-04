class DataAnalyticsTool:
    def __init__(self,jsonData) -> None:
        self.jsonData = jsonData
    def analyseData(self):
        print('Processed Data is '+self.jsonData)
    