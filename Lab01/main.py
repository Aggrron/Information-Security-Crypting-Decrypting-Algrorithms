# Подсчет букв в тексте ---------------
import random
cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alph = {}
for c in cyrillic:
  alph[c.upper()] = 0
f = open("lel.txt", "r")
#print(alph)

def read():
  while True:
    ch = f.read(1)
    print(ch)
    if not ch:
      print("End")
      break

def freq():
  while True:
    ch = f.read(1)
    if ch in alph:
      alph[ch]+=1
    if not ch:
      break
  print(alph)
print("Подсчет букв в тексте:")
freq()
#----------------------------------

#Шифр замены тут тип заменяются буквы в строке из строки т1 на букву в той же позиции строки т2
def swapCipher(cipher):
  t1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
  #t2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
  #t2 = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"
  t2 = "ЯЮЭЬЫЪЩШЧЦЧФУТСРПОНМЛКЙИЗЖЁЕДГВБА_"
  #t3 = "АБВГДЕЁЖЗИЙКЛМНОПХВТУЕХЦЧРЩЪЫЬЭЮЯ"
  result = ""
  for c in cipher:
    if c in t1:
      ind = t1.index(c)
      result += t2[ind]
  return "Result: "  + result

def jopa(txt):
  result = ""
  for ch in txt:
    if ch==" ":
      result+= "_"
    else:
      result += ch
  return result

txt1 = "ЧЙШ_ЧЛГГЯ_ТУ_ДЦЙ_ФСЯО_ЛДСОИЩ_ЕМЧ_ШУШЫФ_ЧФДРЕ_ССФШР_РЫАТ_ТЬЫО_МЗ_КЫС_ШНЛЕД_ШГИШ_ВФТЛ_ЩК_ЗПВДЯН_ЛЕРН_Т_ЙЕЙРОЕ_КЛЯ_ЙЩЯ_ЛЕН_ВРПЕШШ_ЩЗЬПНДВТ_УЫ_ЩШЫ_ИРЙЕ_ГЯА_ФЧЛЙЕ_ЬСПАП_НСГ_С_ВСА_ШЛЕТ_ЗЙ_ЙЗП_ШЙ_КТСФ_НЛМО_ОПЕ_ЗЦЬЧ_ЬВ_УЕЧЗЦ_ЫН_ДЙУЬЦЙМИСЫ_ФИШЕ_СРО"

print("Шифр Замены:")
print(swapCipher(txt1))
#----------------------------

#Шифр вижинера--------------------
def visionerCipher(text,key):
  alph2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
  result = ""
  key_index = 0
  for c in text:
    alphHor = splitString(alph2,key[key_index])
    result += alphHor[alph2.index(c)]
    key_index += 1
    if key_index > len(key)-1:
      key_index = 0
  return result
    

def splitString(text, key):
  res = text.split(key)
  result = key + res[1] + res[0]
  return result

row_key = 5
def swapRowCipher(text, key):
  #key_swap = randomRowSwapKey(key)
  key_swap = [1,4,0,2,3]
  result = ""
  buf_dict = {}
  ch_index = 0
  print("Key swap: ")
  print(key_swap)
  for c in text:
    buf_dict[c] = key_swap[ch_index]
    if ch_index == key-1 or c==text[-1]:
      sorted_text = sortDict(buf_dict)
      for x in sorted_text:
        result += x[0]
      ch_index = 0 
      buf_dict = {}
    ch_index+=1
    
  return result

  
  
def sortDict(buff_dict):
  return sorted(buff_dict.items(), key=lambda x: x[1])
  
def randomRowSwapKey(key):
  t = []
  for i in range(key):
    t.append(i)
  random.shuffle(t)
  return t

print("Шифр вижинера:")
di2 = {"a":4,"b":1,"c":8,"d":3}
di = {1:5,4:2,6:8,9:1}
#print(sortDict(di2))
text_swap = "ВОСПОЛЬЗУЙТЕСЬ_ПОДСКАЗКОЙ"
#print(swapRowCipher(text_swap, row_key))    

t1 = "УДАВЗАГЛАТЫВАЕТСВОЮЖЕРТВУЦЕЛИКОМНЕЖУЯ"
key = "СЛОН"


print(visionerCipher(t1, key))
#print(swapRowCipher("efoke",row_key))

#print(randomRowSwapKey(7))


#print(swapCipher("ДЕТИОСТЕРЕГАЙТЕСЬБАОБАБОВ"))
#print(swapCipher("ГДЩЪХЦЧЛМНОБЖВУПЭЮЕЁЯРСИЙКЫЬЗТАФШ"))
#print(swapCipher("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"))


alph2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#print(splitString(alph2, "Р"))



