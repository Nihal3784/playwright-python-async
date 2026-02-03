import random
import string
import uuid


def generate_random_lead_data(text_length: int = 20) -> dict:
    uid = uuid.uuid4().hex[:6]

    return {
        "name": f"Lead_{uid}",
        "email": f"user_{uid}@gmail.com",
        "mobile": f"9{random.randint(100000000, 999999999)}",
        "text": ''.join(random.choices(string.ascii_letters, k=text_length))
    }
