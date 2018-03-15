from django.urls import path
from .views import InboxListAPIView,SentItemsListAPIView

app_name = "api"

urlpatterns = [
   path('inbox/',InboxListAPIView.as_view(),name="inbox"),
   path('sent_items/',SentItemsListAPIView.as_view(),name="sent_items")
]