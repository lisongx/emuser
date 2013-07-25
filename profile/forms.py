from django.forms import ModelForm
from profile.models import Profile

class profileForm(forms.Form):
    user = forms.CharField(label=u'Your name')
    url = forms.URLField(label=u'Your website', required=False)
    bio = forms.CharField(max_length=256)

