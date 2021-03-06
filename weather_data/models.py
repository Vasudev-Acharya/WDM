import django
from django.db import models

TYPECHOICE = (
    ('Tmin', 'Tmin'),
    ('Tmax', 'Tmax'),
    ('Tmean', 'Tmean'),
    ('Rainfall', 'Rainfall'),
    ('Sunshine', 'Sunshine'),
)

class Region(models.Model):
    initial = True
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    # owner = models.ForeignKey('auth.User', related_name='snippets')
    # highlighted = models.TextField()

    class Meta:
        managed = True
        db_table = 'Region'
        unique_together = (('name'),)

    def __unicode__(self):
        return "%s %s" % (self.id, self.name)

class Weather(models.Model):
    initial = True
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(
                                    'REGION',
                                    on_delete=models.CASCADE,
                                )
    value= models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=TYPECHOICE)
    month = models.CharField(max_length=10,default='NO DATA', editable=False)
    year = models.IntegerField(max_length=10, default='0000', editable=False)

    class Meta:
        managed = True
        db_table = 'Weather'
        unique_together = (('id', 'region', 'type','month', 'year'))

    def __unicode__(self):
        return "%s %s" % (self.id, self.region, self.value,self.type)