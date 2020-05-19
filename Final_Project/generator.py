from faker import Faker
import json


def generate_data():
    Faker.seed(432)
    data = []
    fake = Faker(['cs_CZ', 'en_GB', 'ru_RU'])
    for _ in range(1000):
        user = ''
        email = ''
        while len(user) < 6 and len(email) < 7:
            user = fake.user_name()
            email = fake.ascii_email()
        data.append({
            'username': user,
            'email': email,
            'password': fake.credit_card_security_code()
        })
    return data


if __name__ == '__main__':
    with open('data.txt', 'w') as f:
        f.write(json.dumps(generate_data()))
