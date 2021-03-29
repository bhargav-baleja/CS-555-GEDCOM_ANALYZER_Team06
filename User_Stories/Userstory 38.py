def upcoming_birthdays(table): 
    birthdays_upcoming = []

    for person in individuals:
        if person.birth is not None:
            birthdate = datetime(datetime.now().year, person.birth.month, person.birth.day).date()
            days_until_birthday = birthdate - datetime.today().date()

            if birthdate > datetime.today().date() and days_until_birthday < timedelta(days=30):
                birthdays_upcoming.append(person.name)

    table.append(
        ["US38", "Upcoming Birthdays", "", True, "\n".join(birthdays_upcoming)])
