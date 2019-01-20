# Generated by Django 2.1.5 on 2019-01-19 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitamin_type', models.TextField()),
                ('vitamin_name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_card.Product'),
        ),
    ]
