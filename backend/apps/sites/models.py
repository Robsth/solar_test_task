from django.db import models


class Site(models.Model):
    label = models.CharField('Название', max_length=150, null=False)
    url = models.URLField('Адрес', null=False)
    last_ping_date = models.DateTimeField('Дата последнего опроса', null=True)
    availability_status = models.BooleanField('Статус', default=False)

    def __str__(self):
        return self.label
