from django.db import models

class Topic(models.Model):
    """
    Learning topic of user
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """
    Specific knowledge learnt under a topic
    """
    topic = models.ForeignKey(Topic, on_delete=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        return self.text[:50] + "..."