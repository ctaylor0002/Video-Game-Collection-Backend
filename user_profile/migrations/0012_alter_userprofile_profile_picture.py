# Generated by Django 4.1.4 on 2022-12-24 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_alter_userprofile_profile_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='../images/base_profile_picture.jpg', upload_to='images/'),
        ),
    ]