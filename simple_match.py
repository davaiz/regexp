#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = '^a{1}b?$'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '^a{1}[abc]{1}b{1}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = '^s{1}o{1}f{1}i{1}a{1}.{1}m{1}p{1}[34]{1}$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '^.*[^r]$'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '^[ab]{1}[ab]{1}[ab]{1}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '^[Oabk]{6}$'   

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = '^[aA ]{11}$'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc

REGEXP_8 = '^a.*[^1]$'
