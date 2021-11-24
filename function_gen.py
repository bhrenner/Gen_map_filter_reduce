from datetime import datetime

def faz_dicio(arq):
    dicio = {}
    for i, cont in enumerate(arq):
        if i == 0:
            dicio['Data'] = datetime.strptime(cont, '%d/%m/%Y').date()
        if i == 1:
            dicio['Pfa'] = cont
        if i == 2:
            dicio['Region'] = cont
        if i == 3:
            dicio['Offence'] = cont
        if i == 4:
            dicio['Total'] = int(cont)
    return dicio
