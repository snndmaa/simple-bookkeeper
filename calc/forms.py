from django import forms
from .models import History, Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['creation_date']

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Client Name'
        self.fields['number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Client Email'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Client Address'


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HistoryForm, self).__init__(*args, **kwargs)
        self.fields['loan_amount'].widget.attrs['placeholder'] = 'Enter Loan Amount'
        self.fields['percentage'].widget.attrs['placeholder'] = 'Enter Percent'