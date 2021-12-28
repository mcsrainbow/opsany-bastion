# Generated by Django 2.2.6 on 2020-10-09 10:25

from django.db import migrations
from bastion.utils.init_action_v2 import add_action_to_system


def run_init(apps, schema_editor):
    add_action_to_system()


class Migration(migrations.Migration):

    dependencies = [
        ('bastion', '0005_init_iam_action'),
    ]

    operations = [
        migrations.RunPython(run_init)
    ]