# Generated by Django 4.1.7 on 2023-02-27 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_diet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodserving',
            name='pet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='food_servings', to='pets.pet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='treatserving',
            name='pet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='treat_servings', to='pets.pet'),
            preserve_default=False,
        ),
    ]
