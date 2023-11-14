from django.db import models

class Marca(models.Model):
    marca = models.CharField(max_length=6)

    def __str__(self):
        return self.marca


class Nivel(models.Model):
    nivel = models.CharField(max_length=100)

    def __str__(self):
        return self.nivel

class RevistaConsultor(models.Model):
    nomeRef = models.CharField(max_length=100)
    marca = models.ForeignKey('Marca',on_delete=models.CASCADE)
    ciclo = models.IntegerField()
    incioCiclo = models.DateField()
    fimCiclo = models.DateField()
    revista = models.FileField(upload_to="revistas-pdf")
    imagemRevista = models.ImageField(upload_to='imagens-revistas' , null=True, blank=True)
    def __str__(self):
        return self.nomeRef

class RevistaCasaEstilo(models.Model):
    nomeRef = models.CharField(max_length=100)
    marca = models.ForeignKey('Marca',on_delete=models.CASCADE)
    ciclo = models.IntegerField()
    incioCiclo = models.DateField()
    fimCiclo = models.DateField()
    revista = models.FileField(upload_to="revistas-pdf")
    imagemRevista = models.ImageField(upload_to='imagens-revistas' , null=True, blank=True)
    linkRevista = models.CharField(max_length=255)
    def __str__(self):
        return self.nomeRef

class RevistaAvon(models.Model):
    nomeRef = models.CharField(max_length=100)
    marca = models.ForeignKey('Marca',on_delete=models.CASCADE)
    ciclo = models.IntegerField()
    incioCiclo = models.DateField()
    fimCiclo = models.DateField()
    revista = models.FileField(upload_to="revistas-pdf")
    imagemRevista = models.ImageField(upload_to='imagens-revistas' , null=True, blank=True)
    linkRevista = models.CharField(max_length=255)
    def __str__(self):
        return self.nomeRef

class RevistaEspaco(models.Model):
    nomeRef = models.CharField(max_length=100)
    marca = models.ForeignKey('Marca',on_delete=models.CASCADE)
    ciclo = models.IntegerField()
    incioCiclo = models.DateField()
    fimCiclo = models.DateField()
    revista = models.FileField(upload_to="revistas-pdf")
    imagemRevista = models.ImageField(upload_to='imagens-revistas' , null=True, blank=True)
    linkRevista = models.CharField(max_length=255)
    def __str__(self):
        return self.nomeRef


class Banner(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens-banner')
    def __str__(self):
        return self.nome



class Combo(models.Model):
    nivel = models.ForeignKey('Nivel', on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    ciclo = models.IntegerField()
    imagemCombo = models.ImageField(upload_to='imagens-combos', null=True, blank=True)

    def __int__(self):
        return self.nivel
