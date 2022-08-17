from audioop import reverse


number1 = 10
id(number1)
hong = {
    "score1" : 80,
    "score2" : 75,
    "score3" : 55 
}
avg = sum(list(hong.values()))/len(hong)
print(avg)

# 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
a = "a:b:c:d"
a.replace(":","#")
print(a)

# [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
list1 = [1,3,5,4,2]
list1.sort()
print(list1)
list1.reverse()
print(list1)
str1 = " ".join(['Life', 'is', 'too', 'short'])
print(str1)
tuple1 = (1,2,3)
tuple2 = (4,)
print(tuple1+tuple2)
dica = {'A':90, 'B':80, 'C':70}
dica.pop('B')
list2 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
list3 = list(set(list2))
print(list3)
