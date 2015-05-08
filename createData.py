__author__ = 'waynejessen'

from faker import Factory

import random, time

from shows.models import band, show, showOrder, venue, contact

fake = Factory.create()

def insertband(name, bandHomeTown, bandHomeState, bandGenre):
    """to create and save a band object """
    from shows.models import band
    b= band(bandName=name,
            bandHomeTown=bandHomeTown,
            bandHomeState=bandHomeState,
            bandGenre=bandGenre)
    b.save()

def insertvenue(name, venuecontact , venuedescription, venuearea, venueneighborhood,
                venuestreetaddress, venuecity, venuestate, venuezip, venuephone):
    """to create and save a Venue Object"""
    from shows.models import Venue
    v = venue(venueName=name,
              venueContact=venuecontact,
              venueDescription=venuedescription,
              area=venuearea,
              neighborhood=venueneighborhood,
              streetAddress=venuestreetaddress,
              city=venuecity,
              state=venuestate)
    v.save()

def insertcontact(contactemail, contactfirstname, contactlastname, contanctnickname):
    """to create and save a contact object"""
    from shows.models import contact
    c = contact(contactEmail:contactemail,
                contactFirstName:contactfirstname,
                contactLastName:contactlastname,
                contactNickname:contactnickname)
    c.save()



for i in range(1,1000):

    '''create random time'''
    randMonth  = str(random.randint(1, 12)).zfill(2)
    randDate   = str(random.randint(1, 28)).zfill(2)
    randHour   = str(random.randint(0, 23)).zfill(2)
    randMinute = str(random.randint(0, 59)).zfill(2)
    # format random date/time
    randShowTimeString  = ('2014' + randMonth + randDate + randHour + randMinute)
    randShowDateTime = time.strptime(randShowTimeString, '%Y%m%d%H%M')
    # random date
    stringShowDate  = time.strftime("%Y-%m-%d", randShowDateTime)
    # random time
    randShowTime = str(randShowDateTime.tm_hour).zfill(2) + ':' + random.choice(['00', '15', '30', '45'])
    showVenueID = random.choice(Venue.objects.all())
    Date = stringShowDate
    Time = randShowTime
    bandExtraTesxt = fake.text()
    age = random.choice([0, 18, 21])
    cost = random.choice([10.00, 15.00, 12.50, 18.50])
    insertShow( showVenueID ,stringShowDate, randShowTime, bandExtraTesxt, age, cost)
