from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def reviews(request):
    """
    Render the reviews page
    """
    reviews = Review.objects.filter(approved=True).order_by('created_on')

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST, files=request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review submitted and awaiting approval'
            )
            return HttpResponseRedirect(reverse('reviews'))

    else:
        review_form = ReviewForm()

    return render(
        request,
        "reviews/reviews.html",
        {"reviews": reviews,
         "review_form": review_form,
         },
    )


def review_edit(request, review_id):
    """
    Display an individual review for edit.

    **Context**
    ``review``
        An instance of :model:`reviews.Review`.
    ``review_form``
        An instance of :form:`reviews.ReviewForm`.
    """
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, files=request.FILES, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.save()
            messages.add_message(request, messages.SUCCESS, "Review Updated!")
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating review!")
            
        return HttpResponseRedirect(reverse("reviews"))
    
    else:
        review_form = ReviewForm(instance=review)
    
    return render(
        request,
        "reviews/reviews_edit.html",
        {"review": review,
         "review_form": review_form,
         },
    )

