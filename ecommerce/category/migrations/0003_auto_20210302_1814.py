# Generated by Django 3.1.5 on 2021-03-02 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='q', to='category.category'),
        ),
    ]
