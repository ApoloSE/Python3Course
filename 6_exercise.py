# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas 
# vendidos en el último pedido y calcule el peso total del paquete que será enviado.

#payaso .112
#muñeca .075

p = input('Numero de payasos: ')
m = input('Numero de muñecas: ')
p = int(p)
m = int(m)
pp = 112*p
pm = 75*m

print(f'Peso total: {pp+pm} gramos')