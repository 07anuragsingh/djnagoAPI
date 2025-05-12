from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    book_image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title
