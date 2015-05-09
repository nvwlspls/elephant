from django.contrib import admin

# Register your models here.
from shows.models import show, venue, contact, band, showOrder, genre

admin.site.register(show)
admin.site.register(venue)
admin.site.register(contact)
admin.site.register(band)
admin.site.register(showOrder)
admin.site.register(genre)
