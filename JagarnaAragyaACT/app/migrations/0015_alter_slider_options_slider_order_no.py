# Generated by Django 4.2.2 on 2023-07-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_uburl_contact_yburl'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='slider',
            name='order_no',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]