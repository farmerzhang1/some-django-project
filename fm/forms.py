from django import forms

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-upload-field'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'id': 'js-textarea'}))
