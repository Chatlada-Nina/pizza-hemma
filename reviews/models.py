from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# A draft is defined as zero and published as one.
# (From the I think therefore I blog CL project)
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# Create Review model
class Review(models.Model):
    """
    Store a single review related to : model:`auth.User`.
    """
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    created_on = models.DateField(auto_now=True)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    body = models.TextField()
    image = CloudinaryField(blank=True)
    approved = models.BooleanField(default=False)

    # Add a Meta class to define order of reviews
    class Meta:
        ordering = ["created_on"]

    # Display class object as a string to improve readable for admin
    def __str__(self):
        return f"Review: {self.body} | by {self.author}"