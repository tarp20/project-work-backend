from django.core.management.base import BaseCommand


from contacts.models import Contact


class Command(BaseCommand):
    help = 'set  zero appreciance'

    def handle(self, *args, **kwargs):
        qs = Contact.objects.exclude(appearance=0)
        for contact in qs:
            contact.appearance = 0
            contact.save()
        print('Appearance of all contacts reset to zero')

