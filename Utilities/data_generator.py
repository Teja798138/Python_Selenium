import random
import string
from faker import Faker

fake = Faker()

def generate_random_name():
    return fake.first_name() +" " + fake.last_name()

def generate_random_mobile():
    return "9" + "".join(random.choices(string.digits, k=9))