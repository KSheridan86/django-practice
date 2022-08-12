from django.db import models


class Item(models.Model):
    """
    Docstrings R us!!
    """
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
