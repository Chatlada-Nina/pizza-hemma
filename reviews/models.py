from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# (From the I think therefore I blog CL project)
STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    """
    A model to store a single review submitted by a user.

    The `Review` model is associated with a specific user (author), a rating,
    and an optional image. Reviews can be in either a draft or published state,
    indicated by the `approved` field.

    **Fields:**
    - `author`: A foreign key reference to the `User` model, representing the
      user who submitted the review.
    - `created_on`: The date when the review was created, automatically set
      when the review is created.
    - `rating`: A character field representing the rating given to the
      review, with values from 1 to 5 (choices defined in `RATING_CHOICES`).
    - `body`: A text field containing the content of the review.
    - `image`: An optional image field using Cloudinary for image storage.
      The field is blank by default.
    - `approved`: A boolean flag indicating whether the review is approved
      for display. Defaults to `False`.

    **Meta:**
    - `ordering`: Reviews are ordered by the `created_on` field, so older
      reviews appear first by default.

    **Methods:**
    - `__str__(self)`: Returns a string representation of the review,
      including the review body and the author, to improve readability in
      the Django admin panel.

    **Status:**
    - A draft review has a value of `0` for `approved`, while a published
      review has a value of `1` for `approved`.
    """
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="reviewer")
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
