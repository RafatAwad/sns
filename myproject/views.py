from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import StudentInfo
from parent.models import Parent 

@login_required(login_url='login')
def home_page(request):
    total_student = StudentInfo.objects.count()
    total_parent = Parent.objects.count()

    context = {
        'student': total_student,
        'parent': total_parent,
    }
    return render(request, 'home.html', context)