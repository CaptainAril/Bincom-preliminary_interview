# Generated by Django 4.2.6 on 2023-10-20 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='announced_lga_results',
            fields=[
                ('result_id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField(max_length=11)),
                ('entered_bu_user', models.CharField(max_length=255, null=True)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'announced_lga_results',
            },
        ),
        migrations.CreateModel(
            name='announced_pu_results',
            fields=[
                ('result_id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('polling_unit_uniqueid', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField(max_length=11)),
                ('entered_bu_user', models.CharField(max_length=255, null=True)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'announced_pu_results',
            },
        ),
        migrations.CreateModel(
            name='lga',
            fields=[
                ('uniqeid', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('lga_id', models.IntegerField(max_length=11)),
                ('lga_name', models.CharField(max_length=50)),
                ('lga_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'lga',
            },
        ),
        migrations.CreateModel(
            name='party',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('party_id', models.CharField(max_length=11)),
                ('party_name', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'party',
            },
        ),
        migrations.CreateModel(
            name='states',
            fields=[
                ('state_id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='ward',
            fields=[
                ('uniqueid', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('ward_id', models.IntegerField(max_length=11)),
                ('ward_name', models.CharField(max_length=50)),
                ('ward_description', models.TextField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=50)),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.lga')),
            ],
            options={
                'db_table': 'ward',
            },
        ),
        migrations.CreateModel(
            name='polling_unit',
            fields=[
                ('uniqueid', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField(max_length=11)),
                ('uniquewardid', models.IntegerField(max_length=11, null=True)),
                ('polling_unit_number', models.CharField(max_length=50, null=True)),
                ('polling_unit_name', models.CharField(max_length=50, null=True)),
                ('polling_unit_description', models.TextField()),
                ('lat', models.CharField(max_length=255, null=True)),
                ('long', models.CharField(max_length=255, null=True)),
                ('entered_bu_user', models.CharField(max_length=255, null=True)),
                ('date_entered', models.DateTimeField(null=True)),
                ('user_ip_address', models.CharField(max_length=50, null=True)),
                ('lga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.lga')),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.ward')),
            ],
            options={
                'db_table': 'polling_unit',
            },
        ),
        migrations.AddField(
            model_name='lga',
            name='state_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.states'),
        ),
    ]