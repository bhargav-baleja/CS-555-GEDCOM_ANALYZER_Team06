INDI = {}
FAM = {}

class Individual:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.date = ""


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
    
from datetime import datetime, date


def US27():

  output = []

  with open("../GEDCOM_FILES/US19-.ged","r") as reader: 

    name = ''
    date = ''
    tempIndi = ''

    famReached = False
    indiBlock = False

    for line in reader.readlines():
      sLine = line.replace("\n","").replace("\t","").split(" ")

      if (len(sLine) >= 3):

        if sLine[2] == 'INDI':
          
          if date:
            date = datetime.strptime(date,'%d %b %Y')
            today = date.today()
            age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
            #print(f"[US27] {name} is {age} years old ")
            output.append(f"[US27] {name} is {age} years old")
          
          famBlock = False
          indiBlock = True

        
        if sLine[1] == 'NAME':
          if indiBlock:
            name = " ".join(sLine[2:])

        if sLine[1] == 'DATE':
          if indiBlock:
            date = " ".join(sLine[2:])

        if sLine[2] == 'FAM':          
          indiBlock = False
    output.append(f"[US27] {name} is {age} years old")
  
  return output
