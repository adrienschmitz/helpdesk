# Generated by Django 4.0.2 on 2022-03-19 12:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locais',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Solicitante',
                'verbose_name_plural': 'Solicitantes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cor', models.CharField(default='#000000', max_length=7)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['first_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('patrimonio', models.CharField(blank=True, max_length=100)),
                ('resposta', models.TextField(blank=True)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.local')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.solicitante')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.status')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.person')),
            ],
            options={
                'verbose_name': 'Solicitação',
                'verbose_name_plural': 'Solicitações',
            },
        ),
        migrations.AddField(
            model_name='local',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.setor'),
        ),
    ]