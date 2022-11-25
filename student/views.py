from django.shortcuts import render, redirect
from .forms import StudentForm, StudentAddressForm, StudentDocumentForm, StudentSchoolForm, StudentParentForm
from .models import StudentInfo,Document,School, Location

from django.utils.translation import gettext as _

def student_list(request):
    student = StudentInfo.objects.order_by('-emis_id')
    #address = Location.objects.
    context = {'student': student}
    return render(request, 'student/student-list.html', context)


def student_profile(request, emis_id):
    student = StudentInfo.objects.get(emis_id=emis_id)
    context = {
        'student': student
    }
    return render(request, 'student/student-profile.html', context)


def student_registration(request):
    student_form = StudentForm(request.POST or None, request.FILES or None)
    personal_school_form = StudentSchoolForm(request.POST or None, request.FILES or None)
    student_address_form = StudentAddressForm(request.POST or None)
    student_parent_form = StudentParentForm(request.POST or None, request.FILES or None)
    student_documents_form = StudentDocumentForm(request.POST or None, request.FILES)

    if request.method == 'POST':
        if student_form.is_valid() and personal_school_form.is_valid() and student_address_form.is_valid() and student_parent_form.is_valid() and student_documents_form.is_valid():
            s1 = personal_school_form.save()
            s2 = student_address_form.save()
            s3 = student_parent_form.save()
            s4 = student_documents_form.save()
            student_info = student_form.save(commit=False)
            student_info.school = s1
            student_info.address = s2
            student_info.parent = s3
            student_info.documents = s4
            student_info.save()
            return redirect('student-list')
    context = {
        'student_form': student_form,
        'school_form': personal_school_form,
        'address_form': student_address_form,
        'parent_form': student_parent_form,
        'documents_form': student_documents_form
    }
    return render(request, 'student/student-registration.html', context)

def student_edit(request, emis_id):
    student = StudentInfo.objects.get(emis_id=emis_id)
    student_form = StudentForm(instance=student)
    student_school_form = StudentSchoolForm(instance=student.school)
    student_address_form = StudentAddressForm(instance=student.address)
    student_Parent_form = StudentParentForm(instance=student.parent)
    student_documents_form = StudentDocumentForm(instance=student.documents)

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        student_school_form = StudentSchoolForm(request.POST,instance=student.school)
        student_address_form = StudentAddressForm(request.POST, instance=student.address)
        student_Parent_form = StudentParentForm(request.POST, instance=student.parent)
        student_documents_form = StudentDocumentForm(request.POST, request.FILES, instance=student.documents)
        if student_form.is_valid() and student_school_form.is_valid() and student_address_form.is_valid() and student_Parent_form.is_valid()  and student_documents_form.is_valid():
            s1 = student_school_form.save()
            s2 = student_address_form.save()
            s3 = student_Parent_form.save()
            s4 = student_documents_form.save()
            student_info = student_form.save(commit=False)
            student_info.school = s1
            student_info.address = s2
            student_info.parent = s3
            student_info.documents = s4
            student_info.save()
            return redirect('student-list')

    context = {
        'student_form': student_form,
        'school_form': student_school_form,
        'address_form': student_address_form,
        'parent_form': student_Parent_form,
        'documents_form': student_documents_form
    }
    return render(request, 'student/student-edit.html', context)

def student_delete(request, emis_id):
    student = StudentInfo.objects.get(emis_id=emis_id)
    student.delete()
    return redirect('student-list')
