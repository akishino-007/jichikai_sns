from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='akishino').exists():
            User.objects.create_superuser(
                username=os.environ.get('akishino'),
                email='',
                password=os.environ.get('userpw')
            )