# Uso de funciones incorporadas a  Python para
# el uso de cadenas. 

str1 = "Hay muchos lenguajes de Programacion raros: Ook, Piet, Befunge"

letras = 0
digitos = 0
espacios = 0

for i in str1:
   if i.isalpha():
      letras += 1
   if i.isdigit():
      digitos += 1
   if i.isspace():
      espacios += 1

print ("Hay", len(str1), "caracteres")
print ("Hay", letras, "caracteres alfabeticos")
print ("Hay", digitos, "digitos en la cadena")
print ("Hay", espacios, "espacios en la cadena")