"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 02
"""

def US_02(individual, family):
    """checks if a person's birthday occurs before their marriage"""
    warnings = list()

    for family in family.values():
        if family._marriage_date != 'NA':
            if family._wife_id != 'NA':
                if individual[family._wife_id]._birth_date != 'NA':
                    if individual[family._wife_id]._birth_date > family._marriage_date:
                        warnings.append(
                            f'US_02: {individual[family._wife_id]._name} birthday after marriage date on line number {family.get_line_numbers()["date"]["marriage"]}')

            if family._husband_id != 'NA':
                if individual[family._husband_id]._birth_date != 'NA':
                    if individual[family._husband_id]._birth_date > family._marriage_date:
                        warnings.append(
                            f'US_02: {individual[family._husband_id]._name} birthday after marriage date on line number {family.get_line_numbers()["date"]["marriage"]}')

    return warnings