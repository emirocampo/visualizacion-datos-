import data


pathFile = "../consoles.csv"

companies = {
    1 : "Atari",
    2 : "Bandai",
    3 : "Coleco",
    4 : "Magnavox/Philips",
    5 : "Mattel",
    6 : "Micro Genius",
    7 : "Microsoft",
    8 : "NEC",
    9 : "NEC/Hudson Soft[note 6]",
    10 : "Nintendo",
    11 : "Nokia",
    12 : "Philips",
    13 : "Sega",
    14 : "Sony",
    15 : "Tectoy"
}

def menu():
    print("Elija una de las siguientes opciones (solo el número)")
    for cod,name in companies.items():
        print(f"{cod} : {name}")

def main(): 
    menu()
    keyC = int( input() )
    company = companies[ keyC ]
    listR = data.readData( pathFile, company )
    #print(listR)
    listS = data.sortList(listR)
    #print(listS)
    data.chart(listS)


if __name__ == "__main__":
    main()