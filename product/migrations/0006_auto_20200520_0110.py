# Generated by Django 3.0.6 on 2020-05-20 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200519_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id']},
        ),
    ]
