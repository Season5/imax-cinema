from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'number_of_regular_tickets',
            'number_of_student_tickets',]