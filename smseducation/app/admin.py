from django.contrib import admin
 
from app.models import contact_form
from .models import * 



 

 
@admin.register(contact_form)
class contact_form(admin.ModelAdmin):
    list_display = ('id','fname','lname','email','phone','Message')