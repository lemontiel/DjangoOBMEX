from django.db import models
from .extras.estados import EstadosCLV

class Institucion(models.Model):
    id_Institucion = models.IntegerField(primary_key=True,)
    nombre = models.CharField(max_length=30, blank=False,)
    email = models.EmailField(blank = True)
    rfc = models.CharField(max_length=16, null=True, blank = True,)
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE, blank = True)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, blank = True)
    pedido = models.ManyToManyField('Pedido', blank = True)
    contacto = models.ManyToManyField('Contacto', blank = True)
    def __str__(self):
        return str(self.nombre)

class Telefono(models.Model):
    id_Telefono = models.IntegerField(primary_key=True)
    lada = models.IntegerField(null = True, blank = True)
    numero = models.IntegerField(blank=False)
    extencion = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.numero)

class Pedido(models.Model):
    id_Pedido = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True, blank = False)
    tipoSilla = models.ForeignKey('Inventario', on_delete=models.CASCADE, blank = False)
    monto = models.FloatField(blank = False)
    def __str__(self):
        return str(self.id_Pedido)

class Contacto(models.Model):
    id_Contacto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=90, blank=False)
    apellidoM = models.CharField(max_length=45, blank = True)
    apellidoP = models.CharField(max_length=45, blank = True)
    cargo = models.CharField(max_length=30, null=True, blank = True)
    pedido = models.ManyToManyField('Pedido', blank = True)
    cursos = models.ManyToManyField('Curso', blank = True)
    comentarios = models.ManyToManyField('Comentario', blank = True)
    def __str__(self):
        return str(self.nombre + ' ' + self.apellidoP+' '+ self.apellidoM)

class Curso(models.Model):
    id_Curso = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=False, blank=False)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, blank = True)
    hora = models.TimeField(auto_now=True, blank = True)
    costo = models.FloatField(blank = True)
    instructor= models.CharField(max_length=130, blank=False)
    participantes = models.ManyToManyField('Contacto', blank = True)
    def __str__(self):
        return str(self.id_Curso)

class Inventario(models.Model):
    id_Producto = models.IntegerField(primary_key=True)
    generacion = models.IntegerField(blank = False, choices = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')), unique = True)
    existencias = models.IntegerField(blank = True)
    maxStock = models.IntegerField(blank = True)
    def __str__(self):
        return str(self.id_Producto)

class Direccion(models.Model):
    id_Direccion= models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=50, blank = True)
    numero = models.CharField(max_length=10, blank = True)
    entidad=models.CharField(max_length=30, blank = True)
    colonia=models.CharField(max_length=25, blank = True)
    delegacion = models.CharField(max_length=30, blank = True)
    pais = models.CharField(max_length=30, blank = True)
    numero_2=models.CharField(max_length=30, blank = True)
    entreCalle_1=models.CharField(max_length=30, blank = True)
    entreCalle_2=models.CharField(max_length=30, blank = True)
    estado = models.CharField(max_length = 2, choices = EstadosCLV.estados, blank = False)
    def __str__(self):
        return(str(self.estado+' '+self.calle + ' ' + self.numero))

class Comentario(models.Model):
    id_Comentario=models.IntegerField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True, blank = True)
    texto = models.TextField(blank=False)
    def __str__(self):
        return(str(self.id_Comentario))
