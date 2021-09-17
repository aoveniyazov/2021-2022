---
# Front matter
title: "Отчет по лабораторной работе №1"
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

Приобретение практических навыков установки операционной системы на виртуальную машину, 
настройки минимально необходимых для дальнейшей работы сервисов.

# Задание

Лабораторная работа подразумевает установку на виртуальную машину VirtualBox (https://www.virtualbox.org/) операционной системы
Linux, дистрибутив Centos

# Теоретическое введение

CentOS ( от англ. Community ENTerprise Operating System) — дистрибутив Linux, основанный на коммерческом Red Hat Enterprise Linux компании Red Hat и совместимый с ним. 
Согласно жизненному циклу Red Hat Enterprise Linux (RHEL), CentOS 5, 6 и 7 будут поддерживаться «до 10 лет», поскольку они основаны на RHEL. Ранее версия CentOS 4 поддерживалась семь лет.
Red Hat Enterprise Linux состоит из свободного ПО с открытым кодом, но доступен в виде дисков с бинарными пакетами только для платных подписчиков. 
Как требуется в лицензии GPL и других, Red Hat предоставляет все исходные коды. Разработчики CentOS используют данный исходный код для создания окончательного продукта, очень близкого к Red Hat Enterprise Linux и доступного для загрузки.
CentOS использует программу Yum для загрузки и установки обновлений из репозитория CentOS Mirror Network, тогда как Red Hat Enterprise Linux получают обновления с серверов Red Hat Network. 
CentOS до версии 5.0 для обновлений использовал также программу up2date
Выполнение работы возможно как в дисплейном классе факультета
физико-математических и естественных наук РУДН, так и дома.

Работу выполнял на домашнем компьютере с операционной системой Windows 10, поэтому некоторые пункты сильно отличаются,
в частности начальная установка с терминала и скачка образа виртуальной машины.
Более подробно о CentO см. в [@wiki:centos].

# Выполнение лабораторной работы

Запустил виртуальную машину и проверил в свойствах месторасположение каталога для виртуальных машин. Установил необходимый.

![рисунок1](img(1).png){ #fig:001 width=70% }

![рисунок2](img(2).png){ #fig:002 width=70% }

Создал новую виртуальную машину Centos(Base), тип операционной системы Linux, дистрибутив RedHat. 

![рисунок3](img(3).png){ #fig:003 width=70% }

Указал 4096МБ основной памяти, так как мой ноутбук позволяет.

![рисунок4](img(4).png){ #fig:004 width=70% }

Задал конфигурацию жесткого диска - загрузочный, VDI(VirtualBox Disk Image), динамический виртуальный диск.

![рисунок5](img(5).png){ #fig:005 width=70% }

![рисунок6](img(6).png){ #fig:006 width=70% }

![рисунок7](img(7).png){ #fig:007 width=70% }

Задал размер виртуального диска - 40гб

![рисунок8](img(8).png){ #fig:008 width=70% }

Проверил месторасположение папки для снимков виртуальной машины, а далее добавил новый привод оптических дисков, и выбрал образ системы Centos.

![рисунок9](img(10).png){ #fig:009 width=70% }

![рисунок10](img(11).png){ #fig:010 width=70% }

Запустил виртуальную машину, выбрал установку системы на жесткий диск.Установил русский яхык для интерфейса и раскладки клавиатуры.

![рисунок11](img(12).png){ #fig:011 width=70% }

Указал часовой пояс - Москва.

![рисунок12](img(13).png){ #fig:012 width=70% }

Указал стандартные носители для установки ОС

![рисунок13](img(14).png){ #fig:013 width=70% }

Задал имя виртуальной машины в сети aoveniyazov.localdomain. 

![рисунок14](img(15).png){ #fig:014 width=70% }

Установил пароль для root

![рисунок15](img(16).png){ #fig:015 width=70% }

Выбрал вариант простой установки Centos,  и дождавшись установки системы перезагрузил ее.

![рисунок23](img(24).png){ #fig:016 width=70% }

![рисунок16](img(17).png){ #fig:017 width=70% }

Запустил виртуальную машину и настроил ее

Подключился к виртуальной машине с помощью созданной учетной записи.

Перешел под учетную запись root, обновил системные файлы и установил mc.

![рисунок17](img(18).png){ #fig:018 width=70% }

![рисунок18](img(19).png){ #fig:019 width=70% }

![рисунок19](img(20).png){ #fig:020 width=70% }

Далее освободил диск VDI и создал машину Host2, подключил ее к жесткому диску VDI. 

![рисунок20](img(21).png){ #fig:021 width=70% }

![рисунок21](img(22).png){ #fig:022 width=70% }

![рисунок22](img(23).png){ #fig:023 width=70% }

# Выводы

Сегодня я приобрел практические навыки установки операционной системы на виртуальную машину и минимально ее настроил для дальнейшей работы сервиса.


# Список литературы{.unnumbered}

::: {#refs}
:::