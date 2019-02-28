from django import forms
from .models import NewCarModel


# car form linked to model
class NewCarForm(forms.ModelForm):
    class Meta:
        model = NewCarModel
        fields = '__all__'
    # validation
    def clean_mpg(self):
        mpgData = self.cleaned_data['mpg']
        if mpgData < 20:
            raise forms.ValidationError('That is less than a truck!')
        if mpgData > 500:
            raise forms.ValidationError('That is impossible(in 2019)!')

        return mpgData

    def clean_modelYear(self):
        yearData = self.cleaned_data['modelYear']
        if yearData < 2019:
            raise forms.ValidationError('That is not new!!!')

        return yearData
