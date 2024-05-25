from django.db import models


class Staff(models.Model):
    first_name = models.CharField('Имя', max_length=40)
    last_name = models.CharField('Фамилия', max_length=40)
    patronymic = models.CharField('Отчество', max_length=40, blank=True)
    date_of_birth = models.DateField('Дата рождения')
    picture = models.ImageField('Фото сотрудника', upload_to='pictures', null=True, blank=True)
    salary = models.DecimalField('Заработная плата', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'
