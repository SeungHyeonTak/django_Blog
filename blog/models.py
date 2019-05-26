from django.db import models
from django.conf import settings
from django.utils import timezone # timezone 모듈을 불러온다.



class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def hide(self):
        self.published_date = None
        self.save()

    def __str__(self):
        return self.title