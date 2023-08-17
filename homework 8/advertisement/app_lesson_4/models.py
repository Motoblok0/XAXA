from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
class advertisement(models.Model):

    title = models.CharField(
        max_length=80,
        verbose_name='Name',
    )

    description = models.TextField(
        verbose_name='Description'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price'
    )

    auction = models.BooleanField(
        verbose_name='Auction',
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated at'
    )

    @admin.display(description='date of creation')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color : green; font-weight: bold:;" s>Today at this {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description='date of update')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color : orange; font-weight: bold:;" s>Today at this {} </span>', created_time
            )
        return self.updated_at.strftime('%d.%m.%Y at %H:%M:%S')




    def __str__(self):
        return f"id {self.id} title = {self.title} price = {self.price}"

    class Meta:
        db_table = 'advertisement'