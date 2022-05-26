from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def HelloWorld(request):
    return HttpResponse("Hola mundo, estás en Django - Coderhouse primera vista")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.now()
        documentoDeTexto = f"Hoy es día: <br> {dia}"
        return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"
      return HttpResponse(documentoDeTexto)

def calc_anio_nac(self, edad):
    anio_en_curso = datetime.now().year
    anio_nac = anio_en_curso - int(edad)
    return HttpResponse(f"<br><br> Mi año de nacimiento es: {anio_nac}")

def probandoTemplate(self):

    miHtml = open("C:\\Users\\HP pavilion\\Documents\\APRENDE A PROGRAMAR\\Curso Python\\clase17\\NuevoP\\NuevoP\\plantillas\\template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)

    
