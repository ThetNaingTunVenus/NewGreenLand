# Generated by Django 4.1.7 on 2023-04-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_cartproduct_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='barcode_id',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
