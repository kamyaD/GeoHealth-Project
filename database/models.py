from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


class DatabaseAgakhanData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/hospital/agakhan/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

class DatabaseMamaLucyData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/hospital/mama-lucy/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()


class DatabaseMbagathiData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/hospital/mbagathi/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()


class DatabaseMetropolitanData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/hospital/metropolitan/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

class DatabaseNairobiData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/hospital/nairobi/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

class DatabaseMataData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/hospital/mata/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

class DatabaseBamData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/bam/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

class DatabaseCHSData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/chs/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

class DatabaseSpirometryData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/spirometry/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()


class DatabaseQuontAQData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/quontAQ/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()


class DatabasAirQoData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/airqo/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

class DatabaseEsmaplerData(models.Model):
    name = models.CharField(max_length=64)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='database/e_smapler/')
    uploaded_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        if hasattr(self, 'updated_by') and self.updated_by is None:
            # Get the current authenticated user
            user = self.request.user
            if user.is_authenticated:
                self.updated_by = user
        super().save(*args, **kwargs)

    def delete(self):
        self.file.delete()
        super().delete()

