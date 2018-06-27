# Generated by Django 2.0.6 on 2018-06-09 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doc_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.Doctor'),
        ),
    ]
