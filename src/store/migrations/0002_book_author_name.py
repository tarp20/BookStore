# Generated by Django 3.2.4 on 2021-06-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='author', max_length=50),
            preserve_default=False,
        ),
    ]