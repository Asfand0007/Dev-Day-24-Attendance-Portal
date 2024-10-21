# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path(
    #     "admin/devday/27cndfk8sb36fvxnv0367fnak8cgh376fivnme03ucndbc8u2649cvn36289364bx72b4392674kwq9291740dsu29/",
    #     admin.site.urls,
    # ),
    path("", include("attendance.urls")),
]
handler404 = "attendance.views.page_not_found_404"
handler403 = "attendance.views.limit_exceed_403"