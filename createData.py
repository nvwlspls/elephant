__author__ = 'waynejessen'




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
