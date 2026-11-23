from decimal import Decimal
from django.core.management.base import BaseCommand
from products.models import Product

SAMPLE_PRODUCTS = [
    {
        "name": "Wireless Headphones",
        "description": "Premium Bluetooth over-ear wireless headphones with active noise cancellation and up to 30 hours of battery life.",
        "category": "Electronics",
        "price": Decimal("2999.00"),
        "stock": 20,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Bluetooth Speaker",
        "description": "Portable waterproof Bluetooth speaker with deep bass, 360-degree sound, and 12-hour playtime.",
        "category": "Electronics",
        "price": Decimal("1999.00"),
        "stock": 35,
        "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Laptop Backpack",
        "description": "Durable water-resistant backpack featuring a padded sleeve for up to 15.6-inch laptops and anti-theft design.",
        "category": "Accessories",
        "price": Decimal("1499.00"),
        "stock": 25,
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Smart Watch",
        "description": "Fitness tracking smartwatch with heart rate monitor, sleep tracking, AMOLED display, and 7-day battery life.",
        "category": "Electronics",
        "price": Decimal("3999.00"),
        "stock": 15,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Cotton T-Shirt",
        "description": "100% organic breathable cotton crewneck t-shirt with modern regular fit and premium comfort.",
        "category": "Clothing",
        "price": Decimal("699.00"),
        "stock": 50,
        "image_url": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Running Shoes",
        "description": "Lightweight athletic running shoes engineered with responsive cushioning and breathable mesh upper.",
        "category": "Clothing",
        "price": Decimal("2499.00"),
        "stock": 30,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Coffee Mug",
        "description": "Ceramic matte finish coffee mug with ergonomic handle and 350ml capacity. Microwave and dishwasher safe.",
        "category": "Home",
        "price": Decimal("349.00"),
        "stock": 60,
        "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Python Programming Book",
        "description": "Comprehensive guide to mastering Python for web development, automation, data science, and cloud applications.",
        "category": "Books",
        "price": Decimal("799.00"),
        "stock": 40,
        "image_url": "https://images.unsplash.com/photo-1532012164546-f432f2e3edd4?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "USB-C Cable",
        "description": "Braided fast-charging 100W USB-C to USB-C cable with durable aluminum connectors and 2-meter length.",
        "category": "Accessories",
        "price": Decimal("299.00"),
        "stock": 100,
        "image_url": "https://images.unsplash.com/photo-1588508065123-287b28e013da?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
    {
        "name": "Wireless Mouse",
        "description": "Ergonomic 2.4GHz optical wireless mouse with silent clicks, adjustable DPI, and long battery life.",
        "category": "Electronics",
        "price": Decimal("899.00"),
        "stock": 45,
        "image_url": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=600&auto=format&fit=crop&q=80",
        "is_active": True,
    },
]

class Command(BaseCommand):
    help = "Seed database with 10 sample products across multiple categories"

    def handle(self, *args, **options):
        self.stdout.write("Seeding sample products...")
        created_count = 0
        updated_count = 0

        for item in SAMPLE_PRODUCTS:
            product, created = Product.objects.update_or_create(
                name=item["name"],
                defaults=item
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded products: {created_count} created, {updated_count} updated."
            )
        )
