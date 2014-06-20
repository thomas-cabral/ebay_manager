from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid
import os
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=55)

    class Meta:
        verbose_name_plural = "Categories"

    @python_2_unicode_compatible
    def __str__(self):
        return self.title


class Item(models.Model):
    # Tracking fields
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='item_user')

    # Base item details
    category = models.ForeignKey(Category, related_name='category')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    purchased_for = models.DecimalField(max_digits=10, decimal_places=2)
    item_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Auction posted
    posted = models.BooleanField(default=False)
    listing_url = models.URLField(blank=True)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    buy_it_now = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_estimate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Item sold
    is_sold = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    sold_for = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_actual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('static/images', filename)


class Image(models.Model):
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True, verbose_name='item_image')
    item = models.ForeignKey(Item, related_name='image_item')

    @python_2_unicode_compatible
    def __str__(self):
        return "/%s" % self.image.url

