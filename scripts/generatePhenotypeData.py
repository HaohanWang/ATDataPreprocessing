__author__ = 'Haohan Wang'

import numpy as np

def generatePhenotype():
    text = [line.strip() for line in open('../data/phenotype_published_raw.tsv')]
    print len(text)
    phenoTypeIDs = text[0].split('\t')[2:]
    plantID = []
    dataTmp = [[] for i in range(len(text)-1)]
    c = -1
    for line in text[1:]:
        c+=1
        items = line.split('\t')
        plantID.append(items[0])
        dataTmp[c] = items[2:]
    print dataTmp[0]

    n = len(text)-1
    p = len(dataTmp[0])
    print p

    data = np.zeros([n, p])
    for j in range(p):
        naIndex = []
        values = []
        for i in range(n):
            if dataTmp[i][j] == 'NA':
                naIndex.append(i)
            else:
                try:
                    v = float(dataTmp[i][j])
                except:
                    v = 0
                values.append(v)
                data[i,j] = v
        # m = np.mean(values)  # We don't fill in the missing values ourselves
        m = np.nan
        for i in naIndex:
            data[i,j]=m

    print data.shape

    np.save('../preprocessedData/phenos', data)
    f1 = open('../final/phenotypeNames.txt', 'w')
    for n in phenoTypeIDs:
        f1.writelines(n+'\n')
    f1.close()

    f2 = open('../preprocessedData/phenoIDs', 'w')
    for n in plantID:
        f2.writelines(n+'\n')
    f2.close()

if __name__ == '__main__':
    generatePhenotype()
