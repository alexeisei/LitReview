from django.contrib import admin
from .models import Review, UserFollows, Ticket


admin.site.register(Review)
admin.site.register(UserFollows)
admin.site.register(Ticket)
