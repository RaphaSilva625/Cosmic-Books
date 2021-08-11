# Generated by Django 3.2 on 2021-04-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('editora', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=20)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]