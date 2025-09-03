from faker import Faker


fake = Faker('ru_RU')

int_ = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(18, 100)
}
data = int_

print(data)