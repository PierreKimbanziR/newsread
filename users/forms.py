from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MediaList
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, InlineCheckboxes
from crispy_forms.layout import Fieldset, Layout, Submit, Button




class UserRegisterFrom(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class MediaSelectionForm(forms.ModelForm):
    
    class Meta:
        model = MediaList
        fields = ["medias"]
    
    def __init__(self, *args, **kwargs):
        super(MediaSelectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-MediaSelectionForm'
        self.helper.form_class ='form-horizontal'
        self.helper.method = 'post'
        self.helper.layout = Layout(
            Fieldset('Please, select your favorites newspapers'),
            InlineCheckboxes("medias"),
            FormActions(
                Submit('save', 'Save Your changes'),
                Button('cancel', 'Cancel')
            )

        )
