from django.db import models


class guidemodel(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    location = models.CharField(max_length=40)
    status = models.CharField(max_length=40, default="", editable=True)

    def __str__(self):
        return self.mail
    class Meta:
        db_table = 'guide'


class upload(models.Model):
    placename = models.CharField(max_length=100)
    information = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.placename


