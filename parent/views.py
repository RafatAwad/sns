from django.shortcuts import render, redirect

from .forms import ParentForm, ParentAddressForm
from .models import Parent, Location


def parents_list(request):
    parents = Parent.objects.all()
    context = {'parents': parents}
    return render(request, 'parents/parents-list.html', context)


def parent_profile(request, id):
    parent = Parent.objects.get(id=id)
    context = {
        'parent': parent
    }
    return render(request, 'parents/parent-profile.html', context)


def parent_edit(request, id):
    parent = Parent.objects.get(id=id)
    parent_form = ParentForm(instance=parent.id)
    parent_address_form = ParentAddressForm(instance=parent.address)
    if request.method == 'POST':
        parent_form = ParentForm(request.POST, request.FILES, instance=parent.id)
        parent_address_form = ParentAddressForm(request.POST, instance=parent.address)
        if  parent_form.is_valid() and parent_address_form.is_valid() :
            s1 = parent_address_form.save()
            parent_info = parent_form.save(commit=False)
            parent_info.save()
            return redirect('parents-list')

    context = {
        'parent_form': parent_form,
        'parent_address_form': parent_address_form,
    }
    return render(request, 'parents/parent-edit.html', context)

def parent_delete(request, id):
    parent = Parent.objects.get(p_code=id)
    parent.delete()
    return redirect('parents-list')

