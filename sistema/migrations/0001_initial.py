# Generated by Django 4.2.7 on 2023-11-14 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.IntegerField()),
                ('pontosMinimos', models.IntegerField()),
                ('pontosMaximos', models.IntegerField()),
                ('incioCiclo', models.DateTimeField()),
                ('fimCiclo', models.DateTimeField()),
                ('revista', models.FileField(upload_to='revistas-pdf')),
                ('imagemRevista', models.ImageField(blank=True, null=True, upload_to='imagens-revistas')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.IntegerField()),
                ('imagemCombo', models.ImageField(blank=True, null=True, upload_to='imagens-combos')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.marca')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.nivel')),
            ],
        ),
    ]