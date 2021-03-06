"""
Test cases for user story US_09
Author: Bhargav Baleja
"""

""" Birth before death of parents """

def US_09(individual, family):
    warning = list()

    for fam in family.values():
        if fam._children != 'NA':
            husband_death = individual[fam._husband_id]._death_date

            wife_death = individual[fam._wife_id]._death_date
            for child in fam._children:
                if husband_death != "NA" and individual[child]._birth_date > husband_death:
                    warning.append(f"Family id Line number: {fam._line_numbers.get('family_id')}\n Birth of child {child} is before the death of the father {fam._husband_id}")
                if wife_death != "NA" and individual[child]._birth_date > wife_death:
                    warning.append(f"Family id Line number: {fam._line_numbers.get('family_id')}\n Birth of child {child} is before the death of the mother {fam._wife_id}")
    return warning
