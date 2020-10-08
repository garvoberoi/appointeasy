# Generated by Django 3.0.7 on 2020-10-07 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoint',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='docid',
            field=models.IntegerField(default=1001, null=True),
        ),
    ]
