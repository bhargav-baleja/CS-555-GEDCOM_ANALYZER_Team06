def less_than_fifteen_siblings(table):  # US15: Fewer Than 15 Siblings
    t = False #if there are many kids 
    x = [] #list 
    for fam in families:
        if fam.kid and len(fam.kid) >= 15:
            x.append("Family {} has greater than 15 children.".format(fam.f_id))
            t = True `

    if t:
        result = "Some families have many children."
    else:
        result = "Other(all) families have less than 15 children."

    table.append(
        ["US15", "LEss Than 15 Siblings", "\n".join(x), not t, result])
