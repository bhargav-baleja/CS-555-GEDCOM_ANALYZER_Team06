"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 06
"""


def US_06(individual, family):
    """ US06 : Divorce of the husband or wife must be before death date of the individual"""

    warning = []
    for i, j in family.items():
        if j._divorce_date != 'NA':

            husband_death = individual[j._husband_id]._death_date
            wife_death = individual[j._wife_id]._death_date

            if husband_death != 'NA' and husband_death < j._divorce_date:
                warning.append(
                    f"US_06: {j._husband_name} Death {husband_death} occured prior to the divorce date {j._divorce_date}")

            elif wife_death != 'NA' and wife_death < j._divorce_date:
                warning.append(f"US_06: {j._wife_name} Death {wife_death} occured prior to the divorce date {j._divorced}")

    return warning