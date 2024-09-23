# Defina la clase Automovil que contenga (al menos) los siguientes atributos:
# • patente (string)
# • marca (string)
# • kilometros_recorridos (float)
# • litros_nafta (float)
# La clase deberá proveer un constructor que permita inicializar los atributos, siendo obligatorios patente
# y marca. kilometros_recorridos y litros_nafta, se pueden especificar o no. Si no se especifican,
# se inicializarán por defecto en 0.
# La clase tendrá además un método llamado avanzar() que recibirá como argumento el número de
# kilómetros a conducir y sumará los kilómetros recorridos al valor del atributo kilometros_recorridos.
# El método también restará al valor de litros_nafta la cantidad consumida (se calcula el consumo de
# gasolina como 8.8 litros por cada 100 kms recorridos).
# La clase también contendrá otro método llamado cargar_nafta() que recibirá como argumento los
# litros introducidos que deberán sumarse a la variable litros_nafta.
# Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en la
# gasolina. En dicho caso, deberá mostrar el siguiente mensaje: "Es necesario cargar nafta para
# recorrer la cantidad indicada de kilómetros".

class Automovil(): 
    def __init__(self, patente: str,marca: str, kilometros_recorridos: float, litros_nafta: float ) -> None:
        self.patente = patente
        self.marca = marca
        self.kilometros_recorridos = kilometros_recorridos
        self.litros_nafta = litros_nafta
