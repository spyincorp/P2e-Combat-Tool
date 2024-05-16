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
    

    def getRandomMonster(self):
        if self.min is None or self.max is None:
            raise ValueError("Minimum and maximum levels must be provided.")
        df = beastiary_to_dataframe()
        mask = (df['Level'] >= self.min) & (df['Level'] <= self.max)
        rangedf =df[mask]
        rc =rangedf.sample(n=1)
        out = rc[['Name','Level']].to_string(index=False)

        print(out)
    
if __name__ == "__main__":
    C1 = creature(min=-1, max = 3)
    C1.getRandomMonster()
