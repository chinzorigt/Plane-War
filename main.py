import re
import codecs
f = codecs.open("text.html", 'r', encoding = 'UTF-8')
fw = open("garalt.out", "w", encoding='UTF-8')
dic = {
    'АР': 0,
    'БӨ': 0,
    'БХ': 0,
    'БУ': 0,
    'ГА': 0,
    'ГС': 0,
    'ДА': 0,
    'ДГ': 0,
    'ДО': 0,
    'ДУ': 0,
    'ЗА': 0,
    'ОР': 0,
    'ӨВ': 0,
    'ӨМ': 0,
    'СБ': 0,
    'СЭ': 0,
    'ТӨ': 0,
    'УВ': 0,
    'УБ': 0,
    'УН': 0,
    'ХО': 0,
    'ХӨ': 0,
    'ХЭ': 0
}
k, v = list(dic.keys()), list(dic.values())
for line in f:
    for i in re.findall(r'\d{4}\W*[АБГДЗОӨСТУХ][РӨХУАСГОВМБЭН]\w+',line):
        for j in k:
            if(j in i):
                v[k.index(j)] += 1
print(v)
f.close()