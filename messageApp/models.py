from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup

class UserProfileInfo(models.Model):
    """
    Extra information realted to user
    """

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='UserProfile')
    profile_pic = models.ImageField(upload_to="profile_pic/",blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created_at']


class Message(models.Model):
    sent_by = models.ForeignKey(User,related_name="sent_items",on_delete=models.CASCADE)
    sent_to = models.ForeignKey(User,related_name="inbox",on_delete=models.CASCADE)
    message_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message_body)

    def trucated_message(self):
        html = self.marked_message()
        text = ''.join(BeautifulSoup(html,"html.parser").findAll(text=True))
        return text

    def marked_message(self):
        message = self.message_body
        marked_content = markdown(message)
        return mark_safe(marked_content)

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        ordering = ['-created_at']
