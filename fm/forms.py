from django import forms
from django.conf import settings
from os import listdir
from os.path import isfile, join

CHOICES = [
    ('Simple', 'First Model'), ('DH', 'Diffie-Hellman')
]
default_files = ['diffie-hellman', 'simple']

class UploadFileForm(forms.Form):
    def __init__(self, flist, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['select'] = forms.ChoiceField(choices=flist, widget=forms.Select(attrs=
        {
            'size' : str(len(flist)),
            'id': 'model-select'
        }))
        pass
    # title = forms.CharField(max_length=50)
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-upload-field', 'id': 'file1'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'spthy-content'}))
    # select = forms.ChoiceField(choices=[(f[:-6], f[:-6].upper()) for f in listdir(tamarin_path)], widget=forms.Select(attrs=
    #     {'size': str(len(listdir(tamarin_path))), 'id': 'model-select'
    # }))
