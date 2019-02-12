from django.test import TestCase
from core.models import TODOModel
from django.contrib.auth.models import User


class TODOModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        owner = User.objects.create_user(username='User1', password='1111')
        owner.save()
        todo = TODOModel.objects.create(owner=owner,
                                        title='Task1',
                                        description='some desc')
        todo.save()

    def setUp(self):
        self.todo = TODOModel.objects.get(id=1)

    def test_title_required(self):
        field_required = self.todo._meta.get_field('title').null
        self.assertEquals(field_required, False)

    def test_description_unrequired(self):
        field_unrequired = self.todo._meta.get_field('description').null
        self.assertEquals(field_unrequired, True)

    def test_title_max_length(self):
        max_length = self.todo._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_description_max_length(self):
        max_length = self.todo._meta.get_field('description').max_length
        self.assertEquals(max_length, 300)
