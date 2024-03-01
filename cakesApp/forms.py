from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=50, label="Nombre")
    email = forms.EmailField(label="Email")
    telephone = forms.IntegerField(label="Teléfono")
    content = forms.CharField(label="Contenido", widget=forms.Textarea)
    