"""
Bhargav Baleja
SSW 555 Agile Methods for Software Development Project 2
Purpose: Practice programming with GEDCOM data 
"""
def gedcom_reader(file_path):
    """This function gedcom_reader reads a file path, fields, separator and header and returns the values of the fields
    in the file if the fields given is equal to fields number in file """
    gedcom_data = {'0': ["HEAD", "NOTE", "TRLR"],
                   '1': ["BIRT", "CHIL", "DEAT", "DIV", "FAMC", "FAMS", "HUSB", "MARR", "NAME", "SEX", "WIFE"],
                   '2': ["DATE"], }
    try:
        file_location = open(file_path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open {path}")
    else:
        with file_location:
            for line in file_location:
                line = line.rstrip()
                print(f"--> {line}")
                the_line = line.split()
                valid = "N"  #<valid?> has the value 'N' if the tag is not one of the supported tags 
                level = the_line[0]
                tag = the_line[1]
                arguments = " ".join(the_line[2:])
                if the_line[0] == "0" and len(the_line) >= 3 and the_line[2] in ["FAM", "INDI"]:
                    valid = "Y"
                    tag = the_line[2]
                    arguments = the_line[1]
                elif level in gedcom_data and tag in gedcom_data[level]:
                    valid = 'Y'  #<valid?> has the value 'Y' if the tag is one of the supported tags

                print(f"<-- {level}|{tag}|{valid}|{arguments}")


def main():
    gedcom_reader(r'D:/CS-555-B/Project_01_bbaleja(gedcom_file).ged')

if __name__ == '__main__':
    main()
