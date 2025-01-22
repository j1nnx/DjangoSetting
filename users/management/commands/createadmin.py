from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        user = User.objects.create(
            email='testneykerez@gmail.com',
            first_name='Admin',
            last_name='Test',
        )

        user.set_password('89379540780A')

        user.is_staff = True
        user.is_superuser = True

        user.save()

        self.stdout.write(self.style.SUCCESS(f'User {user.email} created successfully.'))
