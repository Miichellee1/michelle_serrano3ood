
import json

agregar_cliente = True 
lista_pedidos=[]
datos=[]

def no_valido():
    print("***NO VALIDO***/intente nuevamente/n")
def pedidos():
       print(pedidos)
def no_disponible():
       print ("***NO DISPONIBLE***/intente nuevamente/n")


def menu_pedidos ():
        print(
     """
        lista_pedidos 
                       cantidad    valor 
        1.abono           50        1200
        2.tierra          35        1000
        3.lirio           40        1100
        4.Rosas Rojas     43        1700
        5.Margaritas      10        1100
        0.Salir 
                     """ )
 
print(
"""
         Epresa GreenGarden 
""")
    
while agregar_cliente: 
    lista_pedidos=[]

    print ("Ingressa datos de cliente:")

    nombre= input("nombre:")
    while not nombre.isalph():
             no_valido()
    nombre= input ("nombre:")
    
    telefono=input("telefono:")
    while not telefono.isdigital() or len (telefono)!=9:
            no_valido()
            telefono=input("telefono:")

            direccion=input("direccion:")
        
            agregar_compra=True
            valor_venta=0  

            while agregar_compra:
                menu_pedidos()
                productos= input("Ingrese numero de producto:")
   

                agregar_cliente=False
            while productos not in ['1','2','3','4','5','0']:
                no_disponible()

            productos= input("Ingrece numero de productos")
            unidades_productos=input("Unidades:")
            while not unidades_productos.isdigit()or int(unidades_productos)<0:
                no_valido()
            unidades_productos= input("unidades:")
            valor=int(productos)*1000
            valor_venta +=valor* int (unidades_productos)

            lista_pedidos.append({"""
             "codigo":int(productos)
             "unidad":int(unidades_productos)
              """})

            compra =input("Agregar compra:/1 si  /2 no")
            while compra not in ['1','2']:
              no_disponible()
              compra=input("Agregar compra: /1 si  /2 no")
              if compra =='2':
               cliente={
                "nombre":nombre,
                "telefono":telefono,
                "direccion":direccion,
                "procucto":lista_pedidos
 }

print (f"""
       ****** BOLETA*****
       ******************""")
for producto in lista_pedidos:
        print(f"producto{producto['codigo']}:{producto['unidad']}")
print(f"PRECIO FINAL:{valor_venta}$/n****************")
    
nuevo_cliente=input("Ingresar nuevo clienten:/1 si.  /2 no")
while nuevo_cliente not in['1','2']:
        no_disponible()
        nuevo_cliente=input("Ingresa nuevo cliente:/1 si  /no")
        if nuevo_cliente=='2':
            agregar_cliente = False 
            print ("/SALIENDO........")

print("programa finalisado")