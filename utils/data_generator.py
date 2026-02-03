from faker import Faker
import random

fake = Faker("en_IN")


def generate_lead_data():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "mobile": f"+91 {random.randint(70000, 99999)}-{random.randint(10000, 99999)}"
    }
