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
    # print(years)
    # print(units)
    fig, ax = plt.subplots()
    #Colocamos una etiqueta en el eje Y
    ax.set_ylabel('Unidades vendidas')
    #Colocamos una etiqueta en el eje X
    ax.set_title('Año de lanzamiento')
    #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
    plt.bar(years, units)
    #plt.savefig('barras_simple.png')
    #Finalmente mostramos la grafica con el metodo show()
    plt.show()
    plt.bar(console, units)
    plt.show()