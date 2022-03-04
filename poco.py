x = [ [5,2,3], [10,8,9] ] 
#1.1
x[1] = [5,8,9]

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#1.2
estudiantes [0] = {'first_name':  'Michael', 'last_name' : 'Bryant'}


directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
#1.3
directorio_deportes['fútbol'] = ['Andres', 'Ronaldo', 'Rooney']
#me demoro demasiado notar que a futbol le faltaba una tilde y por eso no funcionaba
z = [ {'x': 10, 'y': 20} ]
#1.4
z = {'x': 10, 'y': 30}

print(x)
print(estudiantes)
print(directorio_deportes)
print(z)


#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
#En el directorio_deportes, cambia "Messi" por "Andrés".
#Cambia el valor 20 en z a 30.

#2
estudiantes1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(estudiantes1) 
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

def iterateDictionary(some_list)=

#Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista: