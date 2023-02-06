# Generated by Django 4.1.6 on 2023-02-06 12:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animals', '0003_alter_animal_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Animal',
            new_name='Pet',
        ),
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name_plural': 'Pets'},
        ),
    ]
