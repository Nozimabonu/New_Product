# Generated by Django 5.0.6 on 2024-07-02 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Commentary'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Commodities'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='is_possible',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
