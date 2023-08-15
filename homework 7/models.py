from django.db import models
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

    def __str__(self):
        return f"id {self.id} title = {self.title} price = {self.price}"

    class Meta:
        db_table = 'advertisement'