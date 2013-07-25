from django import forms
from forms import profileForms


def edit(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid(): 
            return HttpResponseRedirect('/edit/') 
    else:
        form = ContactForm()

    return render(request, 'bio_edit.html', {
        'form': form,
    })
