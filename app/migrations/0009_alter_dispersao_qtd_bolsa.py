# Generated by Django 4.1.10 on 2023-10-29 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_agendamento_cod_doador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispersao',
            name='qtd_bolsa',
            field=models.IntegerField(max_length=45),
        ),
    ]
