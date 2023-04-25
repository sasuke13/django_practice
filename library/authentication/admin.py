from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order

from django.contrib import admin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "is_staff")
    list_filter = ("email", "is_staff")
    fields = (("email", "first_name", "middle_name", "last_name", "password"), ("is_active", "is_staff", "is_superuser"), "role")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
    list_filter = ("id", "name", "surname")
    fieldsets = (
        (
            "Unchangeable",
            {
                "fields": ("name", "surname")
            }
        ),
        (
            "Changeable",
            {
                "fields": ("patronymic", "books")
            }
        ),

    )


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "count")
    list_filter = ("id", "name", "count")
    fieldsets = (
        (
            "Unchangeable",
            {
                "fields": ("name", )
            }
        ),
        (
            "Changeable",
            {
                "fields": ("description", "count")
            }
        ),

    )


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    list_filter = ("id", "user", "created_at")
    fields = (("book", "user"), ("end_at", "plated_end_at"))


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
