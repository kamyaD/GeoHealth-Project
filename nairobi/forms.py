from django import forms
from .models import NairobiData


class NairobiDataForm(forms.ModelForm):
    class Meta:
        model = NairobiData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)