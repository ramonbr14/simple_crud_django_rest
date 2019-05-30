# Generated by Django 2.2.1 on 2019-05-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified_at', null=True)),
                ('name', models.CharField(db_column='tx_name', max_length=104)),
                ('login', models.CharField(db_column='tx_login', max_length=64)),
                ('password', models.CharField(db_column='tx_password', max_length=104)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
