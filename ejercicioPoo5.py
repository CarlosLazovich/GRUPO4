"""
Gestión de Donaciones
Nos piden que diseñemos un programa para gestionar donaciones de alimentos.
Los productos tienen los siguientes atributos:
   Nombre
   Cantidad

Tenemos dos tipos de productos:
   Perecedero: tiene un atributo llamado días a caducar.
   No perecedero: tiene un atributo llamado tipo

Tendremos una función llamada Calcular, que según cada clase hará una cosa u
otra, a esta función se le envía la cantidad por producto y entidades a las cuáles
se entregarán donaciones 
   Debe obtener la cantidad que se enviará a cada entidad, sabiendo que la
   distribución debe ser lo más equitativa posible. En caso que sobren
   productos, se almacenan para el próximo ciclo de donación
   Además si el producto es perecedero, se informará:
     Si le queda menos de 10 días para caducar
     ,la entrega debe hacerse en el día actual.
     Si le queda 1 mes para caducar
     ,la entrega debe hacerse en el plazo de 1 semana

Si fuera No Perecedero, se informa cuántos productos se entregarán por
entidad y que queda libre la elección de la fecha de entrega siempre que no
supere el mes.

"""


class Producto:
    def __init__(self,nombre,cantidad_total):
        self.nombre = nombre
        self.cantidad_total = cantidad_total

    def calcular(self,cantidad_a_donar, *args): # args se usa cuando queremos poner muchos argumentos
        if cantidad_a_donar <= self.cantidad_total:
            cantidad_por_entidad = cantidad_a_donar // len(args) # dividimos para cada institucion
            sobrante = cantidad_a_donar % len(args) # el sobrante
            print(f'Para cada entidad se destinara {cantidad_por_entidad} unidades.')
            print(f'Sobraron {sobrante} unidades para la proxima donacion')
        else:
            print(f'cantidad insuficiente. Solo tenes {self.cantidad_total} de unidades')




class Perecedero(Producto):
    def __init__(self,nombre,cantidad_total,dias_a_caducar):
        super(). __init__(nombre, cantidad_total)
        self.dias_a_caducar = dias_a_caducar

    def calcular(self, cantidad_a_donar, *args):
        super().calcular(cantidad_a_donar, *args) 
        if self.dias_a_caducar < 10:
            print(f'Le quedan {self.dias_a_caducar} dias para caducar. Tenes que donarlo hoy')   
        elif self.dias_a_caducar < 30:
            print(f'Te quedan {self.dias_a_caducar} dias. Te queda una semana para donarlo')
        else:
            print(f'Te quedan {self.dias_a_caducar} dias')


class NoPerecedero(Producto):
    def __init__(self, nombre, cantidad_total,tipo):
        super().__init__(nombre, cantidad_total)
        self.tipo = tipo

    def calcular(self, cantidad_a_donar, *args):
        super().calcular(cantidad_a_donar, *args)
        print('Tenes un plazo de un mes para donar')    




producto1 = Perecedero('Leche',20,25)
producto2 = NoPerecedero('Arroz',10,'Granos')

producto1.calcular(10,'comedos 123','hogar de niñas','merendero la hora feliz')

producto2.calcular(3,'comedos 123','hogar de niñas','merendero la hora feliz')

