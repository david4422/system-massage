from django.urls import path
from . import views

urlpatterns = [
    # write message
    path('sendMessage/', views.sendMessage),

    # Get all messages for a specific user
    path('inbox', views.inbox),
    path('unread-inbox', views.unread_inbox),
    path('readMessage/<int:id>', views.readMessage),
    path('deleteMessage/<int:id>', views.deleteMessage),
]
