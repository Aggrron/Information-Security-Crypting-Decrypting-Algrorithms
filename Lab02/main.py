from base2 import base
from itertools import permutations
import operator

file = open("prob_text.txt","rb")
alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ"
tst1 = "СВПООЗЛУЙЬСТЬ_ЕДПСКОКАОЙЗ"
tst2 = "ДСЛИЕЗТЕА_Ь_ЛЬЮВМИ__АОЧХК"
tst3 = "ОКЕСНВРП_ЫРЕАДЕЫН_В_РСИКО"
tst4 = "НМВИАИ_НЕВЕ_СМСТУОРДИАНКМ"
tst5 = "ЕДСЗЬНДЕ_МУБД_УЭ_КТЗЕМНАЫ"
tst6 = "СОНРЧОУО_ХДТ_ИЕИ_ВЗКАТРРИ"
tst7 =  "_ОНКА_БНЫЕЦВЛЕ_К_ТГОАНЕИР"
tst8 =  "НЗМАЕЕАА_Г_НОТВОССОТЬЯАЛС"
tst9 =  "РППОЕААДТВЛ_ЕБЬЛНЫЕ_ПА_ВР"


def decypher(txt):
  key = 5
  possible_orders = {}
  impossible_orders = []
  for z in range(5):
    buf = txt[z*key:(z*key)+key]
    buf_list = []
    i = 1
    for ch in buf:
      ch = ch + str(i)
      buf_list.append(ch)
      i+=1
    #print(buf_list)
    a = list(permutations(buf_list))
    for word in a:
      summ = count_possibillity(word)
      ord_word = make_word(word)
      if summ !=0:
        # [-][-]
        if not check_order(ord_word, possible_orders) and not check_order(ord_word, impossible_orders):
          add_an_order(ord_word, possible_orders, summ)
        #[+][-]    
        if check_order(ord_word, possible_orders) and not check_order(ord_word, impossible_orders):
            possible_orders[ord_word] += summ       
      else:
        if check_order(ord_word, possible_orders) and not check_order(ord_word, impossible_orders):
          impossible_orders.append(ord_word)
          remove_order(ord_word, possible_orders)
        if not check_order(ord_word, possible_orders) and not check_order(ord_word, impossible_orders):
          impossible_orders.append(ord_word)
        

    sorted_d = sorted(possible_orders.items(),key=operator.itemgetter(1))
    #print(sorted_d)
    #print(z, "----------------------------------------------")
  answers = []
  for key in possible_orders.keys():
    answers.append(sorting(txt,key))
  for d in answers:
    print(d)

def sorting(txt,order):
  key = len(order)
  pr_txt = add_spaces(txt, key)
  ind = 0
  mult = 0
  result = ""
  for z in range(len(pr_txt)):
    if ind == key:
      mult += 1
      ind = 0 
    result += pr_txt[int(order[ind])+(key*mult)-1]
    ind += 1 
  return result

def add_spaces(txt, key):
  for i in range(len(txt)):
    if len(txt)%key!=0:
      txt += "_"
    else:
      break
  return txt






  



  
def count_possibillity(word):
  summ = 0
  j = 0
  for i in word:
    if j!=len(word)-1:
      #print(i, word[j+1])
      if i[0] =="_" or word[j+1][0] == "_":
        if excep(i[0], word[j+1][0]):
          summ = 0
          break
        j+=1
        continue
      else:
        curr_letter_index = get_index(i,alph)
        next_letter_index = get_index(word[j+1],alph)
        if int(base[curr_letter_index][next_letter_index]) == 0:
          summ =0
          break
        summ = summ + int(base[curr_letter_index][next_letter_index])
      #print(sum)
      #print(j)
    else:
      break
    j+=1
  return summ

def excep(ch1,ch2):
  if ch1 == "_" and ch2 =="Ь":
    return True
  if ch1 == "_" and ch2 =="Ы":
    return True

def get_index(letter,alphabet):
  letter = letter[:-1]
  return alphabet.index(letter)


#Order Functions --------------------
def make_word(word):
  result = ""
  for ch in word:
    result += ch[1]
  return result

def add_an_order(word, orders,summ):
  orders[word] = summ

def check_order(word, orders):
  return (word in orders)

def remove_order(word, orders):
  del orders[word]
  #orders.remove(word)

#--------------------------------------------








testing1 = ('С', 'В', 'П', 'О', 'О')
testing2 = ('О', 'С', 'П', 'О', 'В')
testing3 = ('О', 'С', 'В', 'П', 'О')
testing4 = ('В', 'О', 'С', 'П', 'О')

#print(count_possibillity(testing1))
#print(count_possibillity(testing2))
#print(count_possibillity(testing3))
#print(count_possibillity(testing4))

print(decypher(tst1))
print("--------------------------------")
print(decypher(tst2))
print("--------------------------------")
print(decypher(tst3))
print("--------------------------------")
print(decypher(tst4))
print("--------------------------------")
print(decypher(tst5))
print("--------------------------------")
print(decypher(tst6))
print("--------------------------------")
print(decypher(tst7))
print("--------------------------------")
print(decypher(tst8))
print("--------------------------------")
print(decypher(tst9))
print("--------------------------------")









#print(decypher(tst1))


#print(d)
#print(base_alph)
#getStat()

#print(stat)    
