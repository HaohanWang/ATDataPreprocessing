__author__ = 'Haohan Wang'

import numpy as np

def getPhenotypeIndex():
    text = [line.strip() for line in open('../final/phenotypeNames.txt')]
    p2i = {}
    c = -1
    for line in text:
        c += 1
        items = line.split('_')
        p2i[items[1]] = c
    return p2i

def getGoldenStandardPosition():
    text = [line.strip() for line in open('../data/locations.txt')]
    n2g = {}
    name = None
    for line in text:
        if line.startswith('***'):
            items = line.split(',')
            for i in range(len(items)):
                if i == 0:
                    ms = items[i].split(':')
                    name = ms[0][3:]
                    c = int(ms[1])
                    s = int(ms[2].split('-')[0])
                    e = int(ms[2].split('-')[1])
                    n2g[name] = [(c, s, e)]
                else:
                    ms = items[i].split(':')
                    try:
                        int(ms[0]) == 0
                    except:
                        print ms[0]
                    else:
                        c = int(ms[0])
                        s = int(ms[1].split('-')[0])
                        e = int(ms[1].split('-')[1])
                        n2g[name] = [(c, s, e)]
    return n2g

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
    p2i = getPhenotypeIndex()
    n2g = getGoldenStandardPosition()
    pos = getGenomePosition()

    phenos = np.load('../final/pheno.npy')

    ids = []
    gld = []
    names = []
    for name in n2g:
        if name in p2i:
            idx = p2i[name]
            l = []
            for i in range(len(pos)):
                c, p = pos[i]
                for (ci, s, e) in n2g[name]:
                    if c == ci and (s <= p <= e):
                        l.append(i)
            if len(l) > 0:
                ids.append(idx)
                names.append(name)
                gld.append(l)
            else:
                print name
        else:
            print name
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