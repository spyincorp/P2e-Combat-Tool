import csv
import random
import pandas as pd

from BlockReader import beastiary_to_dataframe

class creature:
    def __init__(self, cr=0, type=None, npc=False, min=None, max=None):
        self.cr = cr
        self.type = type
        self.npc = npc
        self.min = min
        self.max = max
    
    def getNPC(self):
        df = pd.read_csv('Data\BeastiaryCsv\Beastiary.csv')
        mask = df['Traits'].apply(lambda x: 'humanoid' in x)
        npcs =df[mask]
        return(npcs)
    
    def getRandomMonster(self):
        if self.min is None or self.max is None:
            raise ValueError("Minimum and maximum levels must be provided.")
        
        elif self.npc:
            df = self.getNPC()
            mask = (df['Level'] >= self.min) & (df['Level'] <= self.max)
            rangedf =df[mask]
            rc =rangedf.sample(n=1)
            out = rc[['Name','Level']].to_string(index=False)

            print(out)            
        else:
            df = pd.read_csv('Data\BeastiaryCsv\Beastiary.csv')
            mask = (df['Level'] >= self.min) & (df['Level'] <= self.max)
            rangedf =df[mask]
            rc =rangedf.sample(n=1)
            out2 = rc[['Name','Level']].to_string(index=False)

            print(out2)
    
if __name__ == "__main__":
    C1 = creature(min=-1, max = 3)
    C1.getRandomMonster()
    C2 = creature(npc=True, min =7 , max =12)
    C2.getRandomMonster()