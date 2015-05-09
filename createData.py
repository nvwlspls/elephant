__author__ = 'waynejessen'

from faker import Factory

import random, time

from shows.models import band, show, showOrder, venue, contact

fake = Factory.create()


def insertband(name, bandHomeTown, bandHomeState, bandGenre):
    """to create and save a band object """
    from shows.models import band

    b = band(bandName=name,
             bandHomeTown=bandHomeTown,
             bandHomeState=bandHomeState,
             bandGenre=bandGenre)
    b.save()

"""venue insert and save group"""
def insertvenue(name, venuecontact, venuedescription, venuearea, venueneighborhood,
                venuestreetaddress, venuecity, venuestate, venuezip, venuephone):
    """to create and save a Venue Object"""
    from shows.models import venue

    v = venue(venueName=name,
              venueContact=venuecontact,
              venueDescription=venuedescription,
              area=venuearea,
              neighborhood=venueneighborhood,
              streetAddress=venuestreetaddress,
              city=venuecity,
              state=venuestate)
    v.save()

def createvenue():
    """create and return a venue"""
    from faker import Factory
    fake=Factory.create()
    name=fake.company()
    description=fake.paragraphs(nb=2)
    streetaddress=fake.street_address()
    city=fake.first_name()
    state=fake.state()
    areaRand = fake.random_int(min=0, max=3)
    areas=["North County", "East County", "Central", "South Bay"]
    area = areas[areaRand]
    neighborhoods = ["Webster",
                    "Bankers Hill",
                    "Balboa Park",
                    "Gaslamp Quarter",
                    "City Heights",
                    "Serra Mesa",
                    "Talmadge"]
    neighborhoodrand = fake.random_int(min=0, max=len(neighborhoods )-1)
    neighborhood = neighborhoods[neighborhoodrand]
    return [name, description, area, neighborhood, streetaddress, city, state]

"""contact insert and save group"""
def insertcontact(contactemail, contactfirstname, contactlastname, contanctnickname):
    """to create and save a contact object"""
    from shows.models import contact
    c = contact(contactEmail=contactemail,
                contactFirstName=contactfirstname,
                contactLastName=contactlastname,
                contactNickname=contanctnickname)
    c.save()

def createcontact():
    """create and save a faux contact"""
    from faker import Factory
    fake = Factory.create()
    email = fake.free_email()
    firstname = fake.first_name()
    lastname = fake.last_name()
    nickname = fake.first_name()
    return [email, firstname, lastname, nickname]

def createAndSaveContact():
    """use other functions to create and save a contact to the database"""
    contact = createcontact()
    insertcontact(contact[0], contact[1], contact[2], contact[3])



def insertshow(showvenueid, showdate, showtime, showbands, showbandextratext, showage, showcost,
            showorders):
    """create a new show"""
    from shows.models import show, showOrder

    s = show(showVenueID=showvenueid,
                showDate=showdate,
                showTime=showtime,
                showBandExtraText=showbandextratext,
                showAge=showage,
                showCost=showcost)



"""Get all contact emails"""
def getContactEmails():
    """returns the email addresses, in list format, of all the contacts in the django database"""
    from shows.models import contact
    allcontacts = contact.objects.all()
    contactEmails = []
    for c in allcontacts:
        contactEmails.append(c.contactEmail)
    return contactEmails