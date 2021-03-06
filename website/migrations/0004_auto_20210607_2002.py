# Generated by Django 3.2.4 on 2021-06-07 18:02

from django.db import migrations, models
import django.db.models.deletion
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_photo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dt_publish', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(upload_to=website.models.rename_and_upload),
        ),
        migrations.CreateModel(
            name='AlbumPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ref', models.BooleanField(default=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.album')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='website.photo')),
            ],
        ),
    ]
