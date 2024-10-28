from django.db import models



class urun(models.Model):
    CINSIYET_CHOICES = [
        ('K', 'Kız'),
        ('E', 'Erkek'),
    ]
    urunid = models.CharField(max_length = 10)
    urunad = models.CharField(max_length = 50)
    cinsiyet = models.CharField(max_length = 1 ,choices=CINSIYET_CHOICES , default='E')
    uruntur = models.CharField(max_length=50)

    
    def __str__(self):
        return f"urun ad: {self.urunad} urun id: {self.urunid} urun turu: {self.uruntur} urun cinsiyet: {self.cinsiyet}"

class UrunImage(models.Model):
    urun = models.ForeignKey(urun, on_delete=models.CASCADE)  # Urun modeliyle ilişkilendir
    image = models.ImageField(upload_to='urun_images/')
    def __str__(self): 
        return f"urun img: {self.image}"

# Create your models here.
