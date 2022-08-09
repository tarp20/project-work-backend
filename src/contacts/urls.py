from django.urls import path

from .views import ContactIdView,ContactListView

urlpatterns = [
    path('contacts/<int:pk>/', ContactIdView.as_view()),
    path('contacts/', ContactListView.as_view())

]
