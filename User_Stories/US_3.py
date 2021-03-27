"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 03
"""

from Base_Files.Repository import Repository

def US_3(individual):

        repository = Repository("../GEDCOM_Files/US_03.ged")
        individual = repository.get_individual()
        """ checks if a person's birthday occurs before their death day """
        warnings = list()

        for person in individual.values():
            if person._birth_date != 'NA' and person._death_date != 'NA':
                if person._birth_date > person._death_date:
                    warnings.append(f'US_03: {person._name} birthday after death date on line number {person.get_line_numbers()["date"]["death"]}')

        return warnings

