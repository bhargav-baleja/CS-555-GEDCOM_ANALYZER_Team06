Deceased = {}
Married = {}
    

def US30(file):

    output = []
    with open(file,"r") as reader: 
        currentIndi = {}

        for line in reader.readlines():
            sLine = line.replace("\n","").replace("\t","").split(" ")

            if (len(sLine) == 3):
                
                if sLine[2] == 'INDI':
                    if 'DEAT' in currentIndi:
                        Deceased[currentIndi[id]] = True
                        #currentIndi[DEAT] = True
                        
                    currentIndi = {}
                    currentIndi[id] = sLine[1]

                if sLine[1] == "HUSB":
                    Married[sLine[2]] = True

                if sLine[1] == "WIFE":
                    Married[sLine[2]] = True
                
                if len(currentIndi) > 0:
                    if sLine[1] == 'NAME':
                        currentIndi['NAME'] = sLine[2:].join(" ")
                    
                    if sLine[1] == 'MARR':
                        currentIndi['MARR'] = True
                    
                    if sLine[1] == 'DEAT':
                        currentIndi['DEAT'] = True
                    
                    if sLine[1] == 'DIV':
                        currentIndi['DIV'] = True

    for i in Married.keys():
        if i not in Deceased:
            output.append(f"[US30] {i} is alive and married")
    return output

