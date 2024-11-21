from faker import Faker

fake = Faker('ko-KR')
Faker.seed()

name = fake.name()

print(name)
