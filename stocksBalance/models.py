from django.db import models


class Nemos(models.Model):
    nemo = models.CharField(max_length=50)
    # Field name made lowercase.
    lastprice = models.CharField(db_column='lastPrice', max_length=50)
    # Field name made lowercase.
    registerdatetime = models.DateTimeField(db_column='registerDateTime')

    class Meta:
        managed = False
        db_table = 'nemos'
