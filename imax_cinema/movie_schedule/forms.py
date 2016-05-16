from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'pricing',
            'number_of_regular_tickets',
            'number_of_student_tickets',]
        widgets = {
            'number_of_regular_tickets': forms.NumberInput(attrs={
                'class': 'ticketing',
            }),
            'number_of_student_tickets': forms.NumberInput(attrs={
                'class': 'ticketing',
            }),
            # 'pricing': forms.RadioSelect(),
        }