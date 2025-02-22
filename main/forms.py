from django import forms
from main.models import Reservation

class ReservationForm(forms.ModelForm):

    date = forms.DateField(input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d.%m.%y'],
                           widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Your Date',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter a valid date'}),
                           )

    def clean_name(self):
        name = self.data['name']
        return name.title()


    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'email', 'count', 'date')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),

            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Your Phone'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'name': 'email',
                                            'placeholder': 'Your Email', 'data-rule': 'email',
                                            'data-msg': 'Please enter a valid email'}),

            'count': forms.NumberInput(attrs={'class': 'form-control', 'id': 'people',
                                              'placeholder': 'How many persons'}),
        }