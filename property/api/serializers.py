from rest_framework import serializers

from property.models import PropertyListing


class PropertyListingSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_owner')

    class Meta:
        model = PropertyListing
        fields = ['title', 'body', 'image', 'date_updated', 'username', 'price', 'image2', 'image3', 'address', 'city', 'state', 'zipcode', 'bathrooms', 'bedrooms', 'sqft', 'types',
                  'stay', 'pool', 'balcony', 'gym', 'parking', 'latitude', 'longitude', 'year_built','slug']

    def get_username_from_owner(self, property_listing):
        username = property_listing.owner.username
        return username

class Post11Serializer(serializers.ModelSerializer):
    class meta:
        model=PropertyListing
        fields=['Verify']
