Bienvenida = print("✩ Bienvenido(a)s a nuestro proyecto ✩\nRealizado por: Paola Michelle Herrera Flores - A01284702 y Valeria Enríquez Limón - A00832782")

import csv

nombre_archivo=r"Udemy_Clean.csv"
with open(nombre_archivo,encoding="utf8",  newline='') as f:
    datos=csv.reader(f)
    udemy=list(datos)

def view1():
    #Para saber el total de cursos de la lista
    print("\nANÁLISIS DE LA CANTIDAD DE CURSOS CON MAYOR Y MENOR CALIFICACIÓN")
    total_values= int(len(udemy))
     
   
#OVERALL RATINGS (SIGLAS-"or")
#Promedio de todos los ratings para cada curso

#Overall 1.1
#Lista con todos los valores bajo 'Overall ratings' Columna:2
    list_overall_ratings=[] #creamos lista donde guardaremos los valores de 'Overall rating'
    for i in range(1,total_values): #dentro del rango de 1 para no contar los encabezados hasta total de filas
        overall_ratings= float(udemy[i][2]) #por cada fila, va a la columna 2 de 'udemy' y lo guarda en una variable #en float para poder hacer operaciones con ellos
        list_overall_ratings.append(overall_ratings) #se agrega variable guardada en una lista y asi con todas las filas en 'udemy'
#Los rangos en los que se califican los cursos son:
    num_maximo_or=max(list_overall_ratings) #Rango máximo
    num_minimo_or=min(list_overall_ratings) #Rango mínimo
    print('Los cursos se califican de ', num_minimo_or, ' a ', num_maximo_or)
#La cantidad de cursos con mejores calificaciones y con las peores calificaciones
    cursos_maximo_or= list_overall_ratings.count(num_maximo_or)#cuenta cursos mejores calificados con función count
    cursos_minimo_or= list_overall_ratings.count(num_minimo_or)#cuenta cursos peores calificados con función count
    print('Hay ', cursos_maximo_or, ' con calificación de ', num_maximo_or, '.') #Despliega en pantalla
    print('Hay ', cursos_minimo_or, ' con calificación de ', num_minimo_or, '.') #Despliega en pantalla

#Overall 1.2
#GRÁFICA OVERALL RATING
    print("GRÁFICA DE DISPERSIÓN DE CALIFICACIÓN POR CURSO")
    import matplotlib.pyplot as plt
#Para que no se impriman los nombres de los cursos:
# creamos una lista que va desde 1 hasta el total de cantidad de cursos en Udemy.
    cursos_numeros=[]
    for i in range(0,(total_values-1)):
        cursos_numeros.append(i)
#Para hacer la gráfica:
    ejey=(list_overall_ratings)
    ejex=cursos_numeros
    plt.scatter(ejex,ejey, color="purple", s=2.5) #Usamos scatter para grafica de dispersión, 's' es el tamaño de punto
    plt.title("Calificación por curso\n (cada punto representa un curso)")
    plt.ylabel("Escala de ratings (0-5)")
    plt.xlabel("Cursos")
    plt.show()

def view2():

#NUMBER OF RATINGS (SIGLAS-nor)
#Con esta información podemos clasificar los cursos más famosos y con más impacto a los menos
#Lista con todos los valores bajo 'No_of_ratings' Columna:5

    print("\nCURSO CON MAYOR CANTIDAD DE REVIEWS")
    total_values= int(len(udemy))
    list_number_of_ratings=[] #creamos lista donde guardaremos los valores de 'No of rating'
    for i in range(1,total_values): #dentro del rango de 1 para no contar los encabezados hasta total de filas
        number_of_ratings= int(udemy[i][5]) #por cada fila, va a la columna 2 de 'udemy' y lo guarda en una variable
        list_number_of_ratings.append(number_of_ratings) #se agrega variable guardada en una lista y asi con todas las filas en 'udemy'

#No_Ratings 2.1
#Sacar curso con mayor reviews
    num_maximo_nor=max(list_number_of_ratings)#maximo de lista
#Sacar nombre, rating y cantidad de ratings del curso de mayor ratings
    numero_curso_mayor_ratings=(list_number_of_ratings.index(num_maximo_nor))+1 #se busca en que posición esta el máximo para poderlo buscar en 'udemy',
    #se suma +1 porque al hacer la lista no contamos encabezados y en udemy si estan.
    nombre_curso_mayor_ratings=(udemy[numero_curso_mayor_ratings][1]) #titulo
    categoria_curso_mayor_ratings=(udemy[numero_curso_mayor_ratings][6]) #categoria
    rating_curso_mayor_ratings=(udemy[numero_curso_mayor_ratings][2]) #rating
    print ('El curso con más review es \"',nombre_curso_mayor_ratings, '\" con ',num_maximo_nor, ' de reviews.','Entra en la categoría de \"',categoria_curso_mayor_ratings, '\" y su rating es de ',rating_curso_mayor_ratings, '.')

#No_Ratings 2.2
#Cantidad de cursos que no han tenido la mínima cantidad de reviews
    print("CURSOS CON NINGÚN REVIEW")
    num_minimo_nor=min(list_number_of_ratings) #para saber el numero minimo de lista
    cursos_minimo_nor= list_number_of_ratings.count(num_minimo_nor) #cuantas veces se repite este mínimo
    print ('Hay ', cursos_minimo_nor, 'cursos que tienen ', num_minimo_nor, ' reviews. ')

#No_Ratings 2.3
#También podríamos sacar un total de cuántas personas han tomado cursos en Udemy.
    print("TOTAL DE PERSONAS EN UDEMY QUE HAN DEJADO REVIEW")
    total_usuarios=sum(list_number_of_ratings) #usando 'sum' sumamos todos los usuarios basando en los numeros de ratings dentro de la lista que creamos de solamente los numeros de rating
    print ('En total, hay', total_usuarios,'personas que han tomado cursos en Udemy y han dejado reviews. ')
    
    
#NO HAY GRÁFICA NO OF RATINGS


def view3():
    
    total_values= int(len(udemy))

#CATEGORY (SIGLAS-c)
#Lista con todos los valores bajo 'Category' Columna:6
    print("\nCUANTAS CATEGORIAS HAY")
    list_category=[] #creamos lista de las pasadas veces
    for i in range(1,total_values):
        category= (udemy[i][6])
        list_category.append(category)
    
#Category 3.1
#Guarde la misma lista en otra variable para mantener la lista con todas las categorias intacta porque se usara luego
    total_categorias=[]
    for elemento in list_category:
        total_categorias.append(elemento)  #se crea la misma lista que list_category
#Lista con todas las diferentes categoría
    for elemento in total_categorias: #por cada elemento de la lista que tiene las categorias de todas las columnas
        while not total_categorias.count(elemento)==1: #mientras la cuenta de total de categorías no sea 1, se va a seguir removiendo elemento hasta que solo quede un valor asi
            total_categorias.remove(elemento)
    print(total_categorias)
#por ejemplo, si elemento=marketing, y existe más de un elemento 'marketing' en la lista, entonces lo va a borrar hasta que quede uno solo
#esto nos deja con una lista que tiene las diferentes categorías que usa udemy
#la lista queda asi: ['Leadership & Management', 'Finance & Accounting', 'IT & Software', 'Office Productivity', 'Design', 'Business', 'Personal Development',
#'Development', 'Lifestyle', 'Photography & Video', 'Marketing', 'Music', 'Teaching & Academics', 'Health & Fitness']#

#Cuantos cursos tienen cada categoría
    print("CUANTOS CURSOS HAY POR CATEGORÍA")
    cursos_por_categoria=[] #creamos lista que vamos a usar 
    for i in range(len(total_categorias)): #por cada categoria:
        count_c=list_category.count((total_categorias[i])) #cuenta cuantas veces se repite en la lista creada al principio que contenia las categorías de todas las filas
        cursos_por_categoria.append(count_c)
    #print(cursos_por_categoria) #los agrega a una lista, donde los indices corresponden a cada categoria-sus cursos
#Texto donde dice cuantos cursos hay por categoría
    for i in range(len(total_categorias)): #por cada categoría imprime su cantidad de cursos usando indice [i]
        print('De la categoría',total_categorias[i], 'hay', cursos_por_categoria [i], 'cursos.')

#Category 3.2
#GRÁFICA CATEGORY
    print("GRÁFICA CIRCULAR DE DISTRIBUCIÓN DE CATEGORÍAS")
    import matplotlib.pyplot as plt #se importa matplotlib para hacer gráfica
    cantidad=cursos_por_categoria #es el contenido
    categorias=total_categorias#son las etiquetas
    plt.title("Distribución de cursos por categoría")
    plt.pie(cantidad, labels=categorias, autopct='%0.1f%%') #'.pie' para grafica circular, 'autopct' es para moestrar los porcentajes y hasta que decimal
    plt.show() #muestra gráfica
#Referencia:Auribox Training (2020). "Matplotlib (Parte 3): Gráficas de Pie (Pastel)" Recuperado de: https://www.youtube.com/watch?v=C3-CJPOJGbI&t=50s&ab_channel=AuriboxTraining

def view4():
 
#TOPIC (SIGLAS-t) Columna:8
#Muestra el tema del que se habla en el curso.
#OBJETIVO: Checar cuál es la categoría que tiene más temas

#Usamos los valores utilizados previamente para nuestro análisis.
    total_values= int(len(udemy))
    list_category=[] #creamos lista de las pasadas veces
    for i in range(1,total_values):
        category= (udemy[i][6])
        list_category.append(category)
    total_categorias=[]
    for elemento in list_category:
        total_categorias.append(elemento)
    for elemento in total_categorias:
        while not total_categorias.count(elemento)==1:
            total_categorias.remove(elemento)


#TOPIC 4.1
#No hacemos lista de topics con fila, sino
#Matriz con los diferentes temas por categoría

#Matriz con los diferentes temas por categoría
    lista_temas_t=[]  #inicializamos lista
    for i in range (len(total_categorias)): # range de 0 a 14, por cada categoría (que son 14):
        temas_t=[] #va asignar una lista vacia ###al agarrar siguiente categoría se inicializa de nuevo
        for k in range(1,len(udemy)):  #por cada fila en 'udemy' sin contar encabezado:
            if udemy[k][6]==(total_categorias[i]):  #se va a 'udemy' fila k(va a pasar por todas) y columna 6(de categorias), si la categoría es igual a la que se esta evaluando .
                topic=udemy[k][8] #entonces se guarda el tema en una variable
                temas_t.append(topic) #y se agrega una lista
        for elemento in temas_t:  #una vez completada la lista para que los temas no se repitan, pasa por cada elemento
            if temas_t.count(elemento)>1:  #cuenta cuantas veces aparece en la lista y si el elemento se repite
                temas_t.remove(elemento) #entonces lo remueve hasta que quede solo uno
        lista_temas_t.append(temas_t) #entonces se guarda en lista principal #se hara una matriz
#ya tenemos lista con los diferentes temas, ahora falta contar cuantos son.
#Lista con cantidad de temas
    print("\nCUANTOS TEMAS HAY POR CATEGORÍA")
    cuenta_temas=[] #lista para contarlos
    for i in range(len(lista_temas_t)): #por cada fila en la matriz que formamos
        cuenta_temas.append(len(lista_temas_t[i])) #contara cuantos elementos tiene y los agregara en una lista

#Texto que dice los temas por categorias
    for i in range(len(total_categorias)):
        print ('La categoría', total_categorias[i], 'tiene', (cuenta_temas[i]), 'temas.')

#TOPIC 4.2
#GRAFICA TOPIC
    print("GRÁFICA DE BARRAS DE CANTIDAD DE TEMAS QUE HAY POR CATEGORÍA")
    import matplotlib.pyplot as plt
    ejex=total_categorias #categorias
    ejey=cuenta_temas  #cantidad de temas diferentes
    plt.title("Cantidad de temas por categoría")
    plt.bar(ejex, height=ejey, color="blue",width=0.5) #grafica de barras #'width es que tan anchas son las gráficas
    plt.ylabel("Cantidad de diferentes temas") 
    plt.xlabel("Categorías")
    plt.show()

def view5():

#INSTRUCTOR (SIGLAS-i) Columna:9
#Muestra el instructor de cada curso.
#OBJETIVO: Checar el instructor más común y su promedio de rating.

#INSTRUCTOR 5.1
#El instructor más común y cuantas veces aparece
    print("\nANÁLISIS DE LAS VECES QUE APARECE EL INSTRUCTOR MÁS COMÚN")
    total_values= int(len(udemy)) #Valores totales
    # Con esta podremos saber el instructor más común
    from statistics import mode 
    list_instructor=[]# creamos lista como antes
    for i in range(1,total_values):
        instructor= (udemy[i][9])
        list_instructor.append(instructor)
    ins_comun = mode(list_instructor) #Tenemos que definir la variable con el instructor más común. 


    count= 0
    for i in range(1, total_values): #por todas las filas
        instructor= (udemy[i][9])
        if instructor == str(ins_comun):
            count+=1
    print("El instructor más famoso es:", ins_comun, "aparece", count, "veces.")

#INSTRUCTOR 5.2
#Sacar el promedio de los raitings del instructor más común
    print("ANÁLISIS DEL PROMEDIO DEL RATING DEL INSTRUCTOR MÁS COMÚN")
    instructor_comun = ins_comun
    list_overall_ratings=[]  #Números de ratings se guardan en una lista
    for i in range(1,total_values):
        overall_ratings= (udemy[i][2])
        instructor= (udemy[i][9])
        if instructor == instructor_comun:
            list_overall_ratings.append(overall_ratings)
#Se obtiene el promedio.
    list_overall_ratings =[float(x) for x in list_overall_ratings]#convertir a float  
    suma= sum(list_overall_ratings)
    promedio = suma / len(list_overall_ratings)
    print("El promedio del rating de", instructor_comun, "es", promedio)


#INSTRUCTOR 5.3
#Obtener la gráfica de los resultados obtenidos.
    print("GRÁFICA DEL PROMEDIO DEL INTRUCTOR MÁS COMÚN")
    total_restante = float(5 - promedio)
    import matplotlib.pyplot as plt
    x = [promedio,total_restante]
    labels = ["Promedio de Ratings","Total\n(5 estrellas)"]

    fig, ax = plt.subplots()
    ax.pie(x, labels = labels, autopct='%0.0f%%')
    ax.set_title('Promedio de ratings del instructor más común')
    plt.show()


def view6():
#DURACIÓN (SIGLAS-d)
#RELACIÓN DEL PROMEDIO DE DURACIÓN Y PROMEDIO DE CALIFICACIONES TOTALES DE CATEGORIAS
#OBJETIVO:Sacar el promedio de duración de cada categoría, e incluso relacionarlo con las categorías con mejor calificación.

    total_values= int(len(udemy)) #Valores totales de udemy

    list_category=[]  #Lista con valores de categoría
    for i in range(1,total_values):
        category= (udemy[i][6])
        list_category.append(category)
    
    list_category = sorted(set(list_category)) #Se remueven las categorias repetidas
    print("\nANÁLISIS DEL PROMEDIO DE DURACIÓN POR CATEGORIA")


     
    lista_ans_d = []
    for i in range (len(list_category)): #por cada categoria
        duracion_d = [] #Se insertan los dígitos de duraciones, todos se encuentran en horas.
        for k in range(1,len(udemy)): #por cada fila en nuestros datos (sin contar encabezado):
            if udemy[k][6]==(list_category[i]): #Si es igual a nuestra lista de categoría
                duracion=udemy[k][15]   #Hacemos la variable con los valores de duraciones --- string
                duracion_d.append(duracion) #Se agregan los valores de duraciones a la lista.

        lenList = len(duracion_d) #Se cuentan los elementos de la lista
        sumList = sum(map(float, duracion_d)) #Se convierte a float y se suman los valores
                
        promedio = sumList/lenList #Se obtiene el promedio
        lista_ans_d.append(promedio) #Se obtiene la lista de promedios 
    #Se obtienen las horas promedio (duración) de cada categoría
    for i in range(len(list_category)):
        print ('La categoría', list_category[i], 'tiene un promedio de ', lista_ans_d[i], 'horas.')
    
    print("\nANÁLISIS DEL PROMEDIO DE CALIFICACIONES TOTALES POR CATEGORIA")
     
    lista_ans_ov = []
    for i in range (len(list_category)): 
        overal_rate_d = []
        for k in range(1,len(udemy)): #por cada fila en nuestros datos (sin contar encabezado):
            if udemy[k][6]==(list_category[i]): #Si es igual a nuestra lista de categoría
                overalrate=udemy[k][2]   #Hacemos la variable con los valores de calificaciones  --- string
                overal_rate_d.append(overalrate) #Se agregan los valores de calificaciones a la lista.
        lenList = len(overal_rate_d)  #Se cuentan los elementos de la lista
        sumList = sum(map(float, overal_rate_d))#Se convierte a float y se suman los valores

        promedio = sumList/lenList  #Se obtiene el promedio
        lista_ans_ov.append(promedio) #Se obtiene la lista de promedios 

    #Se obtiene el promedio de las calificaciones totales de cada categoría
    for i in range(len(list_category)):
        print ('La categoría', list_category[i], 'tiene un promedio de ', lista_ans_ov[i], 'calificación total.')

#GRÁFICA
# Hacer una gráfica con el eje y de duración de la categoria y eje x con su calificación.
    print("\nGRPAFICA DE DISPERSIÓN DE RELACIÓN ENTRE DURACIÓN Y CALIFICACIÓN")
    import matplotlib.pyplot as plt #se importa 
    ejey=lista_ans_d
    ejex=lista_ans_ov 
    plt.scatter(ejex,ejey, color="purple", s=10) #Usamos scatter para grafica de dispersión, 's' es el tamaño de punto
    plt.title("Relación de duración y calificación total de categorías.")
    plt.ylabel("Duración")
    plt.xlabel("Calificación Total")
    plt.show()


def view7():

#BESTSELLER (SIGLAS-b)
#Esta columna muestra si el curso es un bestseller (de los mejores vendidos).
#En valores de 'Yes' y 'No'

#Bestseller 5.1
#Lista con todos los valores bajo 'BESTSELLER' Columna:17
#lo sacamos de la misma forma que hicimos anteriormente
    print("\nTOTAL DE CURSOS QUE SON BESTSELLER")
    total_values= int(len(udemy)) 
    list_bestseller=[] 
    for i in range(1,total_values):
        bestseller= (udemy[i][17])
        list_bestseller.append(bestseller)

    count_b_Yes=list_bestseller.count('Yes')#cuenta los que si son bestsellers con .count
    count_b_No=list_bestseller.count('No') #cuenta los que no son bestsellers con .count, este lo usaremos para la gráfica
    print ('Hay un total de', count_b_Yes, 'cursos que son bestsellers') #despliega cuantos cursos son bestseller

#Bestseller 5.2
#GRAFICA (circular) BESTSELLER
#Porcentaje de los cursos que son bestseller y los que no
    print("GRÁFICA CIRCULAR DE CURSOS BESTSELLERS Y LOS QUE NO")
    import matplotlib.pyplot as plt
    cursos_b=[count_b_Yes,count_b_No]
    bestsellers=['BESTSELLER', 'NO bestseller']
    plt.title("Cursos bestseller y cursos no bestseller en Udemy")
    plt.pie(cursos_b, labels=bestsellers, autopct='%0.0f%%') #grafica circular como la anterior
    plt.show()

def view8():

#PRECIO (SIGLAS-p) Columna:18
#Esta columna muestra el precio de cada curso.
#Sacamos la lista de precios como lo hicimos anteriormente

    total_values= int(len(udemy)) 
    list_price=[]
    for i in range(1,total_values):
        price= float(udemy[i][18])
        list_price.append(price)

#Precio 6.1
#Se obtiene el promedio del precio para todos los cursos. 
    print("\nPROMEDIO DEL PRECIO PARA TODOS LOS CURSOS")
    promedio_p=sum(list_price)/(len(list_price)) #suma los elementos de la lista y los divide por cantidad de elementos en lista
    promedio_p=round(promedio_p,2) #redondeamos el promedio
    print('El precio promedio de todos los cursos de Udemy es de $',promedio_p,'dólares.') #despliega precio promedio de todos los cursos

#Precio 6.2
#Hago otra lista igual a la original de todos los precios, porque vamos a modificarla
    print("PRECIO MÁS COMPRADO POR LOS USUARIOS")
    lista_de_precios=[]
    for x in list_price:
        lista_de_precios.append(x)
#Hacemos lista con los diferentes precios que hay, pero que no se repitan
    for elemento in lista_de_precios: #por cada elemento en la lista que tiene precio por curso
        while not lista_de_precios.count(elemento)==1: #mientras no solo haya un mismo elemento en la lista
            lista_de_precios.remove(elemento) #se ira removiendo hasta solo quedar un unico elemento 
 #para tener los datos de forma ascendente
    lista_de_precios.sort() #para acomodar precios de forma ascendente

#para saber cuantos usuarios terminaron el curso segun el precio           
    usuarios_por_precios=[] #iniciamos lista
    for i in range (0,len(lista_de_precios)): #por cada precio
        precios_p=[] #se va a inicializar una lista vacia
        suma=0 #y el contador se va a inicializar en 0
        for k in range(1,len(udemy)): #despues desde la lista de 'udemy'
            if float(udemy[k][18])==(lista_de_precios[i]): #pasa por cada fila de udemy y si es igual a el precio:
                num=int(udemy[k][5]) #guarda lavariable de 'no. rating' correspondiente a la fila
                precios_p.append(num) #agrega variable en una lista
        suma=sum(precios_p)  #una vez que se agregaron todos los ratings, se suman       
        usuarios_por_precios.append(suma) #esa suma se agrega a una lista y se avanza con siguiente precio hasta acabar

    index_max_p=usuarios_por_precios.index(max(usuarios_por_precios)) #en que posición de la lista esta la mayor cantidad de usuarios 
    maximo_p= lista_de_precios[index_max_p] #a que precio corresponde ese indice
    print('El precio más comprado por los usuarios es de $', maximo_p, 'dólares.') #precio mas pagado, se confirma con gráfica

#Precio 6.3
#GRÁFICA PRICE
#eje y venga el número de personas que se inscribieron y eneje x el precio en dólares.
    print("GRAFICA DE LINEA DE NÚMERO DE PERSONAS QUE SE INSCRIBIERON RELACIONADO AL PRECIO")
    import matplotlib.pyplot as plt
    ejex=lista_de_precios 
    ejey=usuarios_por_precios
    plt.title("Número de personas que se inscribieron relacionado a precio")
    plt.plot(ejex, ejey, color="pink") #'plot' para una lista de linea normal
    plt.ylabel("Usuarios")
    plt.xlabel("Precios\n El precio de $128.98 fue el más comprado por la mayor cantidad de usuarios")
    plt.show()




while True:

    inserta = input("\n.............................................\nÍNDICE:\nTeclea ⇢ S para salir del programa. \nTeclea ⇢  1 para ver el análisis de Calificaciones generales.\nTeclea ⇢  2 para ver el análisis de Número de Calificaciones.\
\nTeclea ⇢  3 para ver el análisis de Categorías\nTeclea ⇢  4 para ver el análisis de Temas. \
\nTeclea ⇢  5 para ver el análisis del Instructor más común.\nTeclea ⇢  6 para ver el análisis de Duración de categorías . \
\nTeclea ⇢  7 para ver el análisis de Bestsellers.\nTeclea ⇢  8 para ver el análisis de Precios.\
\nTeclea ⇢  9 para ver el análisis completo.\nINSERTA ⇢  ").lower()
    print("..........................................................")
    if inserta == "s":
        print("╰┈➤ Gracias por pasar por nuestro proyecto, esperamos que vuelvas pronto * ˚ ✦")
        break
    elif inserta == "1":
        view1() 
    elif inserta == "2":
        view2()
    elif inserta == "3":
        view3()
    elif inserta == "4":
        view4()
    elif inserta == "5":
        view5()
    elif inserta == "6":
        view6()
    elif inserta == "7":
        view7()
    elif inserta == "8":
        view8()
    elif inserta == "9":
        view1(), view2(), view3(), view4(), view5(), view6(), view7(), view8() 
    else:
        print("No es una respuesta válida.")
     

#REFERENCIAS:
# Para TECLA 1 -- Referencia: S.A. (2019) "pyplot scatter plot marker size". Recuperado de: https://stackoverflow.com/questions/14827650/pyplot-scatter-plot-marker-size
# Para TECLA 3 -- Referencia:Auribox Training (2020). "Matplotlib (Parte 3): Gráficas de Pie (Pastel)" Recuperado de: https://www.youtube.com/watch?v=C3-CJPOJGbI&t=50s&ab_channel=AuriboxTraining
# Para TECLA 4 -- Referencia: Lisanny Andrés (2020)Python - Grafica de barras. Recuperado de: https://www.youtube.com/watch?v=hJ-E-iSyNcI&ab_channel=LisannyAndr%C3%A9s
# Para TECLA 5 -- Referencia: list, F. (2009). Most common element in a list. Recuperado de: https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
# Para TECLA 6 -- Referencia: Python, S., Rajbhandari, S., Rajbhandari, S., & Jenish, R. (2015). Sum of float numbers in a list in Python. Retrieved 14 October 2021, from https://stackoverflow.com/questions/31187194/sum-of-float-numbers-in-a-list-in-python?rq=1 
# Plot a pie chart in Python using Matplotlib - GeeksforGeeks. (2020). Retrieved 14 October 2021, from https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/ 