from django.db import models

class ModelUser(models.Model) :
    m_idx = models.IntegerField()
    id = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    nickname =  models.CharField(max_length=15)
    team = models.SmallIntegerField()
    email = models.EmailField()
    