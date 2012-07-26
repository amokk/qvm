# -*- coding: utf-8 -*-
import floppyforms as forms
#class ContactForm(forms.Form):
#    name = forms.CharField(label='Jméno', max_length=100, initial='Anonym')
#    email = forms.EmailField(label='E-mail', required=False)
#    phone = forms.CharField(label='Telefon', max_length=20, required=False)
#    reaction = forms.BooleanField(label='Chci dostat odpověď', required=False)
#    text = forms.CharField(label='Zpráva', widget=forms.Textarea, help_text='Sem napište svou připomínku nebo dotaz.')


class Slider(forms.RangeInput):
    min = 5
    max = 20
    step = 5
    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }

class ContactForm(forms.Form):
    # subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    num = forms.IntegerField(widget=Slider)
    # cc_myself = forms.BooleanField(required=False)
