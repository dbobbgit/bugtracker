# Ticket In-progress, Done, Invalid - HTTPResponseRedirect Reverse to ticket detail
# In-progress: ticket.status = ticket.assignee(request.user)
# Done: ticket.status = ticket.assignee = None
# Closer: ticket.closer = request.user
# Invalid: ticket.status = assignee = None, ticket.status("Invalid")
# ticket.save()
# set-up ticket detail template
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from tickets.models import Ticket


def invalid_detail(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = "Invalid"
    ticket.assigned_to = None
    ticket.save()

    return HttpResponseRedirect(reverse('home'))


def in_progress_detail(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = "In Progress"
    ticket.assigned_to = request.user
    ticket.save()

    return HttpResponseRedirect(reverse('ticket-detail', args=[ticket_id],))


def done_detail(request, ticket_id: int):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = "Done"
    ticket.assigned_to = None
    ticket.completed_by = request.user
    ticket.save()

    return HttpResponseRedirect(reverse('home'))
