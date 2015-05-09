__author__ = 'waynejessen'

from faker import Factory

import random, time

from shows.models import band, show, showOrder, venue, contact

fake = Factory.create('en_US')

"""create and insert band group"""


def insertband(name, bandHomeTown, bandHomeState, bandGenre):
    """to create and save a band object """
    from shows.models import band
    b = band(bandName=name,
             bandHomeTown=bandHomeTown,
             bandHomeState=bandHomeState,
             bandGenre=bandGenre)
    b.save()

def createband():
    """create a band using faker and return a list of attributes"""
    from faker import Factory
    from shows.models import genre
    fake=Factory.create('en_US')
    bandname=fake.company()
    bandtown=fake.city()
    bandstate=fake.state()
    genrelist=getallgenres()
    randomgenre=fake.random_int(min=0, max=len(genrelist)-1)
    genre=genrelist[randomgenre]
    return [bandname, bandtown, bandstate, genre]

def createandinsertband():
    """create and insert band"""
    randband = createband()
    insertband(randband[0],
               randband[1],
               randband[2],
               randband[3])


"""venue insert and save group"""


def insertvenue(name, venuecontact, venuedescription, venuearea, venueneighborhood,
                venuestreetaddress, venuecity, venuestate, venuezip, venuephone):
    """to create and save a Venue Object"""
    from shows.models import venue
    v = venue(venueName=name,
              venueContact=venuecontact,
              venueDescription=venuedescription,
              venueArea=venuearea,
              venueNeighborhood=venueneighborhood,
              venueStreetAddress=venuestreetaddress,
              venueCity=venuecity,
              venueState=venuestate,
              venueZipCode=venuezip,
              venuePhone=venuephone)
    v.save()


def createvenue():
    """create and return a venue"""
    from faker import Factory
    from shows.models import contact
    fake = Factory.create('en_US')
    name = fake.company()
    description = fake.paragraphs(nb=2)
    streetaddress = fake.street_address()
    city = fake.first_name()
    state = fake.state()
    areaRand = fake.random_int(min=0, max=3)
    areas = ["North County", "East County", "Central", "South Bay"]
    area = areas[areaRand]
    neighborhoods = ["Webster",
                     "Bankers Hill",
                     "Balboa Park",
                     "Gaslamp Quarter",
                     "City Heights",
                     "Serra Mesa",
                     "Talmadge"]
    neighborhoodrand = fake.random_int(min=0, max=len(neighborhoods) - 1)
    neighborhood = neighborhoods[neighborhoodrand]
    phone = fake.phone_number()
    zip = fake.postalcode()
    emails = getcontactemails()
    randomemailnum = fake.random_int(min=0,max=len(emails)-1)
    email = emails[randomemailnum]
    contact = contact.objects.get(contactEmail=email)
    return [name, contact, description, area, neighborhood, streetaddress, city, state, zip, phone]


def createandsavevenue():
    """create and save a venue"""
    randomvenue = createvenue()
    insertvenue(randomvenue[0],
                randomvenue[1],
                randomvenue[2],
                randomvenue[3],
                randomvenue[4],
                randomvenue[5],
                randomvenue[6],
                randomvenue[7],
                randomvenue[8],
                randomvenue[9])



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


"""show/showorder insert and save group"""


def insertshow(showvenueid, showdate, showtime, showbands, showbandextratext, showage, showcost):
    """create a new show"""
    from shows.models import show, showOrder
    s=show(showVenueID=showvenueid,
             showDate=showdate,
             showTime=showtime,
             showBandExtraText=showbandextratext,
             showAge=showage,
             showCost=showcost)
    s.save()
    for index, band in enumerate(showbands):
        s.showBands.add(band)
        so = showOrder(showOrderOrder=index+1,
                       showOrderShowID=s,
                       showOrderBandID=band)
        so.save()
    s.save()

def createshow():
    """create a random show with existing bands and venues"""
    from shows.models import band, venue
    import random
    from faker import Factory
    fake = Factory.create("en_US")
    time=fake.time()
    date=fake.date()
    extratext=fake.paragraphs(nb=3)
    age=random.choice(['All', '18+', '21+'])
    cost=fake.random_int(min=0, max=20)
    venue = random.choice(venue.objects.all())
    bands = []
    numbands = fake.random_int(min=1, max=10)
    for i in range(0, numbands):
        randband=random.choice(band.objects.all())
        bands.append(randband)
    return [venue, date, time, bands, extratext, age, cost]

def createandsaveshow():
    """create a show and save it using other functions"""
    createdshow = createshow()
    insertshow(createdshow[0],
               createdshow[1],
               createdshow[2],
               createdshow[3],
               createdshow[4],
               createdshow[5],
               createdshow[6])




"""Get all contact emails"""


def getcontactemails():
    """returns the email addresses, in list format, of all the contacts in the django database"""
    from shows.models import contact
    allcontacts = contact.objects.all()
    contactEmails = []
    for c in allcontacts:
        contactEmails.append(c.contactEmail)
    return contactEmails

"""get all genres"""
def getallgenres():
    """return all the genreNames in a list"""
    from shows.models import genre
    allgenres=genre.objects.all()
    genreslist = []
    for g in allgenres:
        genreslist.append(g)
    return genreslist

"""get all venues"""
def getallvenues():
    """return all the venues in a list"""
    from shows.models import venue
    allvenues=venue.objects.all()
    venuelist = []
    for v in allvenues:
        venuelist.append(v)
    return venuelist

for i in range(1, 500):
    createAndSaveContact()

for i in range(1, 500):
    createandsavevenue()

for i in range(1, 10000):
    createandinsertband()

for i in range(1, 1000):
    createandsaveshow()