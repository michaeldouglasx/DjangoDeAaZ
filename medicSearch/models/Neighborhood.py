from ..models import *
from .City import City

class Neighborhood(models.Model):
    city = models.ForeignKey(City, null=True, related_name='city', on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'neighborhood'
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'