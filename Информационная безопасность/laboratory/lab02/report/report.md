---
# Front matter
title: "Отчет по лабораторной работе №2"
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

Получение практических навыков работы в консоли с атрибутами файлов, закрепление теоретических основ дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux

# Задание

Лабораторная работа подразумевает практическое исследование дискреционных разграничений в современных системах с открытым кодом на базе ОС Linux

# Теоретическое введение

В Linux, как и в любой многопользовательской системе, абсолютно естественным образом возникает задача разграничения доступа субъектов — пользователей к объектам — файлам дерева каталогов.
Один из подходов к разграничению доступа — так называемый дискреционный (от англ, discretion — чье-либо усмотрение) — предполагает назначение владельцев объектов, которые по собственному усмотрению определяют права доступа субъектов (других пользователей) к объектам (файлам), которыми владеют.
Дискреционные механизмы разграничения доступа используются для разграничения прав доступа процессов как обычных пользователей, так и для ограничения прав системных программ в (например, служб операционной системы), которые работают от лица псевдопользовательских учетных записей.
[@lossit:ggwp]

# Выполнение лабораторной работы 

Создал учетную запись guest и задал ей пароль

![Создание учетной записи](images/img(1).png){ #fig:001 width=70% }

Выполнил вход в систему от имени пользователя guest

![Вход в систему](images/img(2).png){ #fig:002 width=70% }

Определил директорию где я нахожусь командой pwd. Нахожусь в домашней директории

![Результат pwd](images/img(3).png){ #fig:003 width=70% }

Уточнил имя текущего пользователя командой whoami.

![Результат whoami](images/img(4).png){ #fig:004 width=70% }

Уточнил имя пользователя, его группу, а также группы, куда входит пользователь, командой id и groups. Выведенные значения uid, gid и др. запомнил и сравнил вывод команд. Выводы одинаковы, оба говорят о группе guest.

![Результат id и groups](images/img(5).png){ #fig:005 width=70% }

Просмотрел файл /etc/passwd командой cat /etc/passwd. Нашел в нём свою учётную запись, определил uid пользователя.
Определил gid пользователя. Сравнил найденные значения с полученными в предыдущих пунктах. Отфильтровал результат с помощью grep.

![Результат /etc/passwd | grep guest](images/img(6).png){ #fig:006 width=70% }

Определил существующие в системе директории командой ls -l /home/ и проверил, какие расширенные атрибуты установлены на поддиректориях, находящихся в директории /home, командой: lsattr /home/. Посмотрел директорию, но lsattr отказал в доступе.

![Результат ls -l и lsattr /home/](images/img(7).png){ #fig:007 width=70% }

Создал в домашней директории поддиректорию dir1 командой mkdir dir1. Определил командами ls -l и lsattr, какие права доступа и расширенные атрибуты были выставлены на директорию dir1.

![Результат mkdir dir1, ls-l и lsattr](images/img(8).png){ #fig:008 width=70% }

Снял с директории dir1 все атрибуты командой chmod 000 dir1 и проверил её правильность выполнения командой ls -l

![Результат chmod 000 dir1 и ls -l](images/img(9).png){ #fig:009 width=70% }

Попытался создать в директории dir1 файл file1 командой echo "test" > /home/guest/dir1/file1. Попытка неудачна.

![Результат echo "test" > /home/guest/dir1/file1](images/img(10).png){ #fig:010 width=70% }

Заполнил таблицу «Установленные права и разрешённые действия» (см. табл. 1.1) и на основании заполненной таблицы определил те или иные минимально необходимые права для выполнения операций внутри директории
dir1, заполнил табл. 1.2.
[-@tbl:1.1]
[-@tbl:1.2]
#Таблицы

: Установленные права и разрешённые действия  {#tbl:1.1}

| Права директо рии | Права файла      | Создание файла | Удаление файла | Запись в файл | Чтение файла | Смена директории | Просмотр файлов в директории | Переименование файла | Смена атрибутов файла |   |   |   |
|-------------------|------------------|----------------|----------------|---------------|--------------|------------------|------------------------------|----------------------|-----------------------|---|---|---|
| d--------(000)    | ---------- (000) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | ---------- (000) | -              | -              | -             | -            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | ---------- (000) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(300)    | ---------- (000) | +              | +              | -             | -            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-------(400)    | ---------- (000) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-x-----(500)    | ---------- (000) | -              | -              | -             | -            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drw------(600)    | ---------- (000) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drwx-----(700)    | ---------- (000) | +              | +              | -             | -            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--------(000)    | --x------- (100) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | --x------- (100) | -              | -              | -             | -            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | --x------- (100) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(300)    | --x------- (100) | +              | +              | -             | -            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-------(400)    | --x------- (100) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-x-----(500)    | --x------- (100) | -              | -              | -             | -            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drw------(600)    | --x------- (100) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drwx-----(700)    | --x------- (100) | +              | +              | -             | -            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--------(000)    | -w--------(200)  | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | -w--------(200)  | -              | -              | +             | -            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | -w--------(200)  | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(030)    | -w--------(200)  | +              | +              | +             | -            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d---r----(040)    | -w--------(200)  | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d---r-x--(050)    | -w--------(200)  | -              | -              | +             | -            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d---rw---(060)    | -w--------(200)  | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d---rwx--(070)    | -w--------(200)  | +              | +              | +             | -            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--------(000)    | -wx-------(300)  | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | -wx-------(300)  | -              | -              | +             | -            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | -wx-------(300)  | -              | -              | -             | -            |                  | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(300)    | -wx-------(300)  | +              | +              | +             | -            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-------(400)    | -wx-------(300)  | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-x-----(500)    | -wx-------(300)  | -              | -              | +             | -            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drw------(600)    | -wx-------(300)  | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drwx-----(700)    | -wx-------(300)  | +              | +              | +             | -            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--------(000)    | r--------- (400) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | r--------- (400) | -              | -              | -             | +            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | r--------- (400) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(300)    | r--------- (400) | +              | +              | -             | +            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-------(400)    | r--------- (400) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-x-----(500)    | r--------- (400) | -              | -              | -             | +            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drw------(600)    | r--------- (400) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drwx-----(700)    | r--------- (400) | +              | +              | -             | +            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--------(000)    | r-x-------(500)  | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | r-x-------(500)  | -              | -              | -             | +            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | r-x-------(500)  | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(300)    | r-x-------(500)  | +              | +              | -             | +            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-------(400)    | r-x-------(500)  | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-x-----(500)    | r-x-------(500)  | -              | -              | -             | +            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drw------(600)    | r-x-------(500)  | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drwx-----(700)    | r-x-------(500)  | +              | +              | -             | +            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--------(000)    | rw-------- (600) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | rw-------- (600) | -              | -              | +             | +            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | rw-------- (600) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(300)    | rw-------- (600) | +              | +              | +             | +            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-------(400)    | rw-------- (600) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-x-----(500)    | rw-------- (600) | -              | -              | +             | +            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drw------(600)    | rw-------- (600) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drwx-----(700)    | rw-------- (600) | +              | +              | +             | +            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--------(000)    | rwx------- (700) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d--x-----(100)    | rwx------- (700) | -              | -              | +             | +            | +                | -                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d-w------(200)    | rwx------- (700) | -              | -              | -             | -            | -                | -                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| d----wx--(300)    | rwx------- (700) | +              | +              | +             | +            | +                | -                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-------(400)    | rwx------- (700) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| dr-x-----(500)    | rwx------- (700) | -              | -              | +             | +            | +                | +                            | -                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drw------(600)    | rwx------- (700) | -              | -              | -             | -            | -                | +                            | -                    | -                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |
| drwx-----(700)    | rwx------- (700) | +              | +              | +             | +            | +                | +                            | +                    | +                     |   |   |   |
|                   |                  |                |                |               |              |                  |                              |                      |                       |   |   |   |

: Минимально необходимые права для выполнения операций  {#tbl:1.2}

| Операция               | Минимальные права на директорию | Минимальные права на файл |
|------------------------|---------------------------------|---------------------------|
| Создание файла.        | d-wx------ (300)                | ----------(000)           |
| Удаление файла         | d-wx------ (300)                | ----------(000)           |
| Чтение файла           | d--x------ (100)                | r---------(400)           |
| Запись в файл          | d--x------ (100)                | -w--------(200)           |
| Переименование файла   | d-wx------ (300)                | ----------(000)           |
| Создание поддиректории | d-wx------ (300)                | ----------(000)           |
| Удаление поддиректории | d-wx------ (300)                | ----------(000)           |



# Выводы

Сегодня я приобрел практические навыки работы в консоли с атрибутами файлов, закрепил теоретические основы дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux

# Список литературы{.unnumbered}

::: {#refs}
:::
