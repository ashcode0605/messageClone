from rest_framework import generics
from messageApp.models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated

class SentItemsListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Message.objects.filter(sent_by=self.request.user)
        else:
            return []

class InboxListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Message.objects.filter(sent_to = self.request.user)
        else:
            return []
