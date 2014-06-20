__author__ = 'Thomas'
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('user', 'id', 'date_added', 'date_last_updated', 'category', 'name', 'description', 'purchased_for',
                  'item_weight', 'posted', 'listing_url', 'starting_bid', 'buy_it_now', 'shipping_estimate', 'sold',
                  'sold_for', 'shipping_actual', 'total_weight', 'is_sold', 'image_item')

    user = serializers.Field(source='user.username')
    image_item = serializers.RelatedField(many=True)