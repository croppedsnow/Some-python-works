def check(x: str, name_file: str):
    file = open(name_file, "w")
    x = x.lower().split(" ")
    d = {}
    for i in range(len(x)):
        if x[i] in d.keys():
            d[x[i]] += 1
        else:
            d[x[i]] = 1
    for i in sorted(list(d.keys())):
        file.write(i + " " + str(d[i]) + "\n")
    file.close()


