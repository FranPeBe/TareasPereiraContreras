# La funcion retornar_numero tiene un condicional para cada número del
# 0 al 99 donde si el parámetro coincide con el número este retorna el
# nombre del número en un string.
""" Se agrega un error de sangría a la hora de colocar un comentario
    No se respeta el espaciado entre el # y la primera letra del comentario"""


def retornar_numero(c):

    "No se respeta el espaciado entre el operador."
    if c == 1:
        f = "uno"
    elif c == 0:
        f = "cero"
    elif c == 2:
        f = "dos"
    elif c == 3:
        f = "tres"
    elif c == 4:
        f = "cuatro"
    elif c == 5:
        f = "cinco"
    elif c == 6:
        f = "seis"
    elif c == 7:
        f = "siete"
    elif c == 8:
        f = "ocho"
    elif c == 9:
        f = "nueve"
    elif c == 10:
        f = "diez"
    elif c == 11:
        f = "once"
    elif c == 12:
        f = "doce"
    elif c == 13:
        f = "trece"
    elif c == 14:
        f = "catorce"
    elif c == 15:
        f = "quince"
    elif c == 16:
        f = "dieciséis"
    elif c == 17:
        f = "diecisiete"
    elif c == 18:
        f = "dieciocho"
    elif c == 19:
        f = "diecinueve"
    elif c == 20:
        f = "veinte"
    elif c == 21:
        f = "veintiuno"
    elif c == 22:
        f = "veintidos"
    elif c == 23:
        f = "veintitres"
    elif c == 24:
        f = "veinticuatro"
    elif c == 25:
        f = "veinticinco"
    elif c == 26:
        f = "veintiseis"
    elif c == 27:
        f = "veintisiete"
    elif c == 28:
        f = "veintiocho"
    elif c == 29:
        f = "veintinueve"
    elif c == 30:
        f = "treinta"
    elif c == 31:
        f = "treinta y uno"
    elif c == 32:
        f = "treinta y dos"
    elif c == 33:
        f = "treinta y tres"
    elif c == 34:
        f = "treinta y cuatro"
    elif c == 35:
        f = "treinta y cinco"
    elif c == 36:
        f = "treinta y seis"
    elif c == 37:
        f = "treinta y siete"
    elif c == 38:
        f = "treinta y ocho"
    elif c == 39:
        f = "treinta y nueve"
    elif c == 40:
        f = "cuarenta"
    elif c == 41:
        f = "cuarenta y uno"
    elif c == 42:
        f = "cuarenta y dos"
    elif c == 43:
        f = "cuarenta y tres"
    elif c == 44:
        f = "cuarenta y cuatro"
    elif c == 45:
        f = "cuarenta y cinco"
    elif c == 46:
        f = "cuarenta y seis"
    elif c == 47:
        f = "cuarenta y siete"
    elif c == 48:
        f = "cuarenta y ocho"
    elif c == 49:
        f = "cuarenta y nueve"
    elif c == 50:
        f = "cinceunta"
    elif c == 51:
        f = "cinceunta y uno"
    elif c == 52:
        f = "cinceunta y dos"
    elif c == 53:
        f = "cinceunta y tres"
    elif c == 54:
        f = "cinceunta y cuatro"
    elif c == 55:
        f = "cinceunta y cinco"
    elif c == 56:
        f = "cinceunta y seis"
    elif c == 57:
        f = "cinceunta y siete"
    elif c == 58:
        f = "cinceunta y ocho"
    elif c == 59:
        f = "cinceunta y nueve"
    elif c == 60:
        f = "sesenta"
    elif c == 61:
        f = "sesenta y uno"
    elif c == 62:
        f = "sesenta y dos"
    elif c == 63:
        f = "sesenta y tres"
    elif c == 64:
        f = "sesenta y cuatro"
    elif c == 65:
        f = "sesenta y cinco"
    elif c == 66:
        f = "sesenta y seis"
    elif c == 67:
        f = "sesenta y siete"
    elif c == 68:
        f = "sesenta y ocho"
    elif c == 69:
        f = "sesenta y nueve"
    elif c == 70:
        f = "setenta"
    elif c == 71:
        f = "setenta y uno"
    elif c == 72:
        f = "setenta y dos"
    elif c == 73:
        f = "sesenta y tres"
    elif c == 74:
        f = "setenta y cuatro"
    elif c == 75:
        f = "setenta y cinco"
    elif c == 76:
        f = "setenta y seis"
    elif c == 77:
        f = "setenta y siete"
    elif c == 78:
        f = "setenta y ocho"
    elif c == 79:
        f = "setenta y nueve"
    elif c == 80:
        f = "ochenta"
    elif c == 81:
        f = "ochenta y uno"
    elif c == 82:
        f = "ochenta y dos"
    elif c == 83:
        f = "ochenta y tres"
    elif c == 84:
        f = "ochenta y cuatro"
    elif c == 85:
        f = "ochenta y cinco"
    elif c == 86:
        f = "ochenta y seis"
    elif c == 87:
        f = "ochenta y siete"
    elif c == 88:
        f = "ochenta y ocho"
    elif c == 89:
        f = "ochenta y nueve"
    elif c == 90:
        f = "noventa"
    elif c == 91:
        f = "noventa y uno"
    elif c == 92:
        f = "noventa y dos"
    elif c == 93:
        f = "noventa y tres"
    elif c == 94:
        f = "noventa y cuatro"
    elif c == 95:
        f = "noventa y cinco"
    elif c == 96:
        f = "noventa y seis"
    elif c == 97:
        f = "noventa y siete"
    elif c == 98:
        f = "noventa y ocho"
    elif c == 99:
        f = "noventa y nueve"
    return f


# num_to_string
def num_to_str(c):
    if type(c) == str:  # Verifica que el parámetro no sea tipo string
        return -8  # Caso contrario devuelve el error -8
    f = ""
    if c not in range(0, 100):  # Verifica que el número esté entre el 0 y 99
        return -9   # Caso contrario devuelve el error -9

    f = retornar_numero(c)  # Invoca la función retornar_número

    return f  # Se retorna el string final


# string_work
def string_work(texto):

    # Revisa que el parámetro es tipo string
    if type(texto) != str:
        return -10  # Caso contrario retorna el error -10

    """ Verifica que todos los caracteres del parámetro texto sean parte del
     abecedario. Cada for evalua cada caracter en ASCII; si uno coincide
     con el número establecido en el rango significa que el caracter no
     pertenece al abecedario y retorna el error -11."""
    for x in range(len(texto)):

        for y in range(65):
            if ord(texto[x]) == y:
                return -11

        for z in range(91, 97):
            if ord(texto[x]) == z:
                return -11

        for j in range(166, 209):
            if ord(texto[x]) == j:
                return -11

        for k in range(210, 241):
            if ord(texto[x]) == k:
                return -11

        for n in range(242, 256):
            if ord(texto[x]) == n:
                return -11

    # Cada caracter del parámetro se revisa si es mayúscula o minúscula
    newtex = ""
    for i in range(len(texto)):

        # En caso de ser mayúscula se cambia la letra por la minúscula.
        # Se agrega la letra ya cambiada al str "newtex".
        if texto[i].isupper():
            newtex += texto[i].lower()

        # En caso de ser minúscula se cambia la letra por la mayúscula.
        # Se agrega la letra ya cambiada al str "newtex".
        elif texto[i].islower():
            newtex += texto[i].upper()

    return newtex  # Se retorna el string final


# Prueba que verifica que el parámetro del string_work esté en el abecedario y
# que logre cambiar las mayúsculas por minúsculas y vicesersa.
def test_string_work_1():
    a = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    b = "abcdefghijklmnñopqrstuvwxyz"
    assert string_work(a) == b  # Verifica cambio de mayúsculas
    assert string_work(b) == a  # Verifica cambio de minúsculas


# Revisa que cuando el parámetro del string_work sea un número retorne el
# error correcto de -10.
def test_string_work_2():
    assert string_work(2) == -10


# Revisa que cuando el parámetro del string_work sea un string con símbolos
# o números retorne el error correcto de -11.
def test_string_work_3():
    assert string_work("2@Jk;?") == -11


# Revisa que todos los números del 0 al 99 tengan su respectivo nombre en
# string.
def test_num_to_str_1():
    for x in range(0, 100):
        f = ""
        f = retornar_numero(x)
        assert num_to_str(x) == f


# Verifica que cuando el parámetro de num_to_string sea un string retorne el
# error correcto de -8.
def test_num_to_str_2():
    assert num_to_str("1") == -8


# Verifica que cuando el parámetro de num_to_string sea un número que no
# pertenece al intervalo de 0 a 99 o/y no sea entero positivo retorne el
# error correcto de -9.
def test_num_to_str_3():
    assert num_to_str(100) == -9
    assert num_to_str(1.2) == -9
    assert num_to_str(-1) == -9
