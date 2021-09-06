
from _typeshed import Self


class modelo_negocio:
    def __init__(self,nom,totdes,ced,prestamoE,sobreti,toti,ape,dir,sal,valorH,comisionE,liqR,ieesE):
        self.nombre=nom
        self.valor_hora = valorH
        self.cedula=ced
        self.apellido=ape
        self.direccion=dir
        self.salario=sal
        self.comisionEm=comisionE
        self.ieesEmpleado=ieesE
        self.liquidoR=liqR
        self.toti=toti
        self.sobreti=sobreti
        self.prestamoE=prestamoE
        self.totdes=totdes
    def empresa(self):
        print("empresa:¨{}ruc:{}".format(self.nombre,self.direccion))
    def sueldo(self):
        print
    def totdes(self):
        print

    def empleador(self):
        print(self.nombre,self.cedula,self.direccion)

class empleadoEmpresa(modelo_negocio):
    def __init__(self,contrato,nom,ced):
        super().__init__(self,nom,dir,ced,contrato)
        self.__contrato=contrato

    @property
    def contrato(self):
        return self.__contrato
    @contrato.setter
    def contrato(self,value):
        if value:
            self.__contrato = value
        else:
            self.__contrato= 'sin contrato'
        self.__contrato=value
    
    def mostarmodelo_negocio(self):
        print(self.nombre)


#empleadoEmpresa=empleadoEmpresa("comisariato",1102125624,"9 de octubre")
#empleadoEmpresa.mostra()
class nomina:

    def __init__(self,codigo,antiEmp,sueldohora,deducionCo,comisionEmp,toting,prestamoE,sueldo,hrDiurnas,sobreti,deducionies,deducionAn,totdes,iessE,hrNocturnas):
        self.codigo=codigo
        self.hrDiurnas=hrDiurnas
        self.antiEmp=antiEmp
        self.comisioneEmp=comisionEmp
        self.toting=toting
        self.hrNocturnas=hrNocturnas
        self.ieesE=iessE
        self.deducionAn=deducionAn
        self.totdes=totdes
        self.deducionies=deducionies
        self.sobreti=sobreti
        self.sueldo=sueldo
        self.prestamoE=prestamoE
        self.deducionCo=deducionCo
        self.antiguedad=antiEmp
        self.sueldohora=sueldohora






    def getcodigo(self):
        return self.codigo
    def getHrDiurnas(self):
        return self.hrDiurnas
    def getHrNocturnas(self):
        return self.hrNocturnas
    def getiessE(self):
        return self.iessE
    def gettotdes(self):
        return self.totdes
    def getpretamoE(self):
        return self.prestamoE
    def getdeducionAn(self):
        return self.deducionAn
    def getdeducionies(self):
        return self.deducionies
    def getsobreti(self):
        return self.sobreti
    def gettoting(self):
        return self.toting
    def getcomisionEmp(self):
        return self.comisioneEmp
    def getantiguedad(self):
        return self.antiEmp
    def getdeduccionCo(self):
        return self.deducionCo
    def getsueldo(self):
        return self.sueldo






    def getTOTAL(self):
        total= self.getHrDiurnas()*500 + self.getHrNocturnas()* 500 *0.90
        total= total-(total* 00.7)
       
    def gettotdes(self):
        totdes= self.getiessE+self.getpretamo
        print(totdes)
    def getdeducionAn(self):
        self.iessE=self.deducionies*(self.sueldo+self.sobreti)
    def getsaldo(self):
        self.sueldo= self.sueldo

    def getoting(self):
        self.getotingtoting=self.getpretamoE+self.getcomisionEmp+self.getantiguedad
    def getcomision(self):
        self.getcomisionEmpcomision = self.getdeduccionCo*self.getsueldo

    # def mostarNomina(self):
        print("codigo de empleado:"+self.getcodigo()+"salario mensual: "+str(self.getTOTAL()))
        

    # codigo= input("ingrese codigo de empleado:")
    # hrDiurnas=input("ingrese cantidad de horas diurnas:")
    # hrNocturnas=input("ingrese cantidad la hora nocturna:")

    # #e=nomina(codigo,hrDiurnas,hrNocturnas)
    # #e.mostraNomina

class SistemaPago(Self):
    def pago (self):
        pass
    def saldo(self):
        pass
class pago_nomina(SistemaPago):
    def pago(self):
        return "pago por tarjeta"
    def saldo(self):
        return " saldo a paga por nomina"
    def __init__(self,nombre):
        self.nombre = nombre

    def pago_contado(self,contato):
        return contato.pago()

    SistemaPago=SistemaPago()
    print(SistemaPago.pago())
    
    exit



