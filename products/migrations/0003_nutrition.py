# Generated by Django 3.2.3 on 2021-05-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('size_ml', models.CharField(max_length=45, null=True)),
                ('size_fluid_ounce', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
    ]