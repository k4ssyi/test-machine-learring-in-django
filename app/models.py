from django.db import models


class Iris(models.Model):
    sepal_length = models.FloatField(verbose_name='がく片の長さ', default=0.0)
    sepal_width = models.FloatField(verbose_name='がく片の幅', default=0.0)
    petal_length = models.FloatField(verbose_name='花びらの長さ', default=0.0)
    petal_width = models.FloatField(verbose_name='花びらの幅', default=0.0)
    score = models.IntegerField(verbose_name='判定結果', null=False)
