__author__ = 'Haohan Wang'

import numpy as np

def getPhenotypeIndex():
    text = [line.strip() for line in open('../final/phenotypeNames.txt')]
    p2i = {} # pheno2index
    p2n = {}
    c = -1
    for line in text:
        c += 1
        items = line.split('_')
        p2i[int(items[0])] = c
        p2n[int(items[0])] = items[1]
    return p2i, p2n

def getGoldenStandardPosition():
    cate2pos = {}
    for i in range(1, 18):
        text = [line.strip() for line in open('../data/'+str(i)+'.txt')]
        pos = []
        for line in text:
            items = line.split('\t')
            pos.append((int(items[2]), int(items[0]), int(items[1])))
        cate2pos[i] = pos

    pheno2Cate={}
    text = [line.strip() for line in open('../data/phenotypeIndex.txt')]
    for line in text:
        items = line.split()
        c = int(items[0][:-1])
        for p in items[1:]:
            pheno2Cate[int(p)] = c

    return pheno2Cate, cate2pos


def getGenomePosition():
    text = [line.strip() for line in open('../final/genomeInformation.txt')]
    pos = []
    for line in text:
        items = line.split('\t')
        c = int(items[0])
        p = int(items[1])
        pos.append((c, p))
    snp = np.load('../final/geno.npy')
    assert len(pos) == snp.shape[1]

    return pos

def generateGoldenStandard():
    p2i, p2n = getPhenotypeIndex()
    p2c, c2g = getGoldenStandardPosition()
    pos = getGenomePosition()

    phenos = np.load('../final/pheno.npy')

    ids = []
    gld = []
    names = []

    for pheno in p2i:
        if pheno in p2c:
            genome = c2g[p2c[pheno]]
            l = []
            for i in range(len(pos)):
                c, p = pos[i]
                for (c1, s1, e1) in genome:
                    if c == c1 and s1 <= p <= e1:
                        l.append(i)
            if len(l) > 0:
                ids.append(p2i[pheno])
                names.append(p2n[pheno])
                gld.append(l)

    ids = np.array(ids)

    phe = phenos[:, ids]

    print phe.shape

    for l in gld:
        print l

    np.save('../finalWithGoldenStandard/pheno', phe)
    np.save('../finalWithGoldenStandard/goldenStandard', gld)

    f = open('../finalWithGoldenStandard/phenoNames.txt', 'w')
    for line in names:
        f.writelines(line+'\n')
    f.close()


if __name__ == '__main__':
    generateGoldenStandard()