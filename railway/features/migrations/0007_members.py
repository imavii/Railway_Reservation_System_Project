

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('features', '0006_delete_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
    ]
