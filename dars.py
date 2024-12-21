users = {
    "user1": {
        "name": "",
        "surname": "",
        "phonenumber": "",
        "email": "",
        "birthdate": ""
    }
}

def user_create():
    name = input("Ismingizni kiriting: ")
    surname = input("Familyangizni kiriting: ")
    phonenumber = input("Telefon raqamingizni kiriting: ")
    email = input("Email manzilingizni kiriting: ")
    birthdate = input("Tug'ilgan kuningizni kiriting: ")


    user_id = f"user{len(users) + 1}"

    users[user_id] = {
        "name": name,
        "surname": surname,
        "phonenumber": phonenumber,
        "email": email,
        "birthdate": birthdate
    }

    print(f"Foydalanuvchi {name} {surname} yaratildi! Yangi ID: {user_id}")

user_create()

print(users)
