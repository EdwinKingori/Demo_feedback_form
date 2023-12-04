from django.shortcuts import render
from django.http import HttpResponseRedirect

from . forms import ReviewForm
# Create your views here.


def review(request):
    # Basic or manual form validation process.
    # if request.method == 'POST':
    #     entered_username = request.POST['username']

    #     if entered_username == "":
    #         return render(request, 'reviews/review.html', {
    #             'has_error': True
    #         })
    #     print(entered_username)
    #     return HttpResponseRedirect('/thank_you')

    # Using the Django Form Class
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/thank_you')

    form = ReviewForm()

    return render(request, 'reviews/review.html', {
        "form": form
    })


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
