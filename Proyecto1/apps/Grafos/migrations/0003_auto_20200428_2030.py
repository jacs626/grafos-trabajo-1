# Generated by Django 3.0.5 on 2020-04-28 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grafos', '0002_auto_20200428_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arista',
            options={'ordering': ['nombre'], 'verbose_name': 'Arista', 'verbose_name_plural': 'Aristas'},
        ),
        migrations.AlterModelOptions(
            name='vertice',
            options={'ordering': ['nombre'], 'verbose_name': 'Vertice', 'verbose_name_plural': 'Vertices'},
        ),
        migrations.CreateModel(
            name='Grafo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('tipo', models.CharField(max_length=45)),
                ('aristas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grafos.Arista')),
                ('vertices_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grafos.Vertice')),
            ],
            options={
                'verbose_name': 'Grafo',
                'verbose_name_plural': 'Grafos',
                'ordering': ['nombre'],
            },
        ),
    ]
