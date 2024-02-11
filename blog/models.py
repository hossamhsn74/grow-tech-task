from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a post with a title, content, publication date, and author.
    """
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    published_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_on']

    def __str__(self) -> str:
        """
        Returns a string representation of the post, which is its title.
        """
        return self.title
