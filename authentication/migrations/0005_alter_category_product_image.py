# Generated by Django 5.1.3 on 2024-11-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_category_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product_image',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
