# Generated by Django 2.1.2 on 2020-08-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiry', '0015_auto_20200218_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enq_num',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
