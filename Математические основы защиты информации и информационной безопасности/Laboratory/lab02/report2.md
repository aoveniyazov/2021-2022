---
# Front matter 
lang: ru-RU
title: "Лабораторная работа № 2"
subtitle: "Шифры перестановки"
author: "Овениязов Артур НФИмд-02-22 1032225418"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
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

# Лабораторная работа №2

[TOC]

## Цель работы
Освоить на практике написание шифров перестановки. Таких как маршрутное шифрование и шифр методом Виженера 

## Задание

1. Реализовать маршрутное шифрование.

2) Реализовать шифр Виженера.

## Теоретическое введение

Шифр перестано́вки — это метод симметричного шифрования, в котором элементы исходного открытого текста меняют местами. Элементами текста могут быть отдельные символы, пары букв, тройки букв, комбинирование этих случаев и так далее. Типичными примерами перестановки являются анаграммы Простейшим примеров перестановочного шифра являются так называемые «маршрутные перестановки», использующие некоторую геометрическую фигуру (плоскую или объемную). Шифрование **заключается в том, что текст записывается в такую фигуру по некоторой траектории, а выписывается по другой траектории**.

Шифр Виженера (фр. Chiffre de Vigenère) — метод полиалфавитного шифрования буквенного текста с использованием ключевого слова.[1]

Этот метод является простой формой многоалфавитной замены. Шифр Виженера изобретался многократно. Впервые этот метод описал Джовани Баттиста Белласо (итал. Giovan Battista Bellaso) в книге La cifra del. Sig. Giovan Battista Bellasо в 1553 году[2], однако в XIX веке получил имя Блеза Виженера[3], французского дипломата. Метод прост для понимания и реализации, но является недоступным для простых методов криптоанализа.[4]

Хотя шифр легко понять и реализовать, на протяжении трех столетий он противостоял всем попыткам его сломать; чем и заработал имя le chiffre indéchiffrable (фр. неразгаданный шифр). Многие люди пытались реализовать схемы шифрования, которые по сути являлись шифрами Виженера.[5]

## Оборудование

Лабораторная работа выполнялась дома со следующими характеристиками техники: 

– Ryzen 5600X CPU
– ОС Майкрософт Windows 10
– VirtualBox верс. 6.1.26

Код был написан на языке Python3.

Демонстрация работы кода проводилась в продукте Google Colaboratory.

# Выполнение лабораторной работы
## Шифр Цезаря
 1. Реализовал Шифр Маршрутной перестановки. Показала создание нового шифровочного алфавита. В качестве ключа использовал использованные в примере слова 

      (рис. -@fig:001)
      ![Программа](image/rp1.png){ #fig:001 width=100% }

      2. Получил следующую криптограмму.

         (рис. -@fig:002)
         ![Вывод](image/rp2.png){ #fig:002 width=100% }
      

## Шифр Виженера 
1. Реализовал Шифр Виженера. Код будет представлен отдельно, он довольно громоздкий для отчета.

      
      
      2. Вывод программы шифрования Виженера.
      
      (рис. -@fig:001)
      ![Вывод](image/rp3.png){ #fig:001 width=100% }

      Получили вывод в виде исходного слова, шифра и дешифра
      
## Выводы
В ходе данной лабораторной работы, написал 2 программы для шифров перестановки Поняла принцип шифрования и освоила написание шифров маршрута и Вижинера на языке Python.

## Список литературы 

1. Лабораторная работа 2. Шифры перестановки. // Туис URL: https://esystem.rudn.ru/pluginfile.php/1198312/mod_resource/content/2/007-lab_crypto-gamma.pdf (дата обращения: 12.09.2022).

   





