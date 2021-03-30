Deceased = {}
    

def US29(file):

    output = []
    with open(file,"r") as reader: 
        currentIndi = {}

        for line in reader.readlines():
            sLine = line.replace("\n","").replace("\t","").split(" ")

            if (len(sLine) == 3):

                if sLine[2] == 'INDI':
                    
                    #last ele
                    if 'DEAT' in currentIndi:
                        output.append(f"[US29] {currentIndi[id]} is deceased")
                        #print(output[-1])

                    # reset data                
                    currentIndi = {}
                    currentIndi[id] = sLine[1]
                
                if len(currentIndi) > 0:
                    if sLine[1] == 'NAME':
                        currentIndi['NAME'] = sLine[2:].join(" ")
                    
                    if sLine[1] == 'DEAT':
                        currentIndi['DEAT'] = True
    return output


#US29('US_29-30.ged')