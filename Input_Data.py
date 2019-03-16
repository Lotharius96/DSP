#HERE GOES THE CODE 
import numpy as np
import sys, os
import matplotlib as mpl
import scipy as sp
#####_DEFINICION__DE_VARIABLES####
Path_DirA='Muestra_Vocales/Muestras_A/'
Path_DirE='Muestra_Vocales/Muestras_E/'
Path_DirI='Muestra_Vocales/Muestras_I/'
Path_DirO='Muestra_Vocales/Muestras_O/'
Path_DirU='Muestra_Vocales/Muestras_U/'
#####Direccion_Muestras_AUDIO#####

class Estructuras(Vocales):



class Vocales:
    My_data={}
    New_datos={} # diccionario que contine las nuevas muestras
    counter=0
    ###carga la lista de ficheros#####
  def __init__(self,Path):
    self.Path=Path
    self.y=os.listdir(Path)
    ##y=[]
   
    ##convierte los parametros_de entrada   
  def Get_Input():
       #dir_var=Path
       for i in y:
         dir_var=Path+i
         #obtiene la frecuencia de muestreo de la señal y datos
         fs, data=wavfile.read(dir_var)
         #L=len(data)
         My_data[str(counter)]=data
         counter=counter+1
    counter=0
    ####se_cargan_todas_las_muestras###
   #elimina los silecios de las muestras y las deja mas pura
  def New_Data():
      Index_Init=0 #define los indices de recorte infereior
      Index_Final=0 #define el limite superior de las Muestras
      for i in range(0,19):
        Temp=My_data[str(i)]
        while abs(Temp[counter])<250:
          counter=counter+1
        Index_Init=counter
        counter=0
        while abs(Temp(len(Temp)-1-counter)):
          counter=counter+1
          u=len(Temp)-1-counter   
        Index_Final=u
        New_datos[str(i)]=Temp[Index_Init:Index_Final]
    ###################################
  def FFt_M():
        for i in range(0,19):
         Haming_Window=np.hamming(2000)
         L=len(New_datos[str(i)])
         z=int(L/2000)
          for j in range()
         #New_datos[str(i)]=New_datos[str(i)]*Haming_Window #hace el ventaneo de la señal de python


#for j=1:Z 
 #  x=Vector((j-1)*div+1:(j)*div);
 #  p=12; % p que minimiza el error, energia del error
  # r=zeros(p+1,1);%Funciones de correolacion (filas,columnas)
  # for k=0:p % La sumatoria de n=0 hasta 512-k de x(n)x(n+k)
  #  r(k+1)=x(1:(512-k))'*x((k+1):512);%Correlacion, la segunda traspuesta por la primera
  # end
  # R(:,1)=r(1:p);%Matriz
  # for i=2:p%Construccion de la matriz de autocorrelacion
   # R(:,i)=[R(i,1);R(1:p-1,i-1)];%Columna 
  #end
   #r=r(2:p+1);%termino independiente
   #a=-inv(R)*r;%Filtro
   #Coef(j,:)=a.';
#end

  def Coff():

    #def __init__(self,data):
