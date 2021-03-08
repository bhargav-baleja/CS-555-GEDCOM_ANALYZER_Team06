# Format Name.key = Date
NAME = {}

with open("../GEDCOM_Files/US22_23.ged", "r") as reader:

    indi_group = False
    current_indi = ""
    current_name = ""
    birt_flag = False

    for line in reader.readlines():
        sLine = line.replace("\n","").replace("\t","").split(" ")

        if( len(sLine) >= 1 ):
            if sLine[1] == 'NAME':
                current_name = " ".join(sLine[2:])
            
            elif sLine[1] == 'BIRT':
                birt_flag = True

            elif sLine[1] == 'DATE' and birt_flag:
                f_date = "_".join(sLine[2:])
                if current_name not in NAME.keys():
                    NAME[current_name] = f_date
                    #print(f"Added Name {current_name} with birthdate : {f_date} ")
                elif NAME[current_name] == f_date:
                    print(f"US23 : Name {current_name} with birthdate {f_date} already exists")
                
                birt_flag = False


        if (len(sLine) == 3):

            if sLine[2] == 'INDI':
                indi_group = True
                current_indi = sLine[1]