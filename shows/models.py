from django.db import models

from localflavor.us.forms import USPhoneNumberField, USStateSelect, USZipCodeField



# Create your models here.
class contact(models.Model):

    contactEmail = models.EmailField(max_length = 100, primary_key = True)
    contactFirstName = models.CharField(max_length = 100)
    contactLastName = models.CharField(max_length = 100, null=True)
    contactNickname = models.CharField(max_length = 100, null=True)

    def __unicode__(self):
        return str(str(self.contactFirstName) + " " + str(self.contactLastName))

class venueManager(models.Manager):
    def get_by_natural_key(self, venueName, venueID):
        return self.get(venueName=venueName, venueID=venueID)

class venue(models.Model):
    AREA_CHOICES = (
        ("NC", "North County"),
        ("EC", "East County"),
        ("CC", "Central"),
        ("SB", "South Boy") 
    )

    objects = venueManager()

    venueID = models.AutoField(primary_key = True)
    venueName = models.CharField(max_length = 75,
                                default = "Venue Name")
    venueDescription = models.TextField()
    venueArea = models.CharField(choices =  AREA_CHOICES,
                            max_length = 20)
    venueNeighborhood = models.CharField(max_length = 75,
                                        default = "Neighborhood")
    venueDateAdded = models.DateTimeField(auto_now_add = True)
    venueLastMod = models.DateTimeField(auto_now = True)
    venueStreetAddress = models.CharField(max_length = 150, null=True)
    venueCity = models.CharField(max_length = 150, null=True)
    venueState = models.CharField( max_length=50, null=True)
    venueZipCode = models.CharField(max_length=9, null = True)
    venuePhone = models.CharField(max_length=50, null=True)
    venueContact = models.ForeignKey('contact', related_name = 'contact2', null=True)

    def __unicode__(self):
       return unicode(self.venueName)

    def natural_key(self):
        return (self.venueName)

    class Meta:
        unique_together = (('venueName', 'venueID'),)

class bandManager:
    def get_by_natural_key(self, bandName, bandID):
        return self.get(bandName=bandName, bandID=bandID)

class band(models.Model):
    bandID = models.AutoField(primary_key=True)
    bandName = models.CharField(max_length=200, default="Band Name")
    bandHomeTown = models.CharField(max_length=100,
                                    default="Home Town")
    bandHomeState = models.CharField( max_length=50, null=True)
    '''TODO: Add a genre selection field'''
    bandGenre = models.CharField(max_length=75, null=True)
    bandDateAdded = models.DateTimeField(auto_now_add=True)
    bandDateMod = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
       return unicode(self.bandName)

    def natural_key(self):
        return (self.bandName)

    class Meta:
        unique_together = (('bandName', 'bandID'),)

class showOrder(models.Model):
    showOrderID = models.AutoField(primary_key = True)
    showOrderOrder = models.IntegerField()
    showOrderShowID = models.ForeignKey("show", related_name = 'showIDOrder')
    showOrderBandID = models.ForeignKey("band", related_name = 'bandIDOrder')

    class Meta:
        ordering = ['showOrderOrder']

    def __unicode__(self):
        return unicode(str(self.showOrderOrder) + "-" +str(self.showOrderBandID.bandName))


class show(models.Model):
    showID = models.AutoField(primary_key = True)
    showVenueID = models.ForeignKey("venue")
    showDate = models.DateField()
    showTime = models.TimeField()
    showDateTimeAdded = models.DateTimeField(auto_now_add = True)
    showDateTimeMod = models.DateTimeField(auto_now = True)
    showBands = models.ManyToManyField(band, related_name = "bands" )
    showOrders = models.ManyToManyField(showOrder, related_name = 'orders')
    showBandExtraText = models.TextField()
    showAge = models.CharField(max_length = 3, null = True)
    showCost = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __unicode__(self):
       return unicode(str(self.showVenueID.venueName)+ "-" + str(self.showDate))

    def as_json(self):
        return dict(
            showID=self.showID,
            showVenueName=self.showVenueID,
            showDate=self.showDate,
            showTime=self.showTime,
            showBands=self.showBands.all(),
            showOrders=self.showOrders.all(),
            showBandExtraText=self.showBandExtraText,
            showAge=self.showAge,
            showCost=self.showCost
        )


class genre(models.Model):
    genreID = models.AutoField(primary_key=True)
    genreName = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.genreName)