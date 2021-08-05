from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_country_neighbouring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='iso639_1',
            field=models.CharField(max_length=2, null=True),
        ),
    ]