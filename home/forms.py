from django import forms
from .models import Contact, Appoint

class Contactform(forms.ModelForm):

    name = forms.CharField(
        label='',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        label='',
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        )
    )
    phone = forms.IntegerField(
        label='',
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Phone",
                "class": "form-control"
            }
        )
    )
    mess = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write here...",
                "class": "form-control",
                "rows": 3,
                "cols": 50
            }
        )
    )
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'mess', 'email')

DAY_CHOICES =( 
    ("Monday","Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),        
    ("Thursday", "Thursday"),
    ("Friday","Friday"),
    ("Saturday","Saturday")
) 
TIME_CHOICES =( 
    ("9am-11am","9am-11am"),
    ("11am-1pm", "11-1pm"),
    ("3pm-5pm", "3pm-5pm"),        
    ("5pm-7pm", "5pm-7pm"),
) 
class Appointform(forms.ModelForm):

    f_name = forms.CharField(
        label='',
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": " First Name",
                "class": "form-control"
            }
        )
    )
    l_name = forms.CharField(
        label='',
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        )
    )
    phone1 = forms.IntegerField(
        label='',
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Phone 1",
                "class": "form-control"
            }
        )
    )
    phone2 = forms.IntegerField(
        label='',
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Phone 2",
                "class": "form-control"
            }
        )
    )
    add = forms.CharField(
        label='',
        max_length=100,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address",
                "class": "form-control"
            }
        )
    )
    city = forms.CharField(
        label='',
        max_length=100,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "city",
                "class": "form-control"
            }
        )
    )
    state = forms.CharField(
        label='',
        max_length=50,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "State",
                "class": "form-control"
            }
        )
    )
    pincode = forms.IntegerField(
        label='',
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Pincode",
                "class": "form-control",
            }
        )
    )
    day = forms.ChoiceField(
        label='',
        choices=DAY_CHOICES,
        required=True,
        widget=forms.Select(
            attrs={
                "placeholder": "-----",
                "class": "form-control"
            }
        )
    )
    timeslot = forms.ChoiceField(
        label='',
        choices=TIME_CHOICES,
        required=False,
        widget=forms.Select(
            attrs={
                "placeholder": "------",
                "class": "form-control"
            }
        )
    )
    symptom = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write your symptoms here...",
                "class": "form-control",
                "rows": 3,
                "cols": 50
            }
        )
    )
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
            }
        )
    )
    class Meta:
        model = Appoint
        fields = ('f_name', 'l_name', 'phone1', 'phone2', 'add', 'city', 'state', 'pincode', 'day', 'timeslot', 'symptom', 'email')
        exclude = ("doctor", )

    def __init__(self, *args, **kwargs):
        self.from_doctor = kwargs.pop("from_doctor", None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs): 
        self.instance.doctor = self.from_doctor
        return super().save(*args, **kwargs)