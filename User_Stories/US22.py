INDI = {}
FAM = {}

class Individual:
    def __init__(self, id):
        self.id = id


class Family:
    def __init__(self, id):
        self.id = id

def famExists(id):
    return id in FAM

def indiExists(id):
    return id in INDI

def saveFam(F):
    
    if famExists(F.id):
        print(f"US22 - Family ID {F.id} already exists ")
        return False

    FAM[F.id] = F
    return True
    
def saveIndi(I):
    if indiExists(I.id):
        print(f"US22 - Individual ID {I.id} already exists ")
        return False

    INDI[I.id] = I
    return True
    

with open("../GEDCOM_Files/US22_23.ged", "r") as reader:

    for line in reader.readlines():
        sLine = line.replace("\n","").replace("\t","").split(" ")

        if (len(sLine) == 3):
            if sLine[2] == 'FAM':
                i = Family(sLine[1])
                saveFam(i)

            if sLine[2] == 'INDI':
                i = Individual(sLine[1])
                saveIndi(i)
    