from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ApplicationSearchForm(forms.Form):
    loan_id = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


