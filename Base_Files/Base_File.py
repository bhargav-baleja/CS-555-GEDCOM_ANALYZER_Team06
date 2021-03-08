""" File that runs all the user stories and prints their results. """
import sys

from Base_Files.Logger import Logger
from Base_Files.Repository import Repository

from User_Stories.US_2 import US_2
from User_Stories.US_11 import US_11

def main():
    """ Function that runs all the user stories and prints their results. """
    sys.stdout = Logger()
    # Creating an object of class Repository that will contains both individual and family dictionaries.
    # Pass the path of your GEDCOM file as a parameter below.
    repository = Repository("../GEDCOM_Files/US_02.ged")
    individual = repository.get_individual()
    family = repository.get_family()

    # Prints individual pretty table.
    repository.individual_pretty_table()
    # Prints family pretty table.
    repository.family_pretty_table()

    for item in US_2(individual, family):
        print(item)

    for item in US_11(repository):
        print(f"US_11: {item}")

if __name__ == '__main__':
    """ Calls main method. """
    main()