# Generated by Django 2.1.5 on 2019-02-19 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190218_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Subscriber'),
        ),
    ]
