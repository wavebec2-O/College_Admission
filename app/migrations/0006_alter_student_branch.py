# Generated by Django 4.2.9 on 2024-07-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_student_dynamic_fields_alter_student_college_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('AIML', 'AIML'), ('Civil', 'Civil'), ('Mech', 'Mech'), ('Mech/Civil', 'Mech/Civil'), ('Mech/AIML', 'Mech/AIML'), ('Mech/ECE', 'Mech/ECE'), ('Mech/CSE', 'Mech/CSE'), ('Civil/AIML', 'Civil/AIML'), ('Civil/ECE', 'Civil/ECE'), ('Civil/CSE', 'Civil/CSE'), ('AIML/ECE', 'AIML/ECE'), ('AIML/CSE', 'AIML/CSE'), ('ECE/CSE', 'ECE/CSE')], max_length=50),
        ),
    ]
