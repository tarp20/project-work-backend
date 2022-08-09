# CIC Backend Project Work

## Introduction

You'll be working on extending a simple Django application. What we care about here is quality, so please pay special attention to the quality of your solution, not to the number of finished tasks. If you're not sure about any of the requirements, please make your own decision how to approach it, and document it.
You have 24 hours to prepare your solution. Good luck!

## Application

You are working on the application for storing contacts of company clients, it consists of just a single data model and a simple admin panel. 
The application was stripped of any unnecessary elements, so you can focus on your assignment.

### How to run the application

Application should run on Python 3.10, Django 3.2.6 and postgres database. We provided Pipfile, requirements.txt file and docker-compose.
If you want to run it containerized then `docker-compose up` is enough to run python and postgres containers, otherwise you have to install
database and dependencies by yourself.

If you wish you can change database engine and install additional packages.

You might need to set **DJANGO_SETTINGS_MODULE** environment variable to run the application.

An initial set of data is located in **src/fixtures** directory - it contains 20000 lead records and 1 user record. 
Use the following command to load it:

```bash
python manage.py loaddata fixtures/initial
``` 

### Data model

The whole data model is just a single **Lead** model with the following fields:

* name
* email
* phone
* address

Sample record:

* name: Lidia Stępniewska
* email: lidia@stepniewska.pl
* phone: 600123456
* address: Korytowska, 82-149 Pęchocice 

### Admin panel

When you start the application, so it serves it's content on [http://127.0.0.1:8000](http://127.0.0.1:8000), you can 
access admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) - you can login with the following 
credentials:

* login: admin
* password: admin

## Assignment

Your assignment consists of a few steps - please read through the whole description before you start your work:

1. Create **Contacts** app and define a suitable data structure
2. Create a data migration tool to migrate **Leads** to newly created **Contacts** app
3. Design and create Rest API for interacting with **Contacts**

### Contacts app

The first step is to create a new Django app called **Contacts**. You need to design data structure with appropriate constraints to store the 
contact information that you pull from previous **Leads** application, take into account requirements given in the further steps.

### Migration tool

When you've created the new app and data model, please prepare a management command or a standalone script to migrate 
**Leads** to **Contacts** based on the following rules:

1. All Leads should be processed 
2. Multiple Leads with the same name and phone number should be merged together, so the resulting Contact contains 
all emails and addresses from merged Leads.
3. Multiple Leads with the same name, but different phone number and e-mail should be saved as separate contacts
4. Multiple Leads with the same name and e-mail, but different phone number should be saved to conflicts.csv file for further 
inspection 

You can assume that this is one time migration, script should be optimised for large amount of data.
The tool should report on the numbers of processed records in each category (all records, merged records, 
conflicting records).

### Rest API

When you have migrated the data, please design and build a Rest API allowing some basic Contact interaction:

1. Retrieve contact by id
    1. Response should contain all available fields
    2. Contact should have field with an integer representing number of times it has been retrieved, every time the contact is retrieved then counter is increased.
2. Listing contacts
    1. Response should contain all available fields
    2. Search contacts by full name - partial match
       example: record "Jan Kowalski" should be found with queries: "Jan", "Kowalski", "Jan Kowalski", "Jan Kowal" 
    3. Sort contacts by last name
3. Create new contact(optional)





### Update Migration Tool

To migrate data from Leads to Contact model with  all requirements 
I created ```Management Commands``` to procced the command run :


```bash
python src/manage.py get_contact

``` 

All weird(conflict) record saved into conflicts.csv file for further 
inspection


Also was created statistics.csv file with statistics:
The tool should report on the numbers of processed records in each category (all records, merged records, 
conflicting records).

all algorithm is in ```get_contacts.py  ```




### Update Rest API

1.You can browse every contact by id.
Added special field -  ```appearance``` which represents number of retrieving specific id of contact
```GET /api/v1/contacts/5```

And its posible to reset to zero all contact retrieving by using command


```bash
python src/manage.py set_zero

``` 

2.
Get all contacts:
```GET /api/v1/contacts/```

Paginated 100 contacts per page and created serching engine(partial match) by name


```GET /api/v1/contacts/?search=Jan```


Also added posibility ordering by last name

```GET /api/v1/contacts/?ordering=last_name```





