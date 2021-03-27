import re
"""
Programa realizado por:
-Gaspar Melchor Caamal Aban
-Miguel Aurelio Oxte Tzuc
-Jesus Reyes Tuz Acosta
"""
#El programa solo busca por declaracion de una sola linea.
#VAR = <TIPO> OPERADOR <TIPO>
print("Programa realizado por:")
print("-Gaspar Melchor Caamal Aban")
print("-Miguel Aurelio Oxte Tzuc")
print("-Jesus Reyes Tuz Acosta")
print("-----------------------------")
salir = False
while salir == False:
    while True:
        #Por cada expresion se abre y se cierra el archivo.
        filename='archivo.txt'
        textfile=open(filename, "r")
        #Expresion para buscar el tipo de dato
        #Tipo de dato INT
        regex = "int\s"
        reg = re.compile(regex)
        for line in textfile:
            #Se inicializa el contador en 0
            resultint = 0
            resultint = len(reg.findall(line))
        textfile.close()
        filename = "archivo.txt"
        textfile = open(filename, "r")
        #Tipo de dato DOUBLE
        regex = "double\s"
        reg = re.compile(regex)
        for line in textfile:
            #Se inicializa el contador en 0
            resultdouble = 0
            resultdouble = len(reg.findall(line))
        textfile.close()
        filename = "archivo.txt"
        textfile = open(filename, "r")
        #Tipo de dato STRING
        regex = "string\s"
        reg = re.compile(regex)
        for line in textfile:
            #Se inicializa el contador en 0
            resultstring = 0
            resultstring = len(reg.findall(line))
        textfile.close()
        filename = "archivo.txt"
        textfile = open(filename, "r")
        #Tipo de dato BOOLEAN
        regex = "boolean\s"
        reg = re.compile(regex)
        for line in textfile:
            #Se inicializa el contador en 0
            resultboolean = 0
            resultboolean = len(reg.findall(line))
        textfile.close()
        #Se inicia el ciclo para la validacion de INT
        if resultint >= 1:
            filename = "archivo.txt"
            textfile = open(filename, "r")
            #EXPRESION REGULAR PARA VALIDAR ENTEROS
            regex = "(int\s[\w(\w\d)]+\s?\=\s?[\d|\w]+\s?[\+|\*|\-|\/]\s?[\d|\w]+;)|(int\s[\w(\w\d)]+\s?\=\s?[\d|\w]+;)|(int\s[\w(\w\d)]+;)"
            reg = re.compile(regex)
            for line in textfile:
                #Se inicializa el contador en 0
                intvalor = 0
                intvalor = len(reg.findall(line))
                if intvalor >= 1:
                    print("Ejecucion exitosa")
                else:
                    print("Error 'Asignacion de tipo INT incorrecta' ")
            textfile.close()
            salir = True
            break
        #Se inicia el ciclo para la validacion de DOUBLE
        if resultdouble >= 1:
            filename = "archivo.txt"
            textfile = open(filename, "r")
            #EXPRESION REGULAR PARA VALIDAR REALES
            regex2 = "(double\s[\w(\w\d)]+\s?\=\s?[\d\.\d|\w]+\s?[\+|\*|\-|\/]\s?[\d\.\d|\w]+;)|(double\s[\w(\w\d)]+\s?\=\s?[\d\.\d|\w]+;)|(double\s[\w(\w\d)]+;)"
            reg = re.compile(regex2)
            for line in textfile:
                doublevalor = 0
                doublevalor = len(reg.findall(line))
                if doublevalor >= 1:
                    print("Ejecucion exitosa")
                else:
                    print("Error 'Asignacion de tipo DOUBLE incorrecta' ")
            textfile.close()
            salir = True
            break
        #Se inicia el ciclo para la validacion de STRING
        if resultstring >= 1:
            filename = "archivo.txt"
            textfile = open(filename, "r")
            #EXPRESION REGULAR PARA VALIDAR CADENAS
            #regex3 = "(^string\s\w+\s\=\s\"((\w+\s\w+){1,10})\"\;$)|(^string\s\w+\;$)|(^\w+\s\=\s\"((\w+\s\w+){0,10})\"\;$)|(^\w+\s\=\s\"((\w+\s\w+){0,10})\"\s[+]\s\"((\w+\s\w+){0,10})\"\;$)|(^string\s\w+\s\=\s\"((\w+\s\w+){0,10})\"\s[+]\s\"((\w+\s\w+){1,10})\"\;$)"
            regex3 = "(string\s[\w(\w\d)]+\s?\=\s?\"[\w\W]+\"[\s?\+\s?\"[\w\W]+\"]*;)|(string\s[\w(\w\d)]+\s?\=\s?\"[\w\W]+\";)|(string\s[\w(\w\d)]+;)"
            reg = re.compile(regex3)
            for line in textfile:
                stringvalor = 0
                stringvalor = len(reg.findall(line))
                if stringvalor >= 1:
                    print("Ejecucion exitosa")
                else:
                    print("Error 'Asignacion de tipo STRING incorrecta' ")
            textfile.close()
            salir = True
            break
        #Se inicia el ciclo para la validacion de BOOLEAN
        if resultboolean >= 1:
            filename = "archivo.txt"
            textfile = open(filename, "r")
            #EXPRESION REGULAR PARA VALIDAR OPERADORES LOGICOS
            regex4 = "(^boolean\s\w+\s\=\strue\;$)|(^boolean\s\w+\s\=\s\d+\s(<|>|<=|>=)\s\d+\;$)|(^boolean\s\w+\;\n^[a-z]+\s\=\s\d+\s(<|>|<=|>=)\s\d+\;$)|(^boolean\s\w+\;\n^[a-z]+\s\=\strue\;$)"
            reg = re.compile(regex4)
            for line in textfile:
                booleanvalor = 0
                booleanvalor = len(reg.findall(line))
                if booleanvalor >= 1:
                    print("Ejecucion exitosa")
                else:
                    print("Error 'Asignacion de tipo BOOLEAN incorrecta' ")
            textfile.close()
            salir = True
            break