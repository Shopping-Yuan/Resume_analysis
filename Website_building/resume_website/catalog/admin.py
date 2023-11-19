from django.contrib import admin
from .models import all_card
# Register your models here.
@admin.register(all_card)
class cardsAdmin(admin.ModelAdmin):
     list_display = ('card_ID', 'card_name','card_type')
#admin.site.register(all_card)
