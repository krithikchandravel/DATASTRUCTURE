details=["9751302862F0693","3888560693F7262","5485983835F0649","2580974299F6042","9976672161M6561","0234451011F8013","4294552179O6482"]
count=0
inte={"M","F"}
for words in details:
    int_numbers=int(words[-4:-2])
    if int_numbers>=60:
        count+=1
print(count)

