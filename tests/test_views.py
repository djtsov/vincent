from django.test import TestCase
from core.models import TODOModel
from django.urls import reverse
from django.contrib.auth.models import User


class TODOViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        owner = User.objects.create_user(username='User1', password='1111')
        owner.save()
        todo = TODOModel.objects.create(owner=owner,
                                        title='Task1',
                                        description='some desc')
        todo.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('index'))
        self.assertRedirects(resp, '/accounts/login/?next=/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='User1', password='1111')
        self.assertTrue(login)
        resp = self.client.get(reverse('index'))
        print(resp)
        self.assertEqual(str(resp.context['user']), 'User1')
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'core/index.html')
