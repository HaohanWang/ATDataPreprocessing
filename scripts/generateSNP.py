__author__ = 'Haohan Wang'

import numpy as np

def generateSNPData():
    text = [line.strip() for line in open('../data/call_method_32.b')]
    ids = text[0].split(',')[2:]
    n = len(ids)
    p = len(text)-2
    data = np.zeros([n, p])
    genomeInformation = []
    positionInformation = []
    j = -1
    for line in text[2:]:
        j += 1
        items = line.split(',')
        genomeInformation.append(items[0])
        positionInformation.append(items[1])

        genes = items[2:]
        base = genes[0]
        baseCount = 0
        for i in range(n):
            if genes[i] == base:
                baseCount += 1
        if baseCount > n/2.0:
            a = 0
            b = 1
        else:
            a = 1
            b = 0
        for i in range(n):
            if genes[i] == base:
                data[i,j] = a
            else:
                data[i,j] = b

    print data.shape
    np.save('../preprocessedData/snps', data)

    print len(genomeInformation)

    f1 = open('../final/genomeInformation.txt', 'w')
    for i in range(len(genomeInformation)):
        f1.writelines(genomeInformation[i]+'\t'+positionInformation[i]+'\n')
    f1.close()

    f2 = open('../preprocessedData/snpIDs.txt', 'w')
    for i in ids:
        f2.writelines(i+'\n')
    f2.close()

if __name__ == '__main__':
    generateSNPData()