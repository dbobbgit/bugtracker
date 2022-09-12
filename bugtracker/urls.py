"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from custom_user import views as cu
from auth import views as auth
from tickets import views as tview
from dashboard import views as db


urlpatterns = [
    path('', tview.index, name='home'),
    path('test_ticket/', tview.index, name='test-ticket'),
    path('newticket/', tview.create_ticket_view, name='newticket'),
    path('ticket/<int:ticket_id>/', tview.ticket_detail, name='ticket-detail'),
    path('editticket/<int:ticket_id>/', tview.edit_ticket_detail, name='edit-ticket-detail'),
    path('user/profile/<int:user_id>/', cu.user_detail, name='user-detail'),
    path('in_progress/<int:ticket_id>/', db.in_progress_detail, name='in-progress'),
    path('done/<int:ticket_id>/', db.done_detail, name='done'),
    path('invalid/<int:ticket_id>/', db.invalid_detail, name='invalid'),
    path('login/', auth.login_view, name='login'),
    path('signup/', auth.signup_view, name='signup'),
    path('logout/', auth.user_logout, name='logout'),
    path('admin/', admin.site.urls),
]
