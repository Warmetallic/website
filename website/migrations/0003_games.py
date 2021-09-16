# Generated by Django 3.2.4 on 2021-09-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameID', models.CharField(default='ID', max_length=30)),
                ('gameName', models.TextField(default='Name')),
                ('gameDescription', models.TextField(default='Description')),
                ('gameImage', models.ImageField(upload_to='img')),
            ],
        ),
    ]
