# Generated by Django 3.0.8 on 2020-08-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_product_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Lifestyle', 'Lifestyle'), ('Kitchen', 'Kitchen'), ('Fashion', 'Fashion'), ('Beauty', 'Beauty'), ('Study', 'Study')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]