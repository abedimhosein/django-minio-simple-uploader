from django.db import models


class Document(models.Model):
    doc = models.FileField(upload_to='documents')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
