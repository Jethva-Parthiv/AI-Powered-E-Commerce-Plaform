from django.core.management.base import BaseCommand
from products.models import Product
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seed the database with fake products"

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = ["Electronics", "Books", "Clothing", "Home", "Sports"]

        for _ in range(30):  # generate 30 products
            name = fake.word().capitalize() + " " + random.choice(["Pro", "Max", "Lite", "Book", "Plus"])
            description = fake.sentence(nb_words=12)
            category = random.choice(categories)
            price = round(random.uniform(100, 100000), 2)
            stock = random.randint(1, 50)
            tags = ",".join(fake.words(nb=3))

            Product.objects.create(
                name=name,
                description=description,
                category=category,
                price=price,
                stock=stock,
                tags=tags,
                image="products/default.jpg"  # use a placeholder image
            )

        self.stdout.write(self.style.SUCCESS("✅ Successfully added 30 fake products!"))
