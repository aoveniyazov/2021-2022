---
# Front matter
title: "Отчет по лабораторной работе №7"
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

Освоить на практике применение режима однократного гаммирования.

# Задание

Нужно подобрать ключ, чтобы получить сообщение «С Новым Годом,
друзья!». Требуется разработать приложение, позволяющее шифровать и
дешифровать данные в режиме однократного гаммирования. Приложение должно:
1. Определить вид шифротекста при известном ключе и известном
открытом тексте.
2. Определить ключ, с помощью которого шифротекст может быть
преобразован в некоторый фрагмент текста, представляющий собой один из
возможных вариантов прочтения открытого текста.

# Теоретическое введение
Гамми́рование, или Шифр XOR, — метод симметричного шифрования, заключающийся в «наложении» последовательности, состоящей из случайных чисел, на открытый текст. Последовательность случайных чисел называется гамма-последовательностью и используется для зашифровывания и расшифровывания данных.
[@lossit:ggwp]

# Выполнение лабораторной работы
 
Написал следующий код в файле kripto.py. 


![Код kripto.py](images/img(1).png){ #fig:001 width=70% }

Полученный результат работы приложения:
первая строка соответствует зашифрованной информации, вторая строка – расшифрованному тексту, а третья – ключу.

![Результат выполнения kripto.py](images/img(2).png){ #fig:002 width=70% }

## Ответы на вопросы 

1. Поясните смысл однократного гаммирования.
Принцип гаммирования представляет собой процедуру наложения, при помощи
некой функции G, на входную информационную последовательность гаммы
шифра, т.е. псевдослучайной последовательности.
2. Перечислите недостатки однократного гаммирования.
Недостатки однократного гаммирования заключается в необходимости иметь
огромные объемы данных, которые можно было бы использовать в качестве
гаммы.
3. Перечислите преимущества однократного гаммирования.
Преимущества однократного гаммирования в том, что не может сказать о
дешифровке, верна она или нет из-за равных априорных вероятностей
криптоаналитик. Информация о вскрытом участке гаммы не дает информации об
остальных ее частях.
4. Почему длина открытого текста должна совпадать с длиной ключа?
Так должно быть, потому что мы используем поэлементное перемножение,
чтобы размерность шифртекста была равна размерности открытого текста и
ключа. Также это ее необходимость заключается в том, чтобы шифрование и
расшифрование выполнялось одной и той же программой.
5. Какая операция используется в режиме однократного гаммирования, назовите
её особенности?
В режиме однократного гаммирования используется операция сложения по
модулю 2 (XOR). Двойное прибавление одной и той же величины по модулю 2
восстанавливает исходное значение.
6. Как по открытому тексту и ключу получить шифротекст?
Задача нахождения шифротекста при известном ключе и открытом тексте
состоит в применение следующего правила к каждому символу открытого текста:
Ci = Pi (+) Ki.
7. Как по открытому тексту и шифротексту получить ключ?
Обе части равенства сложим по модулю 2 с Pi.
Ci (+) Pi = Pi (+) Ki (+) Pi = Ki,
Ki = Ci (+) Pi.
8. В чем заключаются необходимые и достаточные условия абсолютной
стойкости шифра?
Необходимые и достаточные условия абсолютной стойкости шифра включают в
себя полную случайность ключа, равенство длин ключа и открытого текста,
однократное использование ключа.

# Выводы

В ходе данной лабораторной работы я освоил применение режима однократного гаммирования на практике, разработал приложение, позволяющее шифровать и дешифровать данные в режиме однократного гаммирования.

# Список литературы{.unnumbered}

::: {#refs}
:::