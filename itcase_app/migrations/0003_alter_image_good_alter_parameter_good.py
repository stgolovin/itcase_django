# Generated by Django 4.2.1 on 2023-05-14 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itcase_app', '0002_alter_good_options_good_sort_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='itcase_app.good'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='itcase_app.good'),
        ),
    ]
