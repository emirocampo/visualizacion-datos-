import csv
import matplotlib.pyplot as plt

listReturn = []
def readData( pathFile, company):
    with open(pathFile) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            # print(line)
            #print(f"line[2] : {line[2]} -- company : {company}")
            if line[2] == company:
                listReturn.append({
                    "ConsoleName" : line[0],
                    "ReleasedYear" : int( line[3] ),
                    "UnitsSold" : float( line[5] )})
        
        return listReturn

def sortList(listS):
    inter = True
    while inter:
        inter = False
        for i in range( len( listS ) - 1 ):
            if listS[i]["ReleasedYear"] > listS[i +1]["ReleasedYear"]:
                listS[i], listS[i +1] = listS[i+1], listS[i]
                inter = True
    return listS

def chart(listC):
    years = list( map( lambda row : row["ReleasedYear"], listC) )
    units = list( map( lambda row : row["UnitsSold"], listC) )
    console = list( map( lambda row : row["ConsoleName"], listC) )
    
    fig, ax = plt.subplots()
    bar_width = 2.0  
    ax.set_title('Millones de consolas vendidas por su fecha de lanzamiento')
    ax.set_xlabel("Año de lanzamiento")    
    ax.set_ylabel('Unidades vendidas')    
    
    plt.bar(years, units)    
    plt.show()

    plt.title('Millones de consolas vendidas por su fecha de lanzamiento')
    plt.bar(console, units)
    plt.show()

    #grafica de pie
    plt.title('Millones de consolas vendidas por su fecha de lanzamiento')
    plt.pie(units, labels=years, autopct="%0.1f %%")
    plt.show()

    #grafica de dispersión
    plt.title('Millones de consolas vendidas por su fecha de lanzamiento')
    plt.scatter(years, units)
    plt.show()

    #grafica de burbujas --> esta es una varioacion del scatter
    plt.scatter(years, units, s=units)
    plt.show()

