class Empleado:
    def __init__(self, id, nombre, sueldo, fecha_ingreso):
        self.__id = id
        self.__nombre = nombre
        self.__fecha_ingreso = fecha_ingreso
        self.__sueldo = sueldo

    def mostrar_empleado(self):
        pass


class Empresa:
    def __init__(self, departamento, empleado, direccion, telefono, razon_social, ruc):
        self.__direccion = direccion
        self.__empleado = empleado
        self.__departamento = departamento
        self.__telefono = telefono
        self.__razon_social = razon_social
        self.__ruc = ruc

    def mostrar(self):
        pass


class Deduccion:
    def __init__(self, less, comision, antiguiedad):
        self.__less = less
        self.__comision = comision
        self.__antiguiedad = antiguiedad

    def deducciones(self, less, comision, antiguiedad):
        pass

    def mostrar(self):
        pass


class Nomina:
    def __init__(
        self,
        id,
        empleado,
        fecha,
        sueldo,
        sobretiempo,
        comision,
        antiguiedad,
        total,
        iess,
        prestamo,
        total_descuento,
        liquidacion_recibir,
    ):
        self.__id = id
        self.__empleado = empleado
        self.__fecha = fecha
        self.__sueldo = sueldo
        self.__sobretiempo = sobretiempo
        self.__comision = comision
        self.__antiguiedad = antiguiedad
        self.__total = total
        self.__iess = iess
        self.__prestamo = prestamo
        self.__total_descuento = total_descuento
        self.__liquidacion_recibir = liquidacion_recibir

    def nomina_empleado(empleado, fecha, sueldo):
        pass

    def sobre_tiempo():
        pass

    def mostrar():
        pass


class Prestamo:
    def __init__(self, fecha, valor, numero_pago, cuota, id, empleado, saldo, estado):
        self.__fecha = fecha
        self.__valor = valor
        self.__numero_pago = numero_pago
        self.__cuota = cuota
        self.__id = id
        self.__empleado = empleado
        self.__saldo = saldo
        self.__estado = estado

    def prestamo():
        pass

    def mostrar(self):
        pass


class Sobretiempo:
    def __init__(
        self, horas_recargo, horas_extraordinarias, empleado, fecha, id, estado
    ):
        self.__horas_recargo = horas_recargo
        self.__horas_extraordinarias = horas_extraordinarias
        self.__empleado = empleado
        self.__fecha = fecha
        self.__id = id
        self.__estado = estado

    def sobretiempo():
        pass

    def mostrar(self):
        pass


class Administratvo:
    def __init__(self, comision):
        self.__comision = comision

    def mostrar(self):
        pass


class Obrero:
    def __init__(self, sindicato, contrato_sindicato):
        self.__sindicato = sindicato
        self.__contrato_sindicato = contrato_sindicato

    def obrero(self):
        pass

    def mostrar(self):
        pass


class Departamento:
    def __init__(self, empleado, id, descpcion):
        self.__empleado = empleado
        self.__id = id
        self.__descpcion = descpcion

    def departamento(self):
        pass

    def mostrar(self):
        pass
