from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from . forms import ReviewForm
from . models import Review

# Create your views here.
# replacing the function view with the class-based view


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank_you')

        return render(request, 'reviews/review.html', {
            "form": form
        })
# Replaced function view with the class_based view above.
# def review(request):
#     # Basic or manual form validation process.
#     # if request.method == 'POST':
#     #     entered_username = request.POST['username']

#     #     if entered_username == "":
#     #         return render(request, 'reviews/review.html', {
#     #             'has_error': True
#     #         })
#     #     print(entered_username)
#     #     return HttpResponseRedirect('/thank_you')

#     # Using the Django Form Class
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank_you')

#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/review.html', {
#         "form": form
#     })


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["message"] = "Submitted Succcessfully!"
        return context


class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
