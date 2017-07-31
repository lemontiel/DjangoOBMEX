from django.db import models
from .extras.estados import EstadosCLV

class Institucion(models.Model):
    id_Institucion = models.AutoField(primary_key=True,)
    nombre = models.CharField(max_length=30, blank=False,)
    email = models.EmailField(blank = True)
    rfc = models.CharField(max_length=16, null=True, blank = True,)
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE, null=True, blank = True)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, null=True, blank = True)
    # pedido = models.OneToOneField('Pedido',on_delete=models.CASCADE, blank = True)
    # contacto = models.ForeignKey('Contacto',blank = True)
    def __str__(self):
        return str(self.nombre)

class Telefono(models.Model):
    id_Telefono = models.AutoField(primary_key=True)
    lada = models.IntegerField(null = True, blank = True)
    tipo = models.CharField(blank=False, max_length=7)
    numero = models.CharField(blank=False, max_length=13)
    extencion = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.numero)

class Pedido(models.Model):
    id_Pedido = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True, blank = False)
    hora = models.TimeField(auto_now=True, blank = False)
    cantidad = models.IntegerField(blank = False, null = False, default=0)
    tipoSilla = models.ForeignKey('Inventario', on_delete=models.CASCADE, blank = False)
    monto = models.FloatField(blank = False)
    contacto = models.ForeignKey("Contacto", on_delete=models.CASCADE)
    institucion= models.ForeignKey("Institucion", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_Pedido)

class Contacto(models.Model):
    id_Contacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=90, blank=False)
    apellidoP = models.CharField(max_length=45, blank = False)
    apellidoM = models.CharField(max_length=45, blank = False)
    cargo = models.CharField(max_length=30, null=True, blank = True)
    telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE, null=True, blank = False)
    email = models.EmailField(blank = False)
    institucion = models.ForeignKey("Institucion", on_delete=models.CASCADE)
    # pedido = models.OneToOneField('Pedido', on_delete=models.CASCADE, blank = True)
    cursos = models.ManyToManyField('Curso', blank = True)
    comentarios = models.ManyToManyField('Comentario', blank = True)
    def __str__(self):
        return str(self.nombre + ' ' + self.apellidoP+' '+ self.apellidoM)

class Curso(models.Model):
    id_Curso = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, blank = True, null=True)
    hora = models.TimeField(auto_now=False, blank = False)
    costo = models.FloatField(blank = False)
    instructor= models.CharField(max_length=130, blank=False)
    participantes = models.ManyToManyField('Contacto', blank = True)
    def __str__(self):
        return str(self.id_Curso)

class Inventario(models.Model):
    id_Producto = models.AutoField(primary_key=True)
    generacion = models.IntegerField(blank = False, choices = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')), unique = True)
    existencias = models.IntegerField(blank = True)
    maxStock = models.IntegerField(blank = True)
    def __str__(self):
        return str(self.id_Producto)

class Direccion(models.Model):
    id_Direccion= models.AutoField(primary_key=True)
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
    id_Comentario=models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True, blank = True)
    texto = models.TextField(blank=False)
    def __str__(self):
        return(str(self.id_Comentario))
