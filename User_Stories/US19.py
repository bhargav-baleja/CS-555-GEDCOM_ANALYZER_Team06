INDI = {}
FAM = {}

class Individual:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.husb = None
        self.wife = None
        self.child = []


class Family:
    def __init__(self, id):
        self.id = id

def famExists(id):
    return id in FAM

def indiExists(id):
    return id in INDI

def saveFam(F):
    
    if famExists(F.id):
        #print(f"US22 - Family ID {F.id} already exists ")
        return False

    FAM[F.id] = F
    return True
    
def saveIndi(I):
    if indiExists(I.id):
        #print(f"US22 - Individual ID {I.id} already exists ")
        return False

    INDI[I.id] = I
    return True
    

MARRIAGE = { 

}

FAMILY_TREE = {

}

def convertToName(id):
  return INDI[id].NAME

def sliceUp(id):
  parents = []
  for i in FAMILY_TREE.keys():
    if id in FAMILY_TREE[i]['CHIL']:
      parents.append(i)
  return parents

def findGrandParents(x):
  arr = sliceUp(x)
  tmp = []
  for i in arr:
    #print(f"i is {i}")
    x = sliceUp(i)
    tmp.extend(x)
    #tmp.append(sliceUp(i))
  return tmp


def US19():
  with open("../GEDCOM_FILES/US19-.ged","r") as reader: 
    famSwitch = False

    temp = { 'CHIL' : []  }

    tempIndi = ''
    tempMarr = ''
    activate = False
    for line in reader.readlines():
      sLine = line.replace("\n","").replace("\t","").split(" ")

      if (len(sLine) >= 3):
          # if sLine[2] == 'FAM':
          #     i = Family(sLine[1])
          #     saveFam(i)
        if sLine[2] == 'INDI':
          #print(f" Indi -> {sLine[1]} ")
          tempIndi = sLine[1]
          #print(f"TempIndi is {tempIndi}")
          i = Individual(sLine[1])
          saveIndi(i)
        
        if sLine[1] == 'NAME':
          #print(f"Name is {sLine[2:]}")
          #print(f"tempIndi is {tempIndi}")
          if tempIndi in INDI:
            #print(sLine[2:])
            INDI[tempIndi].NAME = " ".join(sLine[2:])


        if sLine[2] == 'FAM':
          if not activate:
            activate = True

          if temp:
            #print(f"Clearing out {temp}")
            if 'HUSB' in temp:
              FAMILY_TREE[temp['HUSB']] = temp
            if 'WIFE' in temp:
              FAMILY_TREE[temp['WIFE']] = temp
    
            temp = { 'CHIL': [] }

        if activate:
          if sLine[1] == 'HUSB':
            temp['HUSB'] = sLine[2]
            
            if sLine[2] not in MARRIAGE:
              MARRIAGE[sLine[2]] = True
              tempMarr = sLine[2]

          
          if sLine[1] == 'WIFE':
            temp['WIFE'] = sLine[2]
            MARRIAGE[tempMarr] = (sLine[2])
          
          if sLine[1] == 'CHIL':
            temp['CHIL'].append(sLine[2])
    
    output = []
    for i in MARRIAGE.keys():
      x = findGrandParents(i)
      y = findGrandParents(MARRIAGE[i])

      res = set(x).intersection(y)

      if res:
        output.append(f"[US19] Cousins cannot marry each other :: {convertToName(i)} to {convertToName(MARRIAGE[i])}")
      #print(f" -- {convertToName(i)} married to {convertToName(MARRIAGE[i])} ")
    return output

"""
Individual
  Rick
    Wife: Mariah
    Children: [ Marry, Beth ]

  Marry
    Husb: Dave
      Children: [ Brenda ]
  
  Dave
    Wife: Marry
    Children: [ Brenda ]
  
  Beth
    Husb: Jerry
    Children: [ Morty ]
  
  Jerry
    Wife: Beth
    Children: [ Morty ]
  
  Morty
    

{ Morty: [ Jerry, Beth ],
  Jerry: [  ],
  Beth: [ Mariah, Rick ],
  Brenda: [ Marry, Dave ],
  Marry: [ Rick ],
  Dave: []
}

marriage { 
  Morty: Brenda,
  Beth: Jerry,
  Marry: Dave,
  Rick: Mariah
}

"""