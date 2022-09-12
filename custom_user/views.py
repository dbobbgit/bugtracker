from django.shortcuts import render
from .models import CustomUser
from tickets.models import Ticket

# Create your views here.
# auth = AUTH_USER_MODEL
def user_detail(req, user_id: int):
    user = CustomUser.objects.get(id=user_id)
    user_tickets = Ticket.objects.filter(created_by=user)
    assigned_to = Ticket.objects.filter(assigned_to=user)
    completed_tickets = Ticket.objects.filter(completed_by=user)
    # print(user_tickets[0].user) 
    return render(req, 'user_detail.html', {'user': user, 'tickets': user_tickets, 'assigned_to': assigned_to, 'completed_tickets': completed_tickets},)