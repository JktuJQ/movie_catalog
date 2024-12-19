# Generated by Django 5.1.4 on 2024-12-19 11:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('films', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Вопрос')),
                ('question_type', models.CharField(choices=[('Один', 'Один вариант ответа'), ('Несколько', 'Несколько вариантов ответа')], default=('Один', 'Один вариант ответа'), max_length=10)),
                ('position', models.PositiveIntegerField(verbose_name='Позиция вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос для голосования',
                'verbose_name_plural': 'Вопросы для голосования',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('theme', models.CharField(max_length=1024, verbose_name='Тема опроса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор опроса')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film', verbose_name='Фильм')),
                ('polls', models.ManyToManyField(to='polls.question', verbose_name='Опросы')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
                'ordering': ['theme'],
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Вариант ответа')),
                ('position', models.PositiveIntegerField(verbose_name='Позиция варианта ответа')),
                ('votes', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Проголосовавшие')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответа',
                'ordering': ['name'],
            },
        ),
    ]
