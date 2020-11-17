from django.shortcuts import render
from django.views import View


# Create your views here.
# BASE VIEW Class = View

class CourseView(View):
    template_name = "courses/course-detail.html"

    def get(self, request, id=None, *args, **kwargs):
        # GET METHOD
        return render(request, self.template_name, {})

    # def post(self, request, *args, **kwargs):
    #    return render(request, "about.html", {})


# HTTP METHODS

def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, "about.html", {})
