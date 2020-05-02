from django.db import models


class Vertice(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length= 45, blank=False, null=False)

    class Meta:
        verbose_name = "Vertice"
        verbose_name_plural= "Vertices"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Arista(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length= 45, blank=False, null=False)

    class Meta:
        verbose_name = "Arista"
        verbose_name_plural= "Aristas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Grafo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length= 45, blank=False, null=False)
    tipo = models.CharField(max_length= 45, blank=False, null=False)
    vertices_id=models.ManyToManyField(Vertice)
    aristas_id=models.ManyToManyField(Arista)

    class Meta:
        verbose_name = "Grafo"
        verbose_name_plural= "Grafos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre