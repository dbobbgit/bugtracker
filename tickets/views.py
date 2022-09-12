from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from custom_user.models import CustomUser
from bugtracker.settings import AUTH_USER_MODEL
from auth.forms import SignUpForm, LoginForm
from .models import Ticket
from .forms import TicketAddForm, TicketEditForm
# Create your views here.

@login_required
def index(request):
    """Basic Home Page with Ticket List View - Might Turn Into Dashboard"""
    tickets = Ticket.objects.all()
    return render(request, "index.html", {"tickets": tickets, },)

@login_required
def create_ticket_view(request):
    """Ticket Creation View"""
    if request.method == "POST":
        form = TicketAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                created_by=request.user,
                assigned_to=None,
            )
            return HttpResponseRedirect(reverse("home"))
    form = TicketAddForm()
    return render(request, "form.html", {"form": form})

@login_required
def ticket_detail(request, ticket_id):
    """Ticket Detail View"""
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, "ticket_detail.html", {"ticket": ticket})

@login_required
def edit_ticket_detail(request, ticket_id: int):
    """Ticket Edit View"""
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = TicketEditForm(request.POST, instance=ticket)
        form.save()
        return HttpResponseRedirect(reverse("home"))
    
    form = TicketEditForm()
    return render(request, "form.html", {"form": form})

