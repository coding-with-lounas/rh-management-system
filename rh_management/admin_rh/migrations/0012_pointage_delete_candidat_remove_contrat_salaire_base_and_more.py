# Generated by Django 5.1.4 on 2025-01-16 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_rh', '0011_rename_date_absence_absence_date_absence_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pointage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compteur', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_rh.employe')),
            ],
        ),
        migrations.DeleteModel(
            name='Candidat',
        ),
        migrations.RemoveField(
            model_name='contrat',
            name='salaire_base',
        ),
        migrations.AddField(
            model_name='contrat',
            name='employe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_rh.employe'),
        ),
    ]
