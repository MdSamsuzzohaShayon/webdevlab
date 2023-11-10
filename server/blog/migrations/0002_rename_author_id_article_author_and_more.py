# Generated by Django 4.2.7 on 2023-11-03 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='publication_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='articletags',
            old_name='article_id',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='articletags',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author_name',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='text',
        ),
    ]
