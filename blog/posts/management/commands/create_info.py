from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from posts.models import Post

fake = Faker()


class Command(BaseCommand):
    help = """the command generates a fake posts, 
            if you do not specify a parameter, by default 10 posts are generated"""

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=10)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            create_post = Post.objects.create(
                title=fake.sentence(nb_words=4),
                content=fake.text(),
                updated_at=fake.date_time(),
            )

            self.stdout.write(
                self.style.SUCCESS(f"Все прошло успешно! ({create_post.id})")
            )
