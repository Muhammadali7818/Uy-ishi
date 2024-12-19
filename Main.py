
books = {
    "Men": {
        "Nomi": "Men",
        "Narxi": "15$",
        "Tasnif": "lorem",
        "Soni": "5",
        "Mualifi": "Fatih Duman",
        "Qiymati": 15
    },
    "Sen": {
        "Nomi": "Sen",
        "Narxi": "12$",
        "Tasnif": "lorem",
        "Soni": "1",
        "Mualifi": "Fatih Duman",
        "Qiymati": 12
    }
}

while True:
    kitob = input("Kitob nomini kiriting: ")

    if kitob in books:
        text = f"Kitob nomi: {kitob}\n"
        for key, value in books[kitob].items():
            text += f"{key}: {value}\n"
        print(text)

        kitob_sotib_olmoqchimisiz = input(f"kitobini sotib olmoqchimisiz? (Ha yoki Yo'q): ")

        if kitob_sotib_olmoqchimisiz == "ha":
            soni = int(input(f"Nechta olasiz: "))  
            jami_narx = (books[kitob]["Narxi"])  

            if soni <= int(books[kitob]["Soni"]):  
                
                books[kitob]["Soni"] = str(int(books[kitob]["Soni"]) - soni)

                print(f"\nSiz {soni} nusxa {kitob} kitobini sotib oldingiz!")
                print(f"Jami to'lov: {jami_narx}")
                print(f"Qolgan soni: {books[kitob]['Soni']}")
            else:
                print("Kitobning yetarli nusxalari mavjud emas!")

        elif kitob_sotib_olmoqchimisiz == "yo'q":
            print("Sotib olishdan voz kechdingiz.")
    
    else:
        print("Bunday kitob mavjud emas.")
        kitob_kiritmoqchimisiz = input("Kitob kiritmoqchimisiz (Ha yoki Yo'q)? ")

        if kitob_kiritmoqchimisiz == "ha" or kitob_kiritmoqchimisiz == "xa":
            nomi = input("Kitob nomini kiriting: ")
            narx = input("Kitob narxini kiriting: ")
            tasnifi = input("Kitob tasnifi kiriting: ")
            mualifi = input("Kitob mualifini kiriting: ")
            soni = input("Kitob soni kiriting: ")



            books[nomi] = {
                "Nomi": nomi,
                "Narxi": f"{narx}$",
                "Tasnif": tasnifi,
                "Soni": str(soni),
                "Mualifi": mualifi,
            }

            print("Kitob saqlandi!")
            print(f"\nYangi kitob ma'lumotlari:")
            for key, value in books[nomi].items():
                print(f"{key}: {value}")
        
        elif kitob_kiritmoqchimisiz  == "yo'q":
            print("Yaxshi, dastur yopildi.")
            break
