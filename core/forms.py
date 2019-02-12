from django import forms
from . models import TODOModel
from django.utils import timezone


class TODOForm(forms.ModelForm):

    due_date = forms.CharField(
                    initial=timezone.now().strftime('%Y-%m-%d'),
                    widget=forms.TextInput(attrs={'type': 'date'})
                    )

    class Meta:
        model = TODOModel
        fields = ('title', 'description', 'due_date', 'priority')

    def __init__(self, *args, **kwargs):
        super(TODOForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-input'
