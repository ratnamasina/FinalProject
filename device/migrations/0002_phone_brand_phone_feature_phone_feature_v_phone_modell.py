# Generated by Django 3.2.7 on 2021-09-30 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone_brand',
            fields=[
                ('phone_brand_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_brand_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='phone_feature',
            fields=[
                ('phone_feature_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_feature_name', models.CharField(max_length=200)),
                ('phone_brand_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='device.phone_brand')),
            ],
        ),
        migrations.CreateModel(
            name='phone_modell',
            fields=[
                ('phone_model_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_model_name', models.CharField(max_length=200)),
                ('phone_brand_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='device.phone_brand')),
            ],
        ),
        migrations.CreateModel(
            name='phone_feature_v',
            fields=[
                ('phone_feature_v_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_feature_v_value', models.CharField(max_length=200)),
                ('phone_brand_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='device.phone_brand')),
                ('phone_feature_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='device.phone_feature')),
                ('phone_model_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='device.phone_modell')),
            ],
        ),
    ]
