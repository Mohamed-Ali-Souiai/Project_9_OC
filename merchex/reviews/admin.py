from django.contrib import admin


from reviews.models import Band, Listing


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre')  # liste les champs que nous voulons sur l'affichage de la liste


class ListingAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('title', 'band')  # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)

