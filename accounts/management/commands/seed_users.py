from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User
from django.db import transaction
from user.models import Profile
from django.contrib.auth.hashers import make_password

# class Command(BaseCommand):

#     def add_arguments(self, parser):
#         parser.add_argument('--count',type=int,default=10)

#     @transaction.atomic
#     def handle(self, *args, **options):
        
#         fake = Faker("fa-IR")
#         count = options['count']
#         self.stdout.write(f"Creating {count} users...")
#         default_password = make_password("A/@1234567a")

#         for _ in range(count):

#             User.objects.create(
#                 phone = fake.unique.numerify("09#########"),
#                 first_name = fake.file_name(),
#                 last_name = fake.last_name(),
#                 password = default_password
#             )
        
#         self.stdout.write(self.style.SUCCESS('Done ...'))

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--count',type=int,default=10)

    @transaction.atomic
    def handle(self, *args, **options):
        
        fake = Faker("fa-IR")
        count = options['count']
        self.stdout.write(f"Creating {count} users...")
        default_password = make_password("A/@1234567a")

        users = []
        for _ in range(count):

            users.append(User(
                phone = fake.unique.numerify("09#########"),
                first_name = fake.file_name(),
                last_name = fake.last_name(),
                password = default_password
            ))
        created_users = User.objects.bulk_create(users,batch_size=20)
        
        profiles = []
        for user in created_users:

            profiles.append(
                Profile(
                    user=user,
                    full_name = f'{user.first_name} {user.last_name}',
                    role=Profile.Role.STUDENT
                )
            )
        Profile.objects.bulk_create(profiles,batch_size=20)
        self.stdout.write(self.style.SUCCESS('Done ...'))