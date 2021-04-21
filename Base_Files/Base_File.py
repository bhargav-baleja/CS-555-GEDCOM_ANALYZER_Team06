""" File that runs all the user stories and prints their results. """
import sys

from Base_Files.Logger import Logger
from Base_Files.Repository import Repository

from User_Stories.US_2 import US_2
from User_Stories.US_3 import US_3
from User_Stories.US_05 import US_05
from User_Stories.US_06 import US_06
from User_Stories.US_08 import US_08
from User_Stories.US_09 import US_09
from User_Stories.US_11 import US_11
from User_Stories.US_33 import US_33

def main():
    """ Function that runs all the user stories and prints their results. """
    sys.stdout = Logger()
    # Creating an object of class Repository that will contains both individual and family dictionaries.
    # Pass the path of your GEDCOM file as a parameter below.
    repository = Repository("../GEDCOM_Files/US_02.ged")
    repository1 = Repository("../GEDCOM_Files/US_03.ged")
    repository2 = Repository("../GEDCOM_Files/US_33.ged")
    repository3 = Repository("../GEDCOM_Files/US_06.ged")
    individual = repository.get_individual()
    individual1 = repository1.get_individual()
    individual2 = repository2.get_individual()
    individual3 = repository3.get_individual()
    family = repository.get_family()
    family3 = repository3.get_family()

    # Prints individual pretty table.
    repository.individual_pretty_table()
    # Prints family pretty table.
    repository.family_pretty_table()

    for item in US_2(individual, family):
        print(item)

    for item in US_3(individual1):
        print(item)

    for item in US_05(individual, family):
        print(f"US-05: {item}")

    for item in US_06(individual3, family3):
        print(f"{item}")

    for item in US_08(individual, family):
        print(f"US-08: {item}")

    for item in US_09(individual, family):
        print(f"US-09: {item}")

    for item in US_11(repository):
        print(f"US_11: {item}")

    for item in US_33(repository2):
        print(f"US_33: {item}")



if __name__ == '__main__':
    """ Calls main method. """
    main()