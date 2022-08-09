import csv

from django.core.management.base import BaseCommand
from django.db.models import Value, BooleanField


from contacts.models import Contact
from leads.models import Lead


class Command(BaseCommand):
    help = 'seed contacts'

    def handle(self, *args, **kwargs):
        # get everyone, and mark them apips unprocessed
        qs = Lead.objects.all().annotate(
            processed=Value(False, output_field=BooleanField()))
        # all_leads
        all_data = qs.count()
        # same name and phone
        count_dup = 0

        csv_data = []
        contacts = dict()


        for lead in qs:
            nes_lead = qs.filter(name=lead.name, email=lead.email).exclude(
                phone=lead.phone).count()

            if nes_lead > 0:
                csv_data.append(dict(name=lead.name,
                                     phone=lead.phone,
                                     email=lead.email,
                                     address=lead.address))
                continue

            # is there someone with the same name and phonenumber?
            lead_num = qs.filter(
                name=lead.name, phone=lead.phone, processed=False).count()

            # person_num = qs.filter(
            #     name=person.name, phone=person.phone, processed=False).count()
            # No, they are unique, so make a contact
            if lead_num == 1:
                data = dict(name=lead.name,
                            phone=lead.phone,
                            email=lead.email,
                            address=lead.address)
                if Contact.objects.filter(**data).exists():
                    continue
                else:

                    Contact.objects.create(**data)
            # Yes, there is more than one, set up some lists to capture data
            elif lead_num > 1:
                count_dup += 1
                email_list = []
                address_list = []
                # Get all the people with same name and phone number and gather their details
                same_name_group = qs.filter(
                    name=lead.name, phone=lead.phone, processed=False)
                # cehck list before adding to avoid duplicate phones etc
                for same_name_person in same_name_group:

                    if same_name_person.email not in email_list:
                        email_list.append(same_name_person.email)
                    if same_name_person.address not in address_list:
                        address_list.append(same_name_person.address)
                    # we've dealt with this person so we don't need to look at them again
                    same_name_person.processed = True

                data = dict(name=lead.name, phone=lead.phone,
                            email=';'.join(str(x)for x in email_list),
                            address=';'.join(str(x) for x in address_list),)

                if Contact.objects.filter(**data).exists():
                    continue
                else:
                    Contact.objects.create(**data)
        # create csv weird data
        fieldnames = ['name', 'phone', 'email', 'address']

        with open('conflicts.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_data)

        # statistics data

        fieldnames = ['all records', 'merged records', 'conflicting records']
        weird_data = len(csv_data)
        normal = Contact.objects.all().count()
        row = [normal, count_dup,  weird_data]

        with open('statistics.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            writer.writerow(row)
