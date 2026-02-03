import random
import string


def generate_campaign_name(prefix="auto"):
    random_text = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{prefix}_{random_text}"


def generate_lead_status_name(prefix="lead"):
    random_text = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{prefix}{random_text}"


def generate_role_name(prefix="lead"):
    random_text = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{prefix}{random_text}"


def generate_template_name(prefix="tpl", length=6):
    suffix = ''.join(random.choices(string.ascii_lowercase, k=length))
    return f"{prefix}_{suffix}"


def random_campaign_name(prefix="j"):
    random_text = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{prefix}{random_text}"


def random_excel_name(prefix="excel"):
    suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"{prefix}{suffix}"


def random_text(prefix, length=6):
    return prefix + "" + ''.join(random.choices(string.ascii_lowercase, k=length))


def random_rate():
    return str(random.randint(1000, 9999))


def random_hsn():
    return str(random.randint(100000, 999999))
