# Generated by Django 3.2.9 on 2021-11-29 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('replies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='comment_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comments.comment'),
        ),
    ]