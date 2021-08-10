

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_auto_20180318_1054'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Members',
        ),
    ]
