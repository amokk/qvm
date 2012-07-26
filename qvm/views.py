# Create your views here.
from django.shortcuts import render
from forms import ContactForm

#def create_vm(request):
#    return HttpResponse("fsa")

def create_vm(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'qvm/vm_create.html', {
        'form': form,
    })
