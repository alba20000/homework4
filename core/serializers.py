from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core import models


class Staff(serializers.ModelSerializer):
    fio = serializers.SerializerMethodField()

    class Meta:
        model = models.Staff
        fields = '__all__'

    def get_fio(self, obj: models.Staff):
        return f'{obj.last_name} {obj.first_name} {obj.patronymic}'

    def validate(self, attrs: dict):
        if attrs['salary'] < 0:
            raise ValidationError('Зарплата должна быть положительным числом')
        return attrs
