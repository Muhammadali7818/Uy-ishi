# sonlar1 = [12, 72, 63, 32, 13]
# sonlar2 = [12, 38, 41, 50, 19]
# toq_sonlar = []
# juft_sonlar = []
# for i in sonlar1:
#      if sonlar1[i] % 2 == 0:
#         toq_sonlar.append(sonlar1[i])
#      else:
#         toq_sonlar.append(sonlar1[i])

# for i in sonlar2.__le__:
#      if sonlar2[i] % 2 == 0:
#         toq_sonlar.append(sonlar2[i])
#      else:
#         toq_sonlar.append(sonlar2[i])

# print(toq_sonlar)

sonlar1 = [12, 72, 63, 32, 13]
sonlar2 = [12, 38, 41, 50, 19]
toq_sonlar = []
juft_sonlar = []


for i in sonlar1:
    if i % 2 == 0:
        juft_sonlar.append(i)
    else:
        toq_sonlar.append(i)

for i in sonlar2:
    if i % 2 == 0:
        juft_sonlar.append(i)
    else:
        toq_sonlar.append(i)


print("Toq sonlar:", toq_sonlar)
print("Juft sonlar:", juft_sonlar)