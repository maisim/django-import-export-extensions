# Generated by Django 5.1.1 on 2024-10-14 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list[str] = []

    operations = [
        migrations.CreateModel(
            name="Band",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Band",
                "verbose_name_plural": "Bands",
            },
        ),
        migrations.CreateModel(
            name="Instrument",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Instrument",
                "verbose_name_plural": "Instruments",
            },
        ),
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "external_id",
                    models.CharField(
                        editable=False,
                        help_text="External ID for sync import objects.",
                        null=True,
                        unique=True,
                        verbose_name="External ID",
                    ),
                ),
                (
                    "instrument",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fake_app.instrument",
                    ),
                ),
            ],
            options={
                "verbose_name": "Artist",
                "verbose_name_plural": "Artists",
            },
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_joined", models.DateField()),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fake_app.artist",
                    ),
                ),
                (
                    "band",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fake_app.band",
                    ),
                ),
            ],
            options={
                "verbose_name": "Membership",
                "verbose_name_plural": "Memberships",
            },
        ),
        migrations.AddField(
            model_name="artist",
            name="bands",
            field=models.ManyToManyField(
                related_name="artists",
                through="fake_app.Membership",
                to="fake_app.band",
            ),
        ),
    ]