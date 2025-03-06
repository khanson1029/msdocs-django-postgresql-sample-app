# Generated by Django 4.0.2 on 2022-02-08 04:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Restaurant',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=50)),
        #         ('street_address', models.CharField(max_length=50)),
        #         ('description', models.CharField(max_length=250)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Review',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('user_name', models.CharField(max_length=20)),
        #         ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
        #         ('review_text', models.CharField(max_length=500)),
        #         ('review_date', models.DateTimeField(verbose_name='review date')),
        #         ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restauran_review.restaurant')),
        #     ],
        # ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=50)),
                ('spend', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
