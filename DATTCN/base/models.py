from django.db import models

# Create your models here.
class Quanhuyen(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return f"{self.name}"

class Xaphuong(models.Model):
    name = models.CharField(max_length=200, null=True)
    fkquanhuyen = models.ForeignKey(Quanhuyen,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.name}"

class Duongpho(models.Model):
    name = models.CharField(max_length=200, null=True)
    fkxaphuong = models.ForeignKey(Xaphuong,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.name}"

class Duan(models.Model):
    name = models.CharField(max_length=200, null=True)
    fkduongpho = models.ForeignKey(Duongpho,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"{self.name}"

