from faker import Faker
from faker.providers import internet

fake = Faker()
ip = fake.ipv6(network = False)

print(ip)