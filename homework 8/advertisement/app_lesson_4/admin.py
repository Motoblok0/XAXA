from django.contrib import admin
from .models import advertisement

class advertisement_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ['created_at', 'auction']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        (
            'general', {
                'fields' : ('title', 'description'),
            }
        ),
        (
            'finance',{
                'fields' : ('price', 'auction'),
                'classes' : ['collapse'],
            }
        )
    )

    @admin.display(description='remove bargaining power')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.display(description='add bargaining power')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(advertisement, advertisement_admin)
