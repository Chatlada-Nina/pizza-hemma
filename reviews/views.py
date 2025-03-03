from django.shortcuts import render
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

# Create your views here.
def reviews(request):
    """
    Render the reviews page
    """
    reviews = Review.objects.filter(approved=True).order_by('created_on')

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review submitted and awaiting approval'
            )

    review_form = ReviewForm()

    return render(
        request,
        "reviews/reviews.html",
        {"reviews": reviews,
         "review_form": review_form,
         },
    )
