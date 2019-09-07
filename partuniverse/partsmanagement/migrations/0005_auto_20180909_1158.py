# Generated by Django 2.1.1 on 2018-09-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("partsmanagement", "0004_verifiedstock_comment")]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="comment",
            field=models.TextField(
                blank=True,
                help_text="Optional: A short conclusion.",
                max_length=200,
                null=True,
                verbose_name="Comment",
            ),
        )
    ]
