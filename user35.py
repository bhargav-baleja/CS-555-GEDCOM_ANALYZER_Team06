
def list_recent_births(table):  
    recent_births = []

    for person in individuals:
        if person.birth is not None and datetime.now().date() - timedelta(
                days=365) <= person.birth <= datetime.now().date():
            recent_births.append(person.name)

    table.append(
        ["US35", "List Recent Births", "", True, "\n".join(recent_births)])
