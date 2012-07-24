from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Jméno', max_length=100, initial='Anonym')
    email = forms.EmailField(label='E-mail', required=False)
    phone = forms.CharField(label='Telefon', max_length=20, required=False)
    reaction = forms.BooleanField(label='Chci dostat odpověď', required=False)
    text = forms.CharField(label='Zpráva', widget=forms.Textarea, help_text='Sem napište svou připomínku nebo dotaz.')
