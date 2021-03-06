# Generated by Django 2.1.5 on 2020-09-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='post.Category'),
        ),
    ]
