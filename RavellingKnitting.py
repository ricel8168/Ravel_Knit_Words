################ Ravelling & Knitting

def ravel(x):
    hasil = ""
    for i in range(len(x)):
        hasil += x[:i+1]
    return hasil

print(ravel("Purwadhika"))
print(ravel("Digital"))
print(ravel("Coding"))
print(ravel("School"))

# def knit(x):
#     jawaban = ""
#     for i in x:
#         if i not in jawaban:
#             jawaban += i
#     return jawaban
# ################################## STUCK, ga bisa print huruf dobel.
# print(knit("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))
# print(knit("DDiDigDigiDigitDigitaDigital"))
# print(knit("CCoCodCodiCodinCoding"))
# print(knit("SScSchSchoSchooSchool"))


# Syntax
# Following is the syntax for rfind() method −
# obj.rfind(str, beg=0 end=len(string))
# https://www.tutorialspoint.com/python/string_rfind.htm

# p = "PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"
# p1 = p[0]
# mulai = p.rfind(p1)
# print(p[mulai:len(p)])

def knit(x):
    rajut = x ### rajut adalah input X
    rajut1 = rajut[0] ## rajut1 di gunakan untuk mencari huruf kapital dari inputan / index 0
    mulai = rajut.rfind(rajut1) ## Mencari huruf yang kapital dari urutan paling belakang
    return (rajut[mulai:len(rajut)]) 

print(knit("PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika"))
print(knit("DDiDigDigiDigitDigitaDigital"))
print(knit("CCoCodCodiCodinCoding"))
print(knit("SScSchSchoSchooSchool"))
