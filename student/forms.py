from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        localized_fields = ('dob',)
        

        labels = {
            'grade': _('Class'),
        }

        widgets = {
            'gender': forms.RadioSelect(attrs={
                'class': '',
            }),
        }




class SampleForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)