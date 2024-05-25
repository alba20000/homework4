from django.test import TestCase, Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.staff = models.Staff.objects.create(
            id='1',
            first_name='Иван',
            last_name='Иванов',
            patronymic='Иванович',
            date_of_birth='1999-01-01',
            salary='1000'
        )

    def test_list(self):
        response = self.client.get('/staff_model/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(f'/staff_model/{self.staff.id}/')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        person = {
            'first_name': 'Петр',
            'last_name': 'Петров',
            'patronymic': 'Петрович',
            'date_of_birth': '1999-02-02',
            'salary': '2000',
        }
        response = self.client.post('/staff_model/', person)
        self.assertEqual(response.status_code, 201)

    def test_update(self):
        person = {
            'first_name': 'Петр',
            'last_name': 'Петров',
            'patronymic': 'Петрович',
            'date_of_birth': '1999-02-02',
            'salary': '2000',
        }
        response = self.client.put('/staff_model/1/', person, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_partial_update(self):
        person = {
            'salary': '2000',
        }
        response = self.client.patch('/staff_model/1/', person, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete('/staff_model/1/')
        self.assertEqual(response.status_code, 204)
