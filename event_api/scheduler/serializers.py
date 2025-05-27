from rest_framework import serializers
from .models import User, Event
from django.contrib.auth.password_validation import validate_password
from .utils import has_conflict

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=True, validators = [validate_password])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user =User.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            password = validated_data['password'],
            role = validated_data.get('role', 'viewer')
        )
        return user

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['owner', 'created_at', 'updated_at']

class BatchEventSerializer(serializers.Serializer):
    events = EventSerializer(many=True)

    def validate(self, data):
        user = self.context['request'].user
        for event in data['events']:
            if has_conflict(user, event['start_time'], event['end_time']):
                raise serializers.ValidationError(f"Time conflict with another event: {event['title']}")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        created_events = []
        for event_data in validated_data['events']:
            event = Event.objects.create(owner=user, **event_data)
            created_events.append(event)
        return created_events

from rest_framework import serializers
from .models import EventPermission, User

class EventPermissionSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = EventPermission
        fields = ['user_id', 'username', 'role']

