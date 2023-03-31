from rest_framework import serializers
from .models import Decade, Fads


class DecadeSerializer(serializers.HyperlinkedModelSerializer):
    fads = serializers.HyperlinkedRelatedField(
        view_name='fads_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Decade
        fields = ('id', 'name', 'start_year', 'end_year')


class FadsSerializer(serializers.HyperlinkedModelSerializer):
    decade = serializers.HyperlinkedRelatedField(
        view_name='decade_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Fads
        fields = ('id', 'name', 'image_url', 'description', 'decade')
