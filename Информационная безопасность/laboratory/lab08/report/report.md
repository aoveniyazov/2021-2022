---
# Front matter
title: "Отчет по лабораторной работе №8"
subtitle: "-"
author: "Овениязов Артур"

# Generic otions
lang: ru-RU
toc-title: "Содержание"

# Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

# Pdf output format
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
### Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Misc options
indent: true
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Освоить на практике применение режима однократного гаммирования на примере кодирования различных исходных текстов одним ключом.

# Задание

Исходные данные.
Две телеграммы Центра:
P1 = НаВашисходящийот1204
P2 = ВСеверныйфилиалБанка
Ключ Центра длиной 20 байт:
K = 05 0C 17 7F 0E 4E 37 D2 94 10 09 2E 22 57 FF C8 OB B2 70 54
Два текста кодируются одним ключом (однократное гаммирование).
Требуется не зная ключа и не стремясь его определить, прочитать оба текста. 
Необходимо разработать приложение, позволяющее шифровать и дешифровать тексты P1 и P2 в режиме однократного гаммирования. Приложение должно определить вид шифротекстов C1 и C2 обоих текстов P1 и
P2 при известном ключе ; 
Необходимо определить и выразить аналитически способ, при котором злоумышленник может прочитать оба текста, не
зная ключа и не стремясь его определить

# Теоретическое введение
Гамми́рование, или Шифр XOR, — метод симметричного шифрования, заключающийся в «наложении» последовательности, состоящей из случайных чисел, на открытый текст. Последовательность случайных чисел называется гамма-последовательностью и используется для зашифровывания и расшифровывания данных.
[@lossit:ggwp]

# Выполнение лабораторной работы
 
Написал следующий код в файле kripto2.py. 

![Код kripto2.ipynb](images/img(1).png){ #fig:001 width=70% }

![Результат выполнения kripto2.py](images/img(2).png){ #fig:002 width=70% }

## Ответы на вопросы 

1. Как, зная один из текстов (P1 или P2), определить другой, не зная при
этом ключа?

С помощью формул режима однократного гаммирования получим
шифротексты обеих телеграмм:

С1 = Р1 xor К,

С2 = Р2 xor К.

Задача нахождения открытого текста по известному шифротексту двух
телеграмм, зашифрованных одним ключом, может быть решена. Сложим по модулю
2 оба равенства, получаем:

С1 xor С2 = Р1 xor К xor Р2 xor К = Р1 xor Р2.

имеем:

С1 xor С2 xor Р1 = Р1 xor Р2 xor Р1 = Р2.

Таким образом, получаем возможность определить те символы сообщения Р2,
которые находятся на позициях известного сообщения Р1. Догадываясь по логике
сообщения Р2, Имеем реальный шанс узнать ещё некоторое количество символов
сообщения Р2. Затем вместо Р1 подставляя новоузнанные символы сообщения Р2. И
так далее. Действуя подобным образом, можно если даже не прочитает оба
сообщения, то значительно уменьшит пространство их поиска.

2. Что будет при повторном использовании ключа при шифровании
текста?

Если на сообщение наложить ключ дважды, мы получим исходное сообщение.

3. Как реализуется режим шифрования однократного гаммирования
одним ключом двух открытых текстов?

Один ключ накладываем на оба открытых текста и получаем два
зашифрованных одним ключом шифротекста.

4. Перечислите недостатки шифрования одним ключом двух открытых
текстов.

Зная текст одного из сообщения можно узнать текст второго, не зная кода.

5. Перечислите преимущества шифрования одним ключом двух открытых
текстов.

Нет необходимости каждый раз придумывать ключи для каждого сообщение.

# Выводы

В ходе данной лабораторной работы я освоил на практике применение
режима однократного гаммирования на примере кодирования различных исходных
текстов одним ключом, разработал приложение, позволяющие шифровать и
дешифровать различные тексты в режиме однократного гаммирования.

# Список литературы{.unnumbered}

::: {#refs}
:::