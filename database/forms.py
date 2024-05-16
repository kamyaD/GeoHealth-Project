from django import forms
from .models import (
    DatabaseAgakhanData,DatabaseMamaLucyData,
    DatabaseMbagathiData,DatabaseMetropolitanData,
    DatabaseNairobiData,DatabaseMataData,
    DatabaseBamData,DatabaseCHSData,
    DatabaseSpirometryData,DatabaseQuontAQData,
    DatabasAirQoData,DatabaseEsmaplerData
)


class DatabaseAgakhanDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseAgakhanData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)

class DatabaseMamaLucyDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseMamaLucyData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseMbagathiDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseMbagathiData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseMetropolitanDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseMetropolitanData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseNairobiDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseNairobiData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseMataDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseMataData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseBamDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseBamData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseCHSDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseCHSData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseSpirometryDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseSpirometryData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseQuontAQDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseQuontAQData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabasAirQoDataForm(forms.ModelForm):
    class Meta:
        model = DatabasAirQoData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


class DatabaseEsmaplerDataForm(forms.ModelForm):
    class Meta:
        model = DatabaseEsmaplerData
        fields = ('name', 'file')

    def save(self, request=None, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self.instance, 'updated_by') and self.instance.updated_by is None and request:
            # Get the current authenticated user from the request object
            user = request.user
            if user.is_authenticated:
                self.instance.updated_by = user
        super().save(*args, **kwargs)


