def siblings_should_not_marry(table):  # US18: Siblings Should Not Marry
    sibling_marriage = False
    notes = []
    for fam in families:
        if fam.children and len(fam.children) > 1:
            for i in range(len(fam.children)):
                for j in range(i + 1, len(fam.children)):
                    if any(fam.children[i] in [f.husband, f.wife] and fam.children[j] in [f.husband, f.wife] for f in
                           families):
                        sibling_marriage = True
                        notes.append("{} and {} are married siblings.".format(get_individual(fam.children[i]).name,
                                                                              get_individual(fam.children[j]).name))

    if sibling_marriage:
        result = "Some siblings are married."
    else:
        result = "All siblings are not married."

    table.append(
        ["US18", "Siblings Should Not Marry", "\n".join(notes), not sibling_marriage, result])
