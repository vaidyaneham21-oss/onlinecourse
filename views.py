from django.shortcuts import render, get_object_or_404
from .models import Course, Submission, Choice, Learner

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    learner = Learner.objects.first()

    selected = request.POST.getlist('choices')
    selected_ids = [int(x) for x in selected]

    submission = Submission.objects.create(learner=learner)
    submission.choices.set(selected_ids)

    return show_exam_result(request, course.id, submission.id)


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    choices = submission.choices.all()

    total = 0
    for choice in choices:
        if choice.is_correct:
            total += 1

    return render(request, 'result.html', {
        'course': course,
        'score': total
    })
