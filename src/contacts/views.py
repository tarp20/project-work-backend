from django.db.models import Value 
from django.db.models.functions import Substr, StrIndex

from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactSerializer


class ContactIdView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.get_appear()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ContactListView(generics.ListAPIView):

    queryset = Contact.objects.annotate(
        last_name=Substr('name', StrIndex('name', Value(' '))))
    serializer_class = ContactSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    ordering_fields = ['last_name']
    search_fields = ('name',)
    

    


