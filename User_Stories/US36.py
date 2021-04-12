def list_recent_deaths(table):  # US36: List Recent Deaths
    recent_deaths = []

    for person in individuals:
        if person.death is not None and datetime.now().date() - timedelta(
                days=365) <= person.death <= datetime.now().date():
            recent_deaths.append(person.name)

    table.append(
        ["US36", "List Recent Deaths", "", True, "\n".join(recent_deaths)])
