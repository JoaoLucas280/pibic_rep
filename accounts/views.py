from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from courses.models import Course


@login_required
def dashboard(request):
    courses = (
        Course.objects
        .filter(coordinators=request.user)
        .distinct()
        .prefetch_related(
            "curriculummatrix_set__semester_set__subject_set"
        )
        .order_by("name")
    )

    return render(request, "accounts/dashboard.html", {
        "courses": courses,
    })
