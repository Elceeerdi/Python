import matplotlib.pyplot as var
# %matplotlib_inline #para jupyter notebook
#Grafica 2 vectores
var.plot(["Contabilidad","Estadística","Etica","Operaciones"]
         ,[9,8,10,7],'b-*') #Vector en Y
#Grafica por defecto el vecto X = 1, 2, 3, 4
var.title('Promedio')
var.ylabel('Calificación')
var.xlabel('Asignaturas')
var.show()
var.savefig("graph.png")
