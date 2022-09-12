from django.db import models
from custom_user.models import CustomUser as cu

# Create your models here.

# Title: str
# Time / Date filed: datetime
# Description: str
# User who filed ticket: FK (Foreign Key)
# Status of ticket: str (New / In Progress / Done / Invalid)
# User assigned to ticket: FK (Foreign Key)
# User who completed the ticket: FK (Foreign Key)


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    created_by = models.ForeignKey(cu, on_delete=models.PROTECT, related_name='creator')
    assigned_to = models.ForeignKey(cu, null=True, on_delete=models.PROTECT, related_name='assigned')
    completed_by = models.ForeignKey(cu, default="", null=True, on_delete=models.PROTECT, related_name='completed')

    # Variables for ticket status choices
    NEW = "New"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    INVALID = "Invalid"
    
    STATUS_CHOICES = [
        (NEW, "New"),
        (IN_PROGRESS, "In Progress"),
        (DONE, "Done"),
        (INVALID, "Invalid"),
    ]
    ticket_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=NEW)

    def __str__(self):
        return self.title


# Sets default order of all tickets by datetime
Ticket.objects.order_by('datetime')
