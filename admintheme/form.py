from django.forms import ModelForm, CharField
from admintheme.models import Instance, User

class InstanceForm(ModelForm):
    class Meta:
        model = Instance
        fields = '__all__'

class UserForm(ModelForm):
    email = CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'last_name', 'first_name']
        labels = {
            'first_name': 'Apellidos',
            'last_name': 'Nombre',
            'email': 'E-Mail'
        }
        help_texts = {
            'username': '',
        }
