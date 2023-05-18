# Generated by Django 3.2.18 on 2023-05-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_article', '0006_alter_article_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='preview',
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
