
from django.shortcuts import render

from portfolio_projects.data import PROJECTS


def home(request):
    return render(
        request,
        "core/home.html",
        {"projects": PROJECTS}
    )
