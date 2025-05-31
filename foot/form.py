from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        # getting rid of host and participants
        exclude = ['host', 'participants']  