# Generated by Django 4.2.4 on 2023-08-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_rename_profiles_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
