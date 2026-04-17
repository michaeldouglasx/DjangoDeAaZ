from ..models import *
from .State import State

class City(models.Model):
    state = models.ForeignKey(State, related_name='state', on_delete=models.SET_NULL, null=True)
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.state.name)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

