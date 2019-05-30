from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=True,
        auto_now=True
    )

    class Meta:
        abstract = True


class User(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=104
    )
    login = models.CharField(
        db_column='tx_login',
        null=False,
        max_length=64
    )
    password = models.CharField(
        db_column='tx_password',
        null=False,
        max_length=104
    )

    class Meta:
        db_table = 'user'
        managed = True
