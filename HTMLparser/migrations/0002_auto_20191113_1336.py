# Generated by Django 2.1.5 on 2019-11-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HTMLparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterField(
            model_name='task',
            name='code',
            field=models.CharField(max_length=100, verbose_name='кодировка'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(verbose_name='выполнено'),
        ),
        migrations.AlterField(
            model_name='task',
            name='minutes',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='минуты'),
        ),
        migrations.AlterField(
            model_name='task',
            name='report',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='seconds',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='секунды'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(verbose_name='время старта'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100, verbose_name='заголовок'),
        ),
    ]