# Generated by Django 3.1.4 on 2022-05-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
