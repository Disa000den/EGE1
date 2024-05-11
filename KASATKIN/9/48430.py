# В каждой строке электронной таблицы записаны шесть натуральных чисел. Определите, сколько в таблице строк, для которых выполнены следующие условия:
#
# — в строке встречается ровно четыре различных числа; два из них по два раза,
#
# два— по одному;
#
# — сумма повторяющихся чисел (без учёта повторений, то есть каждое число входит в сумму один раз) меньше суммы неповторяющихся.
#
# В ответе запишите число— количество строк, для которых выполнены эти условия.

f = open('48430.txt')
cnt = 0
for s in f:
    a = sorted(int(x) for x in s.split())
    repeat = [x for x in a if a.count(x) == 2]
    nonrepeat = [x for x in a if a.count(x) == 1]
    if len(repeat) == 4 and len(nonrepeat) == 2 and sum(repeat) // 2 < sum(nonrepeat):
        cnt += 1
print(cnt)