# Generated by Django 3.2.15 on 2022-12-01 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_form_register_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.district', verbose_name='district'),
        ),
    ]
