# Generated by Django 1.11.11 on 2018-06-08 10:36

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import geotrek.authent.models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='baseinfrastructure',
            managers=[
                ('in_structure', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='infrastructuretype',
            name='structure',
            field=models.ForeignKey(blank=True, db_column='structure', default=geotrek.authent.models.default_structure_pk, null=True, on_delete=django.db.models.deletion.CASCADE, to='authent.Structure', verbose_name='Related structure'),
        ),
    ]
