# Generated by Django 4.2.1 on 2023-05-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicqualification',
            name='certificate_number',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
