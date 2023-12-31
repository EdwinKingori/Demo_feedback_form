from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from . forms import ReviewForm
from . models import Review

# Create your views here.
# replacing the function view with the class-based view


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank_you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Replacing the get method
    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, 'reviews/review.html', {
    #         "form": form
    #     })

    #

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


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

# Replaced the TemplateView cotext fetching below with the ListView model above
    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context


class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


# Replacing with the DetailView
    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
