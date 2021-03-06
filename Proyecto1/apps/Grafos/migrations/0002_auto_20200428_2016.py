# Generated by Django 3.0.5 on 2020-04-28 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grafos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Aristas',
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterModelOptions(
            name='vertice',
            options={'ordering': ['nombre'], 'verbose_name': 'Vertices'},
        ),
    ]
