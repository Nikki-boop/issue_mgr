from django.db import migrations

def populate_roles(apps, schemaeditor):
    entries = {
        "product owner": "Team member who defines requirements",
        "developer": "Team member who works on issues",
        "scrum master": "Team's coach"
    }
    Role = apps.get_model("accounts", "Role")
    for k, v in entries.items():
        role_obj = Role(name=k, description = v)
        role_obj.save()



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_roles)
    ]