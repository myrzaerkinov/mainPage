# Generated by Django 4.0.3 on 2022-05-29 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_accounts', '0003_businessaccount_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salonreview',
            name='salon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salon_reviews', to='business_accounts.businessaccount'),
        ),
    ]
