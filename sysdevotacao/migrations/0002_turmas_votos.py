# Generated by Django 4.2.6 on 2023-10-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysdevotacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turmas',
            name='votos',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]