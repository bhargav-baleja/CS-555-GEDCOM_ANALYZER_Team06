"""
Test cases for user story US_08
Author: Bhargav Baleja
"""

"""Children should be born after marriage of parents (and not more than 9 months after their divorce)"""

def US_08(individual, family):
    warning = list()

    for fam in family.values():
        if fam._children != 'NA':
            husband_birth = individual[fam._husband_id]._birth_date
            wife_birth = individual[fam._wife_id]._birth_date
            for child in fam._children:
                if individual[child]._birth_date < husband_birth:
                    warning.append(f"Family id Line number: {fam._line_numbers.get('family_id')}\n The Father {fam._husband_id} is younger than his child {individual[child]._individual_id} which is illegal.")
                elif individual[child]._birth_date < wife_birth:
                    warning.append(f"Family id Line number: {fam._line_numbers.get('family_id')}\n The Mother {fam._wife_id} is younger than her child {individual[child]._individual_id} which is illegal.")

    return warning