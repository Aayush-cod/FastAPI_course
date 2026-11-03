from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

hashed = pwd_context.hash('sec')

print(hashed)
print(pwd_context.verify('sec', hashed))