# Generated by Django 2.1.7 on 2019-03-02 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('composition', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('exp_date', models.DateField(blank=True, help_text='dd/mm/yyyy', null=True)),
                ('demand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Demand')),
                ('drug_stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.DrugStock')),
                ('supply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Supply')),
            ],
        ),
        migrations.CreateModel(
            name='DrugCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(blank=True, choices=[('I', 'Injection'), ('O', 'Oral'), ('T', 'Tablet'), ('S', 'Syrup'), ('C', 'Cream'), ('L', 'Liquid')], max_length=1, null=True)),
                ('nature', models.CharField(blank=True, choices=[('D', 'Depressants'), ('S', 'Stimulants'), ('H', 'Hallucinogens'), ('O', 'Opioids'), ('I', 'Inhalants'), ('C', 'Cannabis')], max_length=1, null=True)),
                ('disease', models.CharField(blank=True, choices=[('D', 'Digestive_system'), ('B', 'Body_pain'), ('E', 'Eye'), ('S', 'Skin'), ('A', 'Alergy'), ('F', 'Fever'), ('CL', 'Cold'), ('C', 'Cough'), ('D', 'Diabetes'), ('R', 'Respiratory_System'), ('V', 'Vitamins'), ('EN', 'Ear,Nose,oropharynx'), ('O', 'Other')], max_length=2, null=True)),
                ('availability', models.CharField(blank=True, choices=[('P', 'prescription_drug'), ('NP', 'On_the_counter_medicine')], max_length=2, null=True)),
                ('drug', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='drugs.Drug')),
            ],
        ),
    ]
