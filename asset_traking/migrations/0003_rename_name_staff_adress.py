# Generated by Django 4.2.3 on 2023-07-21 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset_traking', '0002_alter_assetlog_checkout_by_staff_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='name',
            new_name='adress',
        ),
    ]