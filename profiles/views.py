from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import Userprofile

# Create your views here.

# replaced with the model's UserProfile class that sores the file in the images folder
# def store_file(file):
#     with open("temp/wallpaper.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form,
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = Userprofile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })
