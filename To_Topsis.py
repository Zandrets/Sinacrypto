from socketserver import DatagramRequestHandler
from matplotlib.colors import Normalize
import pandas as pd

class Topsis:
    def __init__(self):
        hashs=pd.DataFrame(pd.read_csv("sistemas_hash.csv",index_col="Algoritmos"))
        keys=pd.DataFrame(pd.read_csv("sistemas_llaves.csv"))
        self.topsis_pipy(hashs, hashs, len(hashs.columns), [3,1,1], ["+","-","-"])
#        self.Normalize(hashs, len(hashs.columns), [3,1,1])
#        data=self.Normalize(hashs, len(hashs.columns), [3,1,1])
#        self.Calc_Values(data, len(hashs.columns), ["+","-","-"])
    def Normalize(self, dataset, nCol, weights):
        for i in range(1, nCol):
            temp = 0
            # Calculating Root of Sum of squares of a particular column
            for j in range(len(dataset)):
                temp = temp + dataset.iloc[j, i]**2
            temp = temp**0.5
            # Weighted Normalizing a element
            for j in range(len(dataset)):
                dataset.iat[j, i] = (dataset.iloc[j, i] / temp)*weights[i-1]
        return dataset

    def Calc_Values(self, dataset, nCol, impact):
        p_sln = (dataset.max().values)[1:]
        n_sln = (dataset.min().values)[1:]
        for i in range(1, nCol):
            if impact[i-1] == '-':
                p_sln[i-1], n_sln[i-1] = n_sln[i-1], p_sln[i-1]
        return p_sln, n_sln
    
    def topsis_pipy(self, temp_dataset, dataset, nCol, weights, impact):
        # normalizing the array
        temp_dataset = self.Normalize(temp_dataset, nCol, weights)

        # Calculating positive and negative values
        p_sln, n_sln = self.Calc_Values(temp_dataset, nCol, impact)

        # calculating topsis score
        # print(" Generating Score and Rank...\n")
        score = []
        for i in range(len(temp_dataset)):
            temp_p, temp_n = 0, 0
            for j in range(1, nCol):
                temp_p = temp_p + (p_sln[j-1] - temp_dataset.iloc[i, j])**2
                temp_n = temp_n + (n_sln[j-1] - temp_dataset.iloc[i, j])**2
            temp_p, temp_n = temp_p**0.5, temp_n**0.5
            score.append(temp_n/(temp_p + temp_n))
        dataset['Topsis Score'] = score

        # calculating the rank according to topsis score
        dataset['Rank'] = (dataset['Topsis Score'].rank(
            method='max', ascending=False))
        dataset = dataset.astype({"Rank": int})

        # Writing the csv
        # print(" Writing Result to CSV...\n")
        dataset.to_csv("Topsis_hash.csv", index=False)
        # print(" Successfully Terminated")
Topsis()