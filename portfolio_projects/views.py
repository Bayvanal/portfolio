
from django.shortcuts import render
from django.http import Http404

from .data import PROJECTS


def project_detail(request, slug):
    project = next(
        (p for p in PROJECTS if p["slug"] == slug),
        None
    )

    if project is None:
        raise Http404("Projet introuvable")

    return render(
        request,
        "projects/detail.html",
        {"project": project}
    )
