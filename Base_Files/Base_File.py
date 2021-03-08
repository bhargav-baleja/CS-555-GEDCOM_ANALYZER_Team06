""" File that runs all the user stories and prints their results. """
import sys

from Base_Files.Logger import Logger
from Base_Files.Repository import Repository


def main():
    """ Function that runs all the user stories and prints their results. """
    sys.stdout = Logger()
    # Creating an object of class Repository that will contains both individual and family dictionaries.
    # Pass the path of your GEDCOM file as a parameter below.
    repository = Repository("../GEDCOM_Files/Gedcom_Project03.ged")
    individual = repository.get_individual()
    family = repository.get_family()

    # Prints individual pretty table.
    repository.individual_pretty_table()
    # Prints family pretty table.
    repository.family_pretty_table()

if __name__ == '__main__':
    """ Calls main method. """
    main()