from django.db import models

# Create your models here.

class party(models.Model):
    """Defines the party model"""

    class Meta:
        db_table = 'party'
        managed = False

    id = models.IntegerField(primary_key=True)
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.partyname}'

class states(models.Model):
    """Defines the states model."""

    class Meta:
        db_table = 'states'
        managed = False

    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.state_name}'


class lga(models.Model):
    """Defines the lga model"""

    class Meta:
        db_table = 'lga'
        managed = False

    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state = models.ForeignKey(states, on_delete=models.CASCADE)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=255, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.lga_name}'


class ward(models.Model):
    """Defines the ward model"""

    class Meta:
        db_table = 'ward'
        managed = False
    
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga = models.ForeignKey(lga, on_delete=models.CASCADE)
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=255, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.ward_name}'


class polling_unit(models.Model):
    """Defines the polling_unit model."""

    class Meta:
        db_table = 'polling_unit'
        managed = False

    uniqueid = models.IntegerField(primary_key=True) # Set auto_increment
    polling_unit_id = models.IntegerField()
    ward = models.ForeignKey(ward, on_delete=models.CASCADE)
    lga = models.ForeignKey(lga, on_delete=models.CASCADE)
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=255, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.polling_unit_name}'

class announced_pu_results(models.Model):
    """Defines the announced_pu_results model"""

    class Meta:
        db_table = 'announced_pu_results'
        managed = False

    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=255, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        field_values = {}
        for field in self._meta.get_fields():
            field_values[field.attname] = str(getattr(self, field.name))
        return str(field_values)


class announced_lga_results(models.Model):
    """Defines the announced_lga_results model"""

    class Meta:
        db_table = 'announced_lga_results'
        managed = False

    result_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=255, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        field_values = {}
        for field in self._meta.get_fields():
            field_values[field.attname] = str(getattr(self, field.name))
        return str(field_values)

