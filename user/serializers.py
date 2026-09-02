from rest_framework import serializers
from auditlog.models import LogEntry
from .models import *


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"

class LogEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = LogEntry
        fields = "__all__"