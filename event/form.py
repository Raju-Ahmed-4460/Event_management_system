from django import forms
from event.models import Event,Category,Participant


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border p-2 w-full',
                'placeholder': 'Enter event name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'border p-2 w-full',
                'placeholder': 'Enter description'
            }),

            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'border p-2 w-full'
            }),

            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'border p-2 w-full'
            }),

            'location': forms.TextInput(attrs={
                'class': 'border p-2 w-full',
                'placeholder': 'Enter location'
            }),

            'category': forms.Select(attrs={
                'class': 'border p-2 w-full'
            }),
        }


        

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border p-2 w-full',
                'placeholder': 'Enter category name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'border p-2 w-full',
                'placeholder': 'Enter description',
                'rows': 3
            }),
        }





class ParticipantModelForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border p-2 w-full',
                'placeholder': 'Enter participant name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'border p-2 w-full',
                'placeholder': 'Enter email'
            }),

            'events': forms.CheckboxSelectMultiple()
        }
