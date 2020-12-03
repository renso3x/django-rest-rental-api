from django.contrib import admin
from .models import Friend, Belonging, Borrowed


class FriendAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class BelongingAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class BorrowedAdmin(admin.ModelAdmin):
    list_display = ("id", "what", "to_who", "when", "returned")


# Register your models here.
admin.site.register(Friend, FriendAdmin)
admin.site.register(Belonging, BelongingAdmin)
admin.site.register(Borrowed, BorrowedAdmin)