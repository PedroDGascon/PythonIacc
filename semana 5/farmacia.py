class Farmacia:

  def __init__(self, local_comercial, registradoras, pasillos, medicamentos):
    self.local_comercial = local_comercial
    self.registradoras = registradoras
    self.pasillos = pasillos
    self.medicamentos = medicamentos

  #Creacion de metodos
  def cadena_far(self):
        print("Que cadena de farmacia es?", self.local_comercial)
        print("Cuanto fue la venta del dia?",self.registradoras)
        print("La cantidad de pasillos en este local es de: ", self.pasillos)
  
  def vende_medicamentos(self):
        print("Que medicinas tienes disponibles en esta sucursal? ", self.medicamentos)
  
 # def __del__(self):
  #    print("Se ha destruido este objeto")  

class Farma_Zonal(Farmacia):
      def comunaFarm(self):
            print("La sucursal de ",self.local_comercial," ha sido movida a la comuna de maipu ")

farm_o = Farmacia("Salcobrand","350.000","Tres pasillos","retrovirales, vacunas")
farm_t = Farmacia("FarmaRebaja","150.000","Un solo pasillo","vitaminas, paracetamol")
  
#llamada al metodo 
farm_t.cadena_far()
farm_t.vende_medicamentos()


print("\n arriba esta el objeto inicial y abajo esta la herencia. \n") 


#Herencia aplicada, su nuevo metodo (comunaFarm) solo puede ser usado por ella y no por la clase padre.   
FarmaZona = Farma_Zonal("FarmaRebaja","500.000","Cinco Pasillos","vitaminas, paracetamol, proteinas, vacunas")
FarmaZona.comunaFarm()
FarmaZona.cadena_far()
FarmaZona.vende_medicamentos()





