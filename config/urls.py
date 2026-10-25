
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "projets/",
        include("portfolio_projects.urls")
    ),

    path(
        "",
        include("portfolio_core.urls")
    ),
]
