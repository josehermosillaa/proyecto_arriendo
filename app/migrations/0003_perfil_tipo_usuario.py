# Generated by Django 4.2 on 2024-05-25 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_inmueble_numero_banos'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='tipo_usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.tipo_usuario'),
            preserve_default=False,
        ),
    ]
