from courses.models import Subject
from students.models import EnrollmentSubject


def add_default_subjects(enrollment):
    subjects = Subject.objects.filter(semester__curriculum_matrix=enrollment.curriculum_matrix)
    EnrollmentSubject.objects.bulk_create(
        [EnrollmentSubject(enrollment=enrollment, subject=s) for s in subjects],
        ignore_conflicts=True,
    )
