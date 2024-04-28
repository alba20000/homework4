from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self) -> str:
        return self.name


class Clients(models.Model):
    first_name = models.CharField('Имя', max_length=40)
    last_name = models.CharField('Фамилия', max_length=40)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Goods(models.Model):
    FRUITS = {
        '1': 'Груша',
        '2': 'Банан',
        '3': 'Киви',
    }
    order_id = models.BigAutoField(primary_key=True)
    fruit = models.CharField(max_length=3, choices=FRUITS)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return f'№{self.order_id} - {self.FRUITS[self.fruit]}'
