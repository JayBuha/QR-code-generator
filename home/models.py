from django.db import models

# Create your models here.
class qrcode(models.Model):
    name = models.CharField(max_length=150)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return str(self.name)