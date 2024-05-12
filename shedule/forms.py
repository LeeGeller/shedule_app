from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from shedule.models import Newsletter


class MixinForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class NewsletterForm(MixinForms):
    class Meta:
        model = Newsletter
        fields = ['start_time', 'end_time', 'frequency', 'clients', 'message']
        widgets = {
            'start_time': DateTimePickerInput(options={"format": "YYYY-MM-DD HH:mm", "showClose": True}),
            'end_time': DateTimePickerInput(options={"format": "YYYY-MM-DD HH:mm", "showClose": True}),
        }
