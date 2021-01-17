
from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Shark


class SharkView(View):
    def get(self, request):
        sharks = Shark.objects.all()
        return render(request, "sharks/shark_list.html", {"shark_list": sharks})

class SharkDetailView(View):
    def get(self, request, pk):
        shark = Shark.objects.get(id=pk)
        return render(request, "sharks/shark_detail.html", {"shark": shark})