from django.db import models


class Prodcut(models.Model):
    """
    Product Model with following attributes
    """
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        "Return string title representation of Product Object"
        return self.title
