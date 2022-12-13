from django.db import models

class TensCis(models.Model):
    cargaExerc = models.IntegerField()
    nRebites = models.IntegerField()
    pRebites = models.IntegerField()
    dRebites = models.IntegerField()
