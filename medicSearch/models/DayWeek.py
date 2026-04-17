from ..models import *

class DayWeek(models.Model):
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Dia da Semana'
        verbose_name_plural = 'Dias da Semana'