---
## Front matter
lang: ru-RU
title: Лабораторная работа №3
author: |
	Овениязов Артур
institute: |
	 RUDN University, Moscow, Russian Federation
date: Октябрь, 2021 Москва

## Formatting
toc: false
slide_level: 2
theme: metropolis
sansfont: NotoMono-Regular
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Прагматика выполнения лабораторной работы

Необходимо провести исследование дискреционных разграничений.

# Цель работы

## Цель работы

Получение практических навыков работы в консоли с атрибутами файлов, закрепление теоретических основ дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux.

# Задачи

## Задачи

1. Создать пользователя guest2.
2. Войти в систему.
3. Определить опытным путем, какие операции доступны, а какие нет.
4. Заполнить таблицу «Установленные права и разрешённые действия для групп»
5. Определить те или иные минимально необходимые права для выполнения операций внутри директории для групп и заполнить таблицу.

# Результат

## Результатом моей работы стала таблица

: Минимально необходимые права для выполнения операций для группы  {#tbl:1.2}

|     Операция                   |     Минимальные   права на директорию     |     Минимальные   права на файл     |
|--------------------------------|-------------------------------------------|-------------------------------------|
|     Создание файла.            |     d----wx--- (030)                      |     ----------(000)                 |
|     Удаление файла             |     d----wx--- (030)                      |     ----------(000)                 |
|     Чтение файла               |     d-----x--- (010)                      |     ----r-----(040)                 |
|     Запись в файл              |     d-----x--- (010)                      |     -----w----(020)                 |
|     Переименование файла       |     d----wx--- (030)                      |     ----------(000)                 |
|     Создание поддиректории     |     d----wx--- (030)                      |     ----------(000)                 |
|     Удаление поддиректории     |     d----wx--- (030)                      |     ----------(000)                 |



## Вывод

Сегодня я приобрел практические навыки работы в консоли с атрибутами файлов, закрепил теоретические основы дискреционного разграничения доступа в современных системах с открытым кодом на базе ОС Linux

## {.standout}

Спасибо за внимание!
