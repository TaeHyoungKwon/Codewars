with open("config.txt", "r") as txt:
    lines = txt.readlines()
    for line in lines:
        variable_, value = line.split(' = ')
        print(f"{variable_}: {value}")
