from django.shortcuts import render
from .models import Review
from .forms import ReviewForm

# Create your views here.
def reviews(request):
    """
    Render the reviews page
    """
    review = Review.objects.all().first()

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()

    review_form = ReviewForm()

    return render(
        request,
        "reviews/reviews.html",
        {"review": review,
         "review_form": review_form,
         },
    )
