def list_living_single(table):  # US31: List Living Single
    living_single = []

    for person in individuals:
        if person.spouse_id is None and person.death is None:
            living_single.append(person.name)

    table.append(
        ["US31", "List Living Single", "", True, "\n".join(living_single)])
