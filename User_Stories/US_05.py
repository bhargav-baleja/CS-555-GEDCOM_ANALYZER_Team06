"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development
Purpose: Testing for user story 05
"""

"""Marriage should occur before death of either spouse"""

def US_05(individual, family):
    warning = list()
    for fam in family.values():
        married = fam._marriage_date
        for indi in individual.values():
            if fam._husband_id == indi._individual_id and indi._death_date != 'NA'and married!= "NA":
                if indi._death_date < married:
                    warning.append(f"Marriage date Line: {fam._line_numbers.get('date').get('marriage')}\nDeath of Husband date Line: {indi._line_numbers.get('date').get('death')}\nThe family {fam._family_id} has a death of husband {fam._husband_id} before the marriage date.")
            elif fam._wife_id == indi._individual_id and indi._death_date != 'NA' and married!= "NA":
                if indi._death_date < married:
                    warning.append(f"Marriage date Line: {fam._line_numbers.get('date').get('marriage')}\nDeath of wife date Line: {indi._line_numbers.get('date').get('death')}\nThe family {fam._family_id} has a death of wife {fam._wife_id} before the marriage date.")

    return warning
