# Generated by Django 3.2.3 on 2021-05-23 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
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
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=45)),
                ('english_name', models.CharField(max_length=45)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Product_Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.allergy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'products_allergy',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='allegry',
            field=models.ManyToManyField(through='products.Product_Allergy', to='products.Allergy'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='nutrition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.nutrition'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
    ]
