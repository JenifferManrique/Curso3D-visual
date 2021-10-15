
from django.shortcuts import render, HttpResponse
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from .models import grupo, cliente, proveedor, producto
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
from django.contrib.auth.mixins import LoginRequiredMixin

class grupolistar(ListView):
    model = grupo
    template_name = 'mantenimientos/grupolistar.html'

class grupoguardar(CreateView):
    model = grupo
    fields = ['gruponombre','grupoanulado']
    template_name = 'mantenimientos/grupoguardar.html'
    success_url = reverse_lazy('grupolistar')

class grupomodificar(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = grupo
    fields = ['gruponombre', 'grupoanulado']
    template_name = 'mantenimientos/grupomodificar.html'
    success_url = reverse_lazy('grupolistar')

def hello_pdf(request):
     #Cree el objeto HttpResponse con los encabezados de PDF adecuados.
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = 'attachment; filename=hello.pdf'

     # Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
     p = canvas.Canvas(response)

     # Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
     # Consulte la documentación de ReportLab para obtener la lista completa de funciones.
     p.drawString(100, 100, "Hello world.")

     # Cierre el objeto PDF limpiamente y listo.
     p.showPage()
     p.save()
     return response

def grupos_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   categorias = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Grupos", styles['Heading1'])
   categorias.append(header)
   headings = ('Id', 'Grupo', 'Activo')
   if not pk:
      todosgrupos = [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.all().order_by('pk')]
   else:
      todosgrupos = [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.filter(id=pk)]
   t = Table([headings] + todosgrupos)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   categorias.append(t)
   doc.build(categorias)
   response.write(buff.getvalue())
   buff.close()
   return response

######################CLIENTE################################

class clientelistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = cliente
    template_name = 'mantenimientos/clientelistar.html'

class clienteguardar(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = cliente
    fields = ['clientecedula','clientenombre','clientetelefono','clienteanulado']
    template_name = 'mantenimientos/clienteguardar.html'
    success_url = reverse_lazy('clientelistar')

class clientemodificar(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = cliente
    fields = ['clientecedula', 'clientenombre', 'clientetelefono', 'clienteanulado']
    template_name = 'mantenimientos/clientemodificar.html'
    success_url = reverse_lazy('clientelistar')

def cliente_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   lista = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Cliente", styles['Heading1'])
   lista.append(header)
   headings = ('Id', 'Cedula', 'Nombre','Telefono','Activo')
   if not pk:
      todosclientes = [(p.id, p.clientecedula, p.clientenombre, p.clientetelefono, p.clienteanulado)
                         for p in cliente.objects.all().order_by('pk')]
   else:
      todosclientes = [(p.id, p.clientecedula, p.clientenombre, p.clientetelefono, p.clienteanulado)
                         for p in cliente.objects.filter(id=pk)]
   t = Table([headings] + todosclientes)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   lista.append(t)
   doc.build(lista)
   response.write(buff.getvalue())
   buff.close()
   return response

###################Proveedor##########################

class proveedorlistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = proveedor
    template_name = 'mantenimientos/proveedorlistar.html'

class proveedorguardar(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = proveedor
    fields = ['proveedorcedula','proveedornombres','proveedortelefono','proveedoranulado']
    template_name = 'mantenimientos/proveedorguardar.html'
    success_url = reverse_lazy('proveedorlistar')

class proveedormodificar(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = proveedor
    fields = ['proveedorcedula', 'proveedornombres', 'proveedortelefono', 'proveedoranulado']
    template_name = 'mantenimientos/proveedormodificar.html'
    success_url = reverse_lazy('proveedorlistar')

def proveedor_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   listaproveedor = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Proveedores", styles['Heading1'])
   listaproveedor.append(header)
   headings = ('Id', 'Cedula', 'Nombre','Telefono','Activo')
   if not pk:
      todosproveedor = [(p.id, p.proveedorcedula, p.proveedornombres, p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.all().order_by('pk')]
   else:
      todosproveedor = [(p.id, p.proveedorcedula, p.proveedornombres, p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.filter(id=pk)]
   t = Table([headings] + todosproveedor)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   listaproveedor.append(t)
   doc.build(listaproveedor)
   response.write(buff.getvalue())
   buff.close()
   return response

###########################Producto############################

class productolistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = producto
    template_name = 'mantenimientos/productolistar.html'

class productoguardar(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = producto
    fields = ['productogrupo','productonombre','productopreciovta','productocodigo','productoexistencia','productoanulado']
    template_name = 'mantenimientos/productoguardar.html'
    success_url = reverse_lazy('productolistar')

class productomodificar(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    model = producto
    fields = ['productogrupo', 'productonombre', 'productopreciovta', 'productocodigo', 'productoexistencia',
              'productoanulado']
    template_name = 'mantenimientos/productomodificar.html'
    success_url = reverse_lazy('productolistar')

def producto_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   listaproducto = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Productos", styles['Heading1'])
   listaproducto.append(header)
   headings = ('Id', 'grupo', 'producto','precio','Código','existencia','estado')
   if not pk:
      todosproductos = [(p.id, p.productogrupo, p.productonombre, p.productopreciovta, p.productocodigo, p.productoexistencia, p.productoanulado)
                         for p in producto.objects.all().order_by('pk')]
   else:
      todosproductos = [(p.id, p.productogrupo, p.productonombre, p.productopreciovta, p.productocodigo, p.productoexistencia, p.productoanulado)
                         for p in producto.objects.filter(id=pk)]
   t = Table([headings] + todosproductos)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))


   listaproducto.append(t)
   doc.build(listaproducto)
   response.write(buff.getvalue())
   buff.close()
   return response