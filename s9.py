from datetime import date

#clase empleado
class Empleado:
    aumentarId = 0
    def __init__(self, nombr='', sueld=0, fechaIngre=''):
        self.__id = Empleado.aumentarId
        self.nombre = nombr
        self.sueldo = sueld
        self.fechaIngreso = fechaIngre
        Empleado.aumentarId += 1
    
    def mostrarEmpleado(self):
        print(self.__id)
        print(self.nombre)
        print(self.sueldo)
        print(self.fechaIngreso)

#clase departamento
class Departamento:
    aumentarId = 0
    def __init__(self, emple='', descr=''):
        self.__id = Departamento.aumentarId
        self.empleado = emple
        self.descripcion = descr
        Departamento.aumentarId += 1
    
    def mostrarDepartamento(self):
        print(self.__id)
        print(self.descripcion)

#clase empresa
class Empresa:
    aumentarId = 0
    def __init__(self, depar='', emple='', direc='', telef='', razonSocia='', ruc=''):
        self.__id = Empresa.aumentarId
        self.departamento = depar
        self.empleado = emple
        self.direccion = direc
        self.telefono = telef
        self.razonSocial = razonSocia
        self.ruc = ruc
        Empresa.aumentarId += 1
    
    def mostrarEmpresa(self):
        print(self.__id)
        print(self.direccion)
        print(self.telefono)
        print(self.razonSocial)
        print(self.ruc)

#clase obrero
class Obrero(Empleado):
    aumentarId = 0
    def __init__(self, nombr='', sueld=0, fechaIngre='', sindi=False, contrColec=False):
        super().__init__(nombr, sueld, fechaIngre)
        self.__id = Obrero.aumentarId
        self.sindicato = sindi
        self.contratoColectivo = contrColec
        Obrero.aumentarId += 1
    
    def mostrarObrero(self):
        print(self.__id)
        print(self.sindicato)
        print(self.contratoColectivo)

#clase administrativo
class Administrativo(Empleado):
    aumentarId = 0
    def __init__(self, nombr='', sueld=0, fechaIngre='', comis=False):
        super().__init__(nombr, sueld, fechaIngre)
        self.__id = Administrativo.aumentarId
        self.comision = comis
        Administrativo.aumentarId += 1
    
    def mostrarAdministrativo(self):
        print(self.__id)
        print(self.comision)

#clase prestamo
class Prestamos:
    aumentarId = 0
    def __init__(self, fecha=0, valor=0, numerPago=0, emple='', estad=False):
        self.__id = Prestamos.aumentarId
        self.fecha = fecha
        self.valor = valor
        self.numPagos = numerPago
        if self.numPagos == 0: self.cuota = 0  # Cuando numeroPagos sea == 0 evita el error.
        else: self.cuota = round((self.valor/self.numPagos), 2)
        self.empleado = emple
        self.saldo = self.cuota * self.numPagos
        self.estado = estad
        Prestamos.aumentarId += 1
    
    def mostrarPrestamos(self):
        print(self.__id)
        print(self.fecha)
        print(self.valor)
        print(self.numPagos)
        print(self.cuota)
        print(self.saldo)
        print(self.estado)

#clase sobretiempo
class Sobretiempo:
    aumentarId = 0
    def __init__(self, horasRecar=0, horasExtra=0, emple='', fecha=0, estad=False):
        self.__id = Sobretiempo.aumentarId
        self.horasRecargo = horasRecar
        self.horasExtraordinarias = horasExtra
        self.empleado = emple
        self.fecha = fecha
        self.estado = estad
        Sobretiempo.aumentarId += 1

    def sobretiempo(self, sueldo=0):
        valor_hora = sueldo/240
        return round((valor_hora*(self.horasRecargo*0.50+self.horasExtraordinarias*2)), 2)

    def mostrarSobretiempo(self):
        print(self.__id)
        print(self.horasRecargo)
        print(self.horasExtraordinarias)
        print(self.fecha)
        print(self.estado)

#clase deducciones
class Deducciones:
    aumentarId = 0
    def __init__(self, comis=0, antig=0):
        self.__id = Deducciones.aumentarId
        self.iess = round((float(input('Porcentaje iess: %')) / 100), 4)
        self.comision = comis
        self.antiguedad = antig
        Deducciones.aumentarId += 1
    
    def mostrarDeducciones(self):
        print(self.__id)
        print(self.iess)
        print(self.comision)
        print(self.antiguedad)

#clase nomina
class Nomina:
    aumentarId = 0
    def __init__(self, emple='', fecha=0, sueld=0, sobreTiemp='', comis=0, antig=0, iess=0, prest=''):
        self.__id = Nomina.aumentarId
        self.empleado = emple
        self.fecha = fecha
        self.sueldo = sueld
        self.sobretiempo = sobreTiemp
        self.sobretiempoCalc = sobreTiemp.sobretiempo(self.sueldo)
        self.comision = round((comis*self.sueldo), 2)
        self.antiguedad = self.CalAntiguedad(antig, self.fecha, self.empleado.fechaIngreso, self.sueldo)
        self.iess = round((iess*(self.sueldo+self.sobretiempoCalc)), 2)
        self.prestamo = prest
        self.prestamoEmpleado = self.prestamo.cuota
        self.totIng = self.sueldo + self.sobretiempoCalc + self.comision + self.antiguedad
        self.totDes = self.iess+self.prestamoEmpleado
        self.liquidoRecibir = round((self.totIng-self.totDes), 2)
        Nomina.aumentarId += 1

    def CalAntiguedad(self, antig=0, fechNom=0, fechIng=0, suel=0):
        calculoFech = fechNom - fechIng
        calculoFechas = calculoFech.days
        return round((antig*calculoFechas/365*suel), 2)

    def mostrarNomina(self):
        print(self.__id)
        print(self.fecha)
        print(self.sueldo)
        print(self.comision)
        print(self.antiguedad)
        print(self.totIng)
        print(self.iess)
        print(self.totDes)
        print(self.liquidoRecibir)



emple = Administrativo("Harold Caicedo", 1450.50, date(2021, 9, 7), True)
empre = Empresa(Departamento(emple, "Departamento de quejas"), emple, "Canton Milagro", "0942470980", "Generar reportes", "25425562231")
validacionEmpleados = isinstance(emple, Administrativo)
if validacionEmpleados:
    if emple.comision:
        comis = round((float(input("Porcentaje de comision: %"))/100), 4)
        deduc = Deducciones(comis=comis)
    else:
        deduc = Deducciones()
else:
    antigued = float(input("Ingresar el cargo por la antiguedad: "))
    deduc = Deducciones(antig=antigued)
hacerSobre = input("El empleado hizo sobretiempo [yes]  [no]: ")
if hacerSobre == "yes":
    sobre_tiemp = Sobretiempo(2, 6, emple, date(2021, 9, 7), True)
else:
    sobre_tiemp = Sobretiempo(emple=emple)
hacerPrest = input("El empleado hizo un prestamo [yes] | [no]: ")
if hacerPrest == "yes":
    prest = Prestamos(date(2021, 9, 20), 350, 5, emple, True)
else:
    prest = Prestamos(emple=emple)

nomin = Nomina(empre.empleado, date(2021, 7, 28), emple.sueldo, sobre_tiemp, deduc.comision, deduc.antiguedad, deduc.iess, prest)

print("")
print("MOSTRAR EMPRESA")
empre.mostrarEmpresa()
print("")
print("MOSTRAR EMPLEADO")
emple.mostrarEmpleado()
# print("")
# print("MOSTRAR EMPLEADO OBRERO")
# emple.mostrarObrero()
print("")
print("MOSTRAR EMPLEADO ADMINISTRATIVO")
emple.mostrarAdministrativo()
print("")
print("MOSTRAR EMPLEADO DEPARTAMENTO")
empre.departamento.mostrarDepartamento()
print("")
print("MOSTRAR SOBRETIEMPO")
sobre_tiemp.mostrarSobretiempo()
print("")
print("MOSTRAR DEDUCCIONES")
deduc.mostrarDeducciones()
print("")
print("MOSTRAR PRESTAMOS")
prest.mostrarPrestamos()
print("")
print("MOSTRAR NOMINA")
nomin.mostrarNomina()
print("")
