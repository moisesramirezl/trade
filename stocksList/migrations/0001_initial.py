# Generated by Django 3.0.6 on 2020-05-25 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nemos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nemo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True,
                                            max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStocks',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                              primary_key=True, serialize=False, to='stocksList.Users')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(
                    decimal_places=2, default=0, max_digits=10)),
                ('tax', models.DecimalField(
                    decimal_places=2, default=0, max_digits=10)),
                ('purchase_date', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('nemo_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='stocksList.Nemos')),
            ],
        ),
    ]
