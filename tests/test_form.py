from django.test import TestCase
from django.utils import timezone
from core.forms import TODOForm


class RenewBookFormTest(TestCase):

    def test_renew_form_date_field_label(self):
        form = TODOForm()
        initial = form.fields['due_date'].initial
        self.assertTrue(initial, timezone.now().strftime('%Y-%m-%d'))
