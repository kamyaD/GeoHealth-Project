# Generated by Django 5.0.6 on 2024-05-13 22:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analysis_reports", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysisreportsdata",
            name="file",
            field=models.FileField(upload_to="reports/analysis-reports/"),
        ),
    ]
