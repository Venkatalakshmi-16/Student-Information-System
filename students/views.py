from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Student, Mark, Subject
from .forms import StudentForm, MarkForm
from django.core.paginator import Paginator


# =========================
# DASHBOARD
# =========================
@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_marks = Mark.objects.count()

    context = {
        'total_students': total_students,
        'total_marks': total_marks
    }

    return render(request, 'students/dashboard.html', context)


# =========================
# STUDENT LIST
# =========================
@login_required
def student_list(request):
    query = request.GET.get('q')

    if query:
        student_list = Student.objects.filter(name__icontains=query)
    else:
        student_list = Student.objects.all()

    paginator = Paginator(student_list, 5)  # 5 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    context = {
        'students': students
    }

    return render(request, 'students/student_list.html', context)
# =========================
# ADD STUDENT
# =========================
@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})


# =========================
# EDIT STUDENT
# =========================
@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/add_student.html', {'form': form})


# =========================
# DELETE STUDENT
# =========================
@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


# =========================
# ADD MARK
# =========================
@login_required
def add_mark(request):
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('student_list')
            except IntegrityError:
                form.add_error(None, "Mark with this Student and Subject already exists.")
    else:
        form = MarkForm()

    return render(request, 'students/add_mark.html', {'form': form})


# =========================
# STUDENT REPORT
# =========================
@login_required
def student_report(request, id):
    student = get_object_or_404(Student, id=id)
    marks = Mark.objects.filter(student=student)

    total = sum(mark.marks for mark in marks)
    subject_count = marks.count()

    percentage = 0
    grade = "N/A"

    if subject_count > 0:
        percentage = total / subject_count

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "Pass"
    else:
        grade = "Fail"

    context = {
        'student': student,
        'marks': marks,
        'total': total,
        'percentage': percentage,
        'grade': grade
    }

    return render(request, 'students/student_report.html', context)