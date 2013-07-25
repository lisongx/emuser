from django.forms import ModelForm
from profile.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
