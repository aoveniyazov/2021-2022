---
# Front matter
title: "Отчет по лабораторной работе №5"
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

Изучение механизмов изменения идентификаторов, применения SetUID- и Sticky-битов. Получение практических навыков работы в консоли с дополнительными атрибутами. Рассмотрение работы механизма
смены идентификатора процессов пользователей, а также влияние бита Sticky на запись и удаление файлов.

# Задание

Лабораторная работа подразумевает практическое исследование дискреционных разграничений в современных системах с открытым кодом на базе ОС Linux, а именно изучение атрибутов для групп пользователей.

# Теоретическое введение

В Linux, как и в любой многопользовательской системе, абсолютно естественным образом возникает задача разграничения доступа субъектов — пользователей к объектам — файлам дерева каталогов.
Один из подходов к разграничению доступа — так называемый дискреционный (от англ, discretion — чье-либо усмотрение) — предполагает назначение владельцев объектов, которые по собственному усмотрению определяют права доступа субъектов (других пользователей) к объектам (файлам), которыми владеют.
Дискреционные механизмы разграничения доступа используются для разграничения прав доступа процессов как обычных пользователей, так и для ограничения прав системных программ в (например, служб операционной системы), которые работают от лица псевдопользовательских учетных записей.
[@lossit:ggwp]

# Выполнение лабораторной работы 
## ВАЖНО!!! Пунктов в отчете было бы необычайного много если отвечать скрином на каждый, поэтому многие пункты были объеденены для более легкого составления отчета .
## Часть первая
Войдите в систему от имени пользователя guest.Создайте программу simpleid.c.
Скомплилируйте программу и убедитесь, что файл программы создан:gcc simpleid.c -o simpleid 
Выполните программу simpleid:./simpleid 
Выполните системную программу id: id и сравните полученный вами результат с данными предыдущего пункта
задания. 
Программа и команда выдают одинаковые результаты.

![Результат компилирования simpleid и id](images/img(1).png){ #fig:001 width=70% }

Усложните программу, добавив вывод действительных идентификаторов,cкомпилируйте и запустите simpleid2.c:
gcc simpleid2.c -o simpleid2 ./simpleid2

![Результат компилирования simpleid2](images/img(2).png){ #fig:002 width=70% }

От имени суперпользователя выполните команды
chown root:guest /home/guest/simpleid2
chmod u+s /home/guest/simpleid2
Chmod u+s наделяет каждого пользователя правами владельца(кто пытается получить к нему доступ), а chown меняет владельца.
Выполните проверку правильности установки новых атрибутов и смены
владельца файла simpleid2:
ls -l simpleid2
Запустите simpleid2 и id:
./simpleid2
id
Результаты соврадают.

![Результат chmod, chown, simpleid2, id](images/img(3).png){ #fig:003 width=70% }

 Создайте программу readfile.c.Откомпилируйте её.
gcc readfile.c -o readfile

![Результат компилирования readfile.c](images/img(4).png){ #fig:004 width=70% }

Смените владельца у файла readfile.c (или любого другого текстового файла в системе) и измените права так, чтобы только суперпользователь
(root) мог прочитать его, a guest не мог

![Смена прав и владельца readfile.c](images/img(5).png){ #fig:005 width=70% }

Проверьте, что пользователь guest не может прочитать файл readfile.c.

![Проверка чтения файла](images/img(6).png){ #fig:006 width=70% }

Смените у программы readfile владельца и установите SetU’D-бит

![Обратная смена владельца файла](images/img(7).png){ #fig:007 width=70% }

Проверьте, может ли программа readfile прочитать файл readfile.c? Проверьте, может ли программа readfile прочитать файл /etc/shadow?
Чтение обоих файлов не удалось.

![Проверка чтения](images/img(8).png){ #fig:008 width=70% }

## Часть вторая
Выясните, установлен ли атрибут Sticky на директории /tmp, для чего
выполните команду ls -l / | grep tmp. От имени пользователя guest создайте файл file01.txt в директории /tmp
со словом test: echo "test" > /tmp/file01.txt.Просмотрите атрибуты у только что созданного файла и разрешите чтение и запись для категории пользователей «все остальные»:
ls -l /tmp/file01.txt chmod o+rw /tmp/file01.txt ls -l /tmp/file01.txt

![Результат chmod и ls -l /tmp/file01.txt](images/img(n).png){ #fig:009 width=70% }

От пользователя guest2 (не являющегося владельцем) попробуйте прочитать файл /tmp/file01.txt:
cat /tmp/file01.txt5., попробуйте дозаписать в файл /tmp/file01.txt слово test2 командой echo "test2" > /tmp/file01.txt.
Проверьте содержимое файла командой
cat /tmp/file01.txt
От пользователя guest2 попробуйте записать в файл /tmp/file01.txt
слово test3, стерев при этом всю имеющуюся в файле информацию командой
echo "test3" > /tmp/file01.txt
Проверьте содержимое файла командой
cat /tmp/file01.txt
От пользователя guest2 попробуйте удалить файл /tmp/file01.txt командой
rm /tmp/fileOl.txt
Все операции были выполнены успешно.

![Результат cat и echo](images/img(9).png){ #fig:010 width=70% }

Повысьте свои права до суперпользователя следующей командой
su -
и выполните после этого команду, снимающую атрибут t (Sticky-бит) с
директории /tmp:
chmod -t /tmp. Покиньте режим суперпользователя командой exit.
От пользователя guest2 проверьте, что атрибута t у директории /tmp нет:
ls -l / | grep tmp. Повторите предыдущие шаги. Какие наблюдаются изменения?
Ваши наблюдения занесите в отчёт - все удалось.

![Результат chmod -t /tmp](images/img(10).png){ #fig:011 width=70% }

Повысьте свои права до суперпользователя и верните атрибут t на директорию /tmp:
su - chmod +t /tmp exit

![Результат su/chmod +t](images/img(11).png){ #fig:012 width=70% }

# Листинг программ
## Simpleid.c
```c++
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
int
main ()
{
uid_t uid = geteuid ();
gid_t gid = getegid ();
printf ("uid=%d, gid=%d\n", uid, gid);
return 0;
}```
## Simpleid2.c
```
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
int
main ()
{
uid_t real_uid = getuid ();
uid_t e_uid = geteuid ();
gid_t real_gid = getgid ();
gid_t e_gid = getegid () ;
printf ("e_uid=%d, e_gid=%d\n", e_uid, e_gid);
printf ("real_uid=%d, real_gid=%d\n", real_uid, real_gid);
return 0;
}
```
## readfile.c
```
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
int
main (int argc, char* argv[])
{
unsigned char buffer[16];
size_t bytes_read;
int i;
int fd = open (argv[1], O_RDONLY);
do
{
bytes_read = read (fd, buffer, sizeof (buffer));
for (i =0; i < bytes_read; ++i) printf("%c", buffer[i]);
}
while (bytes_read == sizeof (buffer));
close (fd);
return 0;
}
```
# Выводы

Сегодня я приобрел практические навыки работы в консоли с атрибутами файлов, закрепил теоретические основы дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux и изучил механизмы изменения идентификаторов применения SetUID- и Sticky-битов.

# Список литературы{.unnumbered}

::: {#refs}
:::