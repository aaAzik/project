from rest_framework import serializers
from scoop.models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image = obj.image.url
            return request.build_absolute_uri(image)
        return None