from django.db import models


class Good(models.Model):
    name = models.TextField(max_length=30, help_text="Enter good name")
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.name


class Image(models.Model):
    good = models.ForeignKey(to="Good", on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=100)
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_order']

    def __str__(self):
        return self.caption


class Parameter(models.Model):
    good = models.ForeignKey(to='Good', on_delete=models.CASCADE, related_name='parameters')
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sort_order = models.IntegerField(default=0)


    class Meta:
        ordering = ['sort_order']
