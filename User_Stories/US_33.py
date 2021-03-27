"""
Author: Bhargav Baleja
CS 555 Agile Methods for Software Development 
Purpose: user story 33
"""

def US_33(self):
        """List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file"""
        orphans = list()
        for family in self._family.values():
            if family._children != 'NA':
                for child in family._children:
                    if family._husband_id and family._wife_id:
                        if self._individual[family._husband_id]._death_date != 'NA' and self._individual[family._wife_id]._death_date != 'NA' and \
                                self._individual[child]._age != 'NA' and self._individual[child]._age < 18 and self._individual[child]._age >=0:
                            orphans.append(f"{self._individual[child]._individual_id} {self._individual[child]._name} "
                                           f"has age {self._individual[child]._age} and is orphan")

        return orphans
