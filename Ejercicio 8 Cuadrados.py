def CuadradosLIsta(Lista=[2,8,9,10,12,5,1]):
    ListaCuadrados=[]
    for i in range(0,len(Lista)):
        CuadradoNumero = Lista[i] * Lista [i]
	ListaCuadrados.append(CuadradoNumero) 
    return ListaCuadrados
CuadradosLIsta(Lista=[2,8,9,10,12,5,1])
