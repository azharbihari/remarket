from django.contrib import admin

from interests.models import Interest


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'is_accepted',
                    'created_at', 'updated_at')
    list_filter = ('is_accepted',)
    search_fields = ('user__username', 'product__title')
