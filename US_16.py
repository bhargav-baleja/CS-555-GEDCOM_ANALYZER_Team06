#Story Owner-Ananya

def male_last_name(table):  # US16: Male Last Names
    fat_last_name = True
    x = []
    for fam in families:
        if fam.children:
            l_name = get_individual(fam.husb).name[get_individual(fam.husb).name.rfind(" "):]

            for m in fam.children:
                if get_individual(m).sex == "M" and l_name not in get_individual(m).name:
                    x.append(
                        "{} does not have  fat's  last name, {}".format(get_individual(m).name, l_name))
                    fat_l_name = False

    if fat_last_name:
        result = "All male children have their fat's last name."
    else:
        result = "Few male children does not  have their fat's  last name."

    table.append(
        ["US16", "Male Last Names", "\n".join(x), fat_last_name, result])
