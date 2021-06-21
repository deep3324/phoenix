from django.contrib import admin
from PhoenixApp.models import ArtCraft, Review,Contact,PreviousEvent,UpComingEvent,Result, Blog, Gallery, quizomania
# from PhoenixApp.models import Member 
# Register your models here.
admin.site.register(Review)
admin.site.register(Contact)
admin.site.register(PreviousEvent)
admin.site.register(UpComingEvent)
admin.site.register(Result)
# admin.site.register(Member)
admin.site.register(Gallery)
admin.site.register(ArtCraft)
admin.site.register(quizomania)

@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyinject.js',)

