
# Create your models here.
from django.db import models


class DMSClient(models.Model):
    # Fields
    first_name = models.CharField(max_length=20, help_text="Enter your first name")
    last_name = models.CharField(max_length=20, help_text="Enter your last name")
    sex = models.CharField(max_length=20, help_text="Enter your sex")
    age = models.CharField(max_length=20, help_text="Enter your age")

    # Metadata
    class Meta:
        ordering = ["first_name", "last_name"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return list.reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.first_name, self.second_name, self.sex, self.age


class DMSProcedure(models.Model):
    # Fields
    client_id = models.OneToOneField('DMSClient', on_delete=models.SET_NULL, null=True)
    procedure_name = models.CharField(max_length=20, help_text="Enter procedure's name")
    cost = models.IntegerField(help_text="Enter the cost")
    #sex = models.CharField(max_length=20, help_text="Enter your sex")


    # Metadata
    class Meta:
        ordering = ["procedure_name"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return list.reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.procedure_name, self.cost

class DMSPhysician(models.Model):
    # Fields
    procedure_id = models.ForeignKey('DMSProcedure', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=20, help_text="Enter your first name")
    last_name = models.CharField(max_length=20, help_text="Enter your last name")
    sex = models.CharField(max_length=20, help_text="Enter your sex")
    age = models.CharField(max_length=20, help_text="Enter your age")

    # sex = models.CharField(max_length=20, help_text="Enter your sex")

    # Metadata
    class Meta:
        ordering = ["first_name", "last_name"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return list.reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.first_name, self.second_name, self.sex, self.age


class DMSClinic(models.Model):
    # Fields
    procedure_id = models.ForeignKey('DMSPhysician', on_delete=models.SET_NULL, null=True)
    clinic_name = models.CharField(max_length=20, help_text="Enter your first name")

    # sex = models.CharField(max_length=20, help_text="Enter your sex")

    # Metadata
    class Meta:
        ordering = ["clinic_name"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return list.reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.clinic_name


class DMSUser(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    my_name = models.CharField(max_length=20, help_text="Enter name of your company")

    # Metadata
    class Meta:
        ordering = ["-my_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return list.reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

