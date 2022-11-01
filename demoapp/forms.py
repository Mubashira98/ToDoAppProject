from django import forms

from demoapp.models import todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = todo
        fields = "__all__"