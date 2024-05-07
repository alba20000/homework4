#Запросы

In [3]: models.Animal.objects.all()
Out[3]: <QuerySet [<Animal: Бобер>, <Animal: Карп>, <Animal: Игуана>, <Animal: Медведь>, <Animal: Енот>]>

In [4]: list(models.Animal.objects.all())
Out[4]:
[<Animal: Бобер>,
 <Animal: Карп>,
 <Animal: Игуана>,
 <Animal: Медведь>,
 <Animal: Енот>]

In [5]: models.Animal.objects.first()
Out[5]: <Animal: Бобер>

In [6]: models.Animal.objects.last()
Out[6]: <Animal: Енот>

In [7]: models.Animal.objects.count()
Out[7]: 5

In [8]: models.Animal.objects.order_by('name')
Out[8]: <QuerySet [<Animal: Бобер>, <Animal: Енот>, <Animal: Игуана>, <Animal: Карп>, <Animal: Медведь>]>

In [9]: models.Animal.objects.order_by('-name')
Out[9]: <QuerySet [<Animal: Медведь>, <Animal: Карп>, <Animal: Игуана>, <Animal: Енот>, <Animal: Бобер>]>

In [10]: models.Animal.objects.filter(name__contains='р')
Out[10]: <QuerySet [<Animal: Бобер>, <Animal: Карп>]>

In [11]: models.Animal.objects.filter(name__exact='Карп')
Out[11]: <QuerySet [<Animal: Карп>]>

In [12]: models.Staff.objects.all()
Out[12]: <QuerySet [<Staff: Шишкин Василий>, <Staff: Мушкин Петр>]>

In [13]: models.Staff.objects.filter(salary__gt=1000)
Out[13]: <QuerySet [<Staff: Мушкин Петр>]>

In [15]: models.Staff.objects.latest('date_of_birth')
Out[15]: <Staff: Шишкин Василий>

In [16]: models.Staff.objects.get(id=1)
Out[16]: <Staff: Шишкин Василий>

In [17]: models.Goods.objects.all()
Out[17]: <QuerySet [<Goods: №1 - Груша>, <Goods: №2 - Банан>, <Goods: №3 - Киви>, <Goods: №4 - Груша>, <Goods: №5 - Банан>]>

In [20]: models.Goods.objects.filter(fruit='1')
Out[20]: <QuerySet [<Goods: №1 - Груша>, <Goods: №4 - Груша>]>

In [22]: models.Staff.objects.dates('date_of_birth', 'day')
Out[22]: <QuerySet [datetime.date(1963, 9, 11), datetime.date(1988, 1, 24)]>

In [23]: models.Staff.objects.dates('date_of_birth', 'day').reverse()
Out[23]: <QuerySet [datetime.date(1988, 1, 24), datetime.date(1963, 9, 11)]>

In [25]: models.Clients.objects.values('first_name', 'phone_number')
Out[25]: <QuerySet [{'first_name': 'Иван', 'phone_number': '88005553535'}, {'first_name': 'Александр', 'phone_number': '89999999999'}]>

In [27]: models.Goods.objects.values_list('fruit', flat=True)
Out[27]: <QuerySet ['1', '2', '3', '1', '2']>

In [28]: models.Goods.objects.get(order_id=4)
Out[28]: <Goods: №4 - Груша>

In [29]: models.Animal.objects.exclude(name__contains='б')
Out[29]: <QuerySet [<Animal: Карп>, <Animal: Игуана>, <Animal: Медведь>, <Animal: Енот>]>

In [30]: models.Goods.objects.filter(order_id=6).exists()
Out[30]: False

In [31]: models.Clients.objects.create(first_name='Михаил', last_name='Сушкин', phone_number='89321477337')
Out[31]: <Clients: Михаил Сушкин>

In [32]: models.Clients.objects.filter(last_name='Иванович').update(last_name='Иванов')
Out[32]: 1

In [34]: models.Goods.objects.get(order_id=5).delete()
Out[34]: (1, {'core.Goods': 1})
