__author__ = 'Haohan Wang'

import numpy as np

def eco2array():
    text = [line.strip() for line in open('../data/meta_info.tsv')][1:]
    e2a = {}
    for line in text:
        items = line.split('\t')
        e2a[items[1]] = items[0]
    return e2a


def mergeFile():
    snpsIDs = [line.strip() for line in open('../preprocessedData/snpIDs.txt')]
    snps = np.load('../preprocessedData/snps.npy')

    geno = {}
    for i in range(len(snpsIDs)):
        geno[snpsIDs[i]] = snps[i,:]

    phenoIDs = [line.strip() for line in open('../preprocessedData/phenoIDs')]
    phenos = np.load('../preprocessedData/phenos.npy')

    pheno = {}
    for i in range(len(phenoIDs)):
        pheno[phenoIDs[i]] = phenos[i,:]

    e2a = eco2array()

    sData = []
    pData = []
    eids = []

    for eid in pheno:
        aid = e2a[eid]
        if aid in geno:
            eids.append(eid)
            pData.append(pheno[eid])
            sData.append(geno[aid])

    pData = np.array(pData)
    sData = np.array(sData)

    f = open('../final/ecotype_id.txt', 'w')
    for eid in eids:
        f.writelines(eid + '\n')
    f.close()

    np.save('../final/pheno', pData)
    np.save('../final/geno', sData)

if __name__ == '__main__':
    mergeFile()