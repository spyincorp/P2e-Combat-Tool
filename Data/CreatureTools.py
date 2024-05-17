import csv
import random
import pandas as pd

from BlockReader import dataframe_to_csv, beastiary_to_dataframe

def print_title_card(instance):
    name = instance.__class__.__name__ 
    print('\033[92m' + f'====================={name}=====================' + '\033[0m \n')

class creature:
    def __init__(self, cr=0, type=None,  min=None, max=None, name =''):
        self.cr = cr
        self.type = type
        self.min = min
        self.max = max
        self.name = name
    def updatebeastiary():
        dataframe_to_csv()
      
    def getRandomMonster(self):
        print_title_card(self)
        if self.min is None or self.max is None:
            raise ValueError("Minimum and maximum levels must be provided.")
                   
        else:
            df = pd.read_csv('Data\BeastiaryCsv\Beastiary.csv')
            mask = (df['Level'] >= self.min) & (df['Level'] <= self.max)
            rangedf =df[mask]
            rc =rangedf.sample(n=1)
            out2 = rc[['Name','Level']].to_string(index=False)

            print(out2 + '\n')

    def getByTrait(self):
        df = pd.read_csv('Data\BeastiaryCsv\Beastiary.csv')
        mask = df['Traits'].apply(lambda x: f'{self.type}' in x)
        traitsdf =df[mask]
        return(traitsdf)

    def __getByNameDf(self):
        df = pd.read_csv('Data\BeastiaryCsv\Beastiary.csv')
        mask =df['Name'].str.contains(self.name, case=False)
        namedf = df[mask]
        out = namedf[['Name','Level']].to_string(index=False)
        return(namedf)
    
    def getByName(self):
        print_title_card(self)
        namedf = self.__getByNameDf()
        out = namedf[['Name','Level']].to_string(index=False)
        print(out)

    def getNPC(self):
        pass

    def getRandomNPC(self):
        pass

class npc(creature):
    def __init__(self, cr=0, type='',  min=None, max=None, name =''):
        super().__init__(cr, type,  min, max, name)

    def getNPC(self):
        self.type = 'humanoid'
        npcs = self.getByTrait()
        return(npcs)
    
    def getRandomNPC(self):
        print_title_card(self)
        df = self.getNPC()
        mask = (df['Level'] >= self.min) & (df['Level'] <= self.max)
        rangedf =df[mask]
        rc =rangedf.sample(n=1)
        out = rc[['Name','Level']].to_string(index=False)

        print(out + '\n') 

    
if __name__ == "__main__":
    C1 = creature(min=-1, max = 3)
    C1.getRandomMonster()

    C2 = npc(min =7 , max =12)
    C2.getRandomNPC()

    C3 = npc(name = 'dragon')
    C3.getByName()
  