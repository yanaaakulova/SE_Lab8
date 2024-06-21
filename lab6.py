with open("data.csv") as f:
    notSurvivedC = 0
    notSurvivedQ = 0
    notSurvivedS = 0
    next(f)
    for line in f:
        data = line.split(",")
        sex = data[5]
        port = data[12].strip()
        survived = data[1]
        age = 0
        if data[6] != "":
            age = float(data[6])
        if sex == "male" and age > 40 and survived == "0":
            if port == "C":
                notSurvivedC += 1
            if port == "Q":
                notSurvivedQ += 1
            if port == "S":
                notSurvivedS += 1
    print("Погибших мужчин старше 40 лет из Шербура:", notSurvivedC)
    print("Погибших мужчин старше 40 лет из Квинстауна:", notSurvivedQ)
    print("Погибших мужчин старше 40 лет из Саутгемптона:", notSurvivedS)
