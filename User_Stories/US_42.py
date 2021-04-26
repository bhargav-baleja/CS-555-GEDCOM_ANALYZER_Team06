def date_validity_helper(this_date):
    feb = 28

    if (this_date.year % 4) == 0:
        feb = 29

    month_lengths = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return this_date.day < month_lengths[this_date.month - 1]










def reject_illegitimate_birthdays(table):  # US42: Reject Illegitimate Birthdays
    bad_date = []
    bad_dates = False

    for person in individuals:
        if not (person.birth is None or date_validity_helper(person.birth)) or not (
                person.death is None or date_validity_helper(person.death)):
            bad_date.append("{} has a illegitimate birthday.".format(person.name))
            bad_dates = True

    table.append(
        ["US42", "Reject Illegitimate Birthdays", "", not bad_dates, "\n".join(bad_date)])
