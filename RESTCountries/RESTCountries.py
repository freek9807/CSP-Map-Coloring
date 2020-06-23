import requests
import json

class RESTCountries():

    url = "https://restcountries.eu/rest/v2/all"

    def __init__(self):
        r = requests.get(self.url)
        nations = r.json()
        self.code2name = {}
        self.adjMatrix = {}

        for nation in nations:
            self.adjMatrix[nation['alpha3Code']] = nation['borders']
            self.code2name[nation['alpha3Code']] = nation['alpha2Code']

        self.adjMatrix['KWT'].append('IRQ')
        self.adjMatrix['ALA'].append('FIN')
        self.adjMatrix['ATA'].append('ARG')
        self.adjMatrix['AUS'].extend(['PNG','IDN','NZL'])
        self.adjMatrix['CUB'].extend(['USA','MEX'])
        self.adjMatrix['GRL'].extend(['CAN','GBR','ISL','SJM'])
        self.adjMatrix['ISL'].extend(['GRL','GBR','NOR','SJM','CAN'])
        self.adjMatrix['JPN'].extend(['CHN','RUS','PRK','KOR'])
        self.adjMatrix['MDG'].extend(['MOZ','ZAF'])
        self.adjMatrix['NCL'].extend(['AUS','NZL'])
        self.adjMatrix['NZL'].extend(['AUS','NCL'])
        self.adjMatrix['PHL'].extend(['IDN','VNM','PNG'])
        self.adjMatrix['PRI'].extend(['DOM','VEN'])
        self.adjMatrix['SLB'].extend(['PNG','AUS','NZL'])
        self.adjMatrix['SJM'].extend(['NOR','GRL','ISL'])
        self.adjMatrix['TWN'].extend(['CHN','PHL','JPN','VNM'])
        self.adjMatrix['MYS'].extend(['PHL'])
        self.adjMatrix['TTO'].extend(['VEN','GUY'])

        for (key,val) in self.adjMatrix.items():
            for neir in val:
                if key not in self.adjMatrix[neir]:
                    self.adjMatrix[neir].append(key)

    def getAdjMatrix(self):
        return self.adjMatrix

    def getCode2name(self):
        return self.code2name