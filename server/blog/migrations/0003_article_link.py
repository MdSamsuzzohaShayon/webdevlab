# Generated by Django 4.2.7 on 2023-11-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_author_id_article_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.CharField(default='post-1-slug', max_length=255),
            preserve_default=False,
        ),
    ]
