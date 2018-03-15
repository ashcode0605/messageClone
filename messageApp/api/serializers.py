from rest_framework import serializers
from messageApp.models import Message
from markdown_deux import markdown
from messageApp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    profile_pic = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username','profile_pic')

    def get_profile_pic(self,obj):
        try:
            p = obj.UserProfile.profile_pic.url
        except:
            p = ''
        
        return p

class MessageSerializer(serializers.ModelSerializer):

    message_body = serializers.SerializerMethodField()
    sent_by = serializers.SerializerMethodField()
    sent_to = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('sent_by','sent_to','message_body','created_at')

    def get_message_body(self,obj):
        markdown_text = markdown(obj.message_body)
        return markdown_text

    def get_sent_by(self,obj):
        serialzedUser = UserSerializer(obj.sent_by)
        return serialzedUser.data

    def get_sent_to(self,obj):
        serialzedUser = UserSerializer(obj.sent_to)
        return serialzedUser.data

