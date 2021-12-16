from django import forms
CHOICES = (
    ('Simple', 'First Model'), ('DH', 'Diffie-Hellman')
)
class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-upload-field', 'id': 'file1'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'spthy-content'}))
    select = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs=
        {'size': str(len(CHOICES)), 'id': 'model-select'
    }))
