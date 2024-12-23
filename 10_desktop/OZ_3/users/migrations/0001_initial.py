# Generated by Django 5.1.2 on 2024-11-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("nickname", models.CharField(max_length=50, unique=True)),
                ("name", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=15)),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("groups", models.ManyToManyField(blank=True, related_name="custom_user_set", to="auth.group")),
                (
                    "user_permissions",
                    models.ManyToManyField(blank=True, related_name="custom_user_set", to="auth.permission"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
