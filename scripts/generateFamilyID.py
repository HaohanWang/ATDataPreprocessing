__author__ = 'Haohan Wang'

def generateCountryID():
    ids = [line.strip() for line in open('../final/ecotype_id.txt')]

    text = [line.strip() for line in open('../data/meta_info.tsv')]

    id2family = {}
    familyUnique = {}
    c = 0
    for line in text:
        items = line.split('\t')
        pid = items[1]
        fid = items[-1]
        if fid not in familyUnique:
            familyUnique[fid] = c
            c += 1
        id2family[pid] = familyUnique[fid]

    fams = [id2family[m] for m in ids]

    print len(set(fams))

    f = open('../final/countryID.txt', 'w')
    for m in fams:
        f.writelines(str(m)+'\n')
    f.close()


def generateRegionID():
    ids = [line.strip() for line in open('../final/ecotype_id.txt')]

    text = [line.strip() for line in open('../data/meta_info.tsv')]

    id2family = {}
    familyUnique = {}
    c = 0
    for line in text:
        items = line.split('\t')
        pid = items[1]
        fid = items[-2]
        if fid not in familyUnique:
            familyUnique[fid] = c
            c += 1
        id2family[pid] = familyUnique[fid]

    fams = [id2family[m] for m in ids]

    print len(set(fams))

    f = open('../final/regionID.txt', 'w')
    for m in fams:
        f.writelines(str(m)+'\n')
    f.close()


if __name__ == '__main__':
    generateRegionID()
