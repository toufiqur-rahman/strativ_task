from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_language_iso639_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='languages', to='core.country'),
        ),
    ]