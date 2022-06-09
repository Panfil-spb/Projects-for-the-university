# Операционные системы

Задания выполнены в ОС Linux.
В файлах `README.md` каждой лабораторной работы приведены системные вызовы, которые использовались для реализации программы. Приведенные сведения являются минимальными. Для подробной информации следует обратиться к руководству программиста системы Linux (команда `man`).
Если системный вызов возвращает результат, в программе проверяется этот результат и выполняются действия действия – вывод результата на экран и завершение программы в случае ошибки.

Для компиляции и запуска программы используйте скрипты (файлы `*.sh`), которые вместе с исходным кодом находятся в соответствующих директориях.


## Содержание

### Параллельное выполнение и взаимодействие программ в ОС

1. [LAB_1](./LAB_1) Создание и уничтожение потоков
2. [LAB_2](./LAB_2) Синхронизация потоков с помощью мьютексов и неименованных семафоров
3. [LAB_3](./LAB_3) Взаимодействие потоков через неименованные каналы
4. [LAB_4](./LAB_4) Создание и уничтожение процессов
5. [LAB_5](./LAB_5) Синхронизация процессов с помощью именованных семафоров

### Управление памятью в ОС

6. [LAB_6](./LAB_6) Взаимодействие процессов через разделяемую память

### Управление внутренними коммуникациями в ОС

7. [LAB_7](./LAB_7) Взаимодействие процессов через именованные каналы
8. [LAB_8](./LAB_8) Взаимодействие процессов через очереди сообщений

### Управление внешними коммуникациями в ОС

9. [LAB_9](./LAB_9) Сетевое взаимодействие процессов через сокеты

### Правление файлами и доступом к объектам ОС

10. Программный интерфейс пространств имен


## Иерархическая модель ОС

Каждый уровень представляет собой некоторую функцию операционной системы.

  №  | НАЗВАНИЕ | ОБЪЕКТ | ПРИМЕРЫ ДЕЙСТВИЯ
:---:|:--------:|:------:|:-------:
13 | Оболочка | Интерфейс пользователя | Действия на языке обол. Цикл опрса событий 
12 | Процессы пользователя | Виртуальная машина | Создать, приостанвить, возобновить, уничтожить
11 | Каталоги | Таблицы соотв. внешн. и внутр. имён | Создать, связать, модиф, прочитать, читать, записать
10 | Устройства | Дисплей, принтер, клавиатура | Создать, уничтожить, откр., закрыть, читать, записать
9 | Файловая система | Файлы | То же, что и на 10
8 | Коммуникации | Конвейер, буфер | То же, что и на 10
7 | Виртуальная память | Страницы, сегменты | Загрузить, выгрузить, прочитать, записать
6 | Локальная внешняя память | Диск, сектор, дорожка | Прочитать, записать
5 | Элементарные процессы | Семафоры, сигналы, дескрипторы, очереди | Создать, уничтожить, возобновить, приостановить процесс
4 | Прерывания | Процедуры обработки прерываний | Вызов, возврат, маскирование, размаскирование, уст. Вектор
3 | Процедуры | Логическое завершение, набор команд, стеки | Вызов, возврат, прочит. из стека, записать в стек
2 | Система команд | Инструкции, директивы | Чтение,запись, пересылка, сравнение, арифметические операции
1 | Физическая машина | Регистры, процессор, ячейки памяти | Сброс, установка, запись, чтение

**Уровень 1.** Уровень электронных схем, на котором определены такие объекты, как регистры, счетчики, логические схемы, сумматоры и т. д. 
Известны и операции, определенные на этих схемах: сброс, установка, чтение, запись. Таким образом, первой функцией ОС является управление физической аппаратурой.

**Уровень 2.** Управление аппаратурой производится с помощью выполнение команд процессора, это несколько более абстрактный уровень, чем уровень аппаратуры. Вспомним, например, программную модель процессора.

**Уровень 3.** На этом уровне отдельные инструкции системы команд объединяются в логически законченные участки, выполняющие определенные функции, и называемые процедурами. Процедура – это базовый элемент любой программной системы. Выполнение любой программы - это последовательность вызовов процедур.

**Уровень 4.** На этом уровне появляются прерывания как средство взаимодействия процессора с периферийной аппаратурой. Проблема взаимодействия с аппаратурой состоит в том, что сигналы от аппаратуры могут появляться в произвольный момент времени относительно потока выполняемых команд. Система прерываний и позволяет преодолеть эту асинхронность появления сигналов от аппаратуры. Реакция на сигналы - это определенным образом организованные процедуры - процедуры обработки прерываний. 

Первые четыре уровня - это уровни, очень сильно зависящие от аппаратуры машины. Далее идет более высокий уровень абстракции.

**Уровень 5.** На этом уровне появляются средства, связанные с попытками одновременного выполнения нескольких задач. Например, печать, редактирование текста и обмен данными через модем. Если процессор один, а задач требуется выполнять несколько, то появляется некоторая надстройка, обеспечивающая переключение задач. Здесь появляется понятие - контекст. При этом одна задача приостанавливается, ее контекст сохраняется в специальной структуре данных, а другая возобновляется и ее контекст восстанавливается. Большая роль здесь отводится вопросам взаимодействия задач, например, одна задача не может продолжить выполнение с какой-то точки, пока другая задача не пройдет через определенную точку в своей программе. Все средства организации многозадачности и взаимодействия задач объединены на этом уровне элементарных процессов.

**Уровень 6.** На данном уровне осуществляется управление доступом к устройствам внешней памяти одной машины. Пользовательские программы лишь определяют логическое расположение данных на дисках, а программы этого уровня осуществляют поиск, запись и чтение физически, определяя положение данных на дорожках и секторах. Программы этого уровня всегда оформляются в виде процессов, поэтому и находятся над соответствующим уровнем.

**Уровень 7.** На данном уровне осуществляется управление виртуальной памятью. Виртуальная память - это средство расширения оперативной памяти за счет дискового пространства.

Вплоть до уровня 7 операционная среда имеет дело в основном с ресурсами одного компьютера. Начиная со следующего уровня, среда выполнения программ существенно расширяется.

**Уровень 8.** На уровне 8 осуществляется управление коммуникациями - обменом данными - между процессами. Для этого создаются специальные средства, которые базируются на средствах 5-го уровня. При этом одни и те же примитивы используются как для коммуникаций между процессами, выполняемыми на одной машине, так и для процессов, выполняемых на разных машинах, хотя сами примитивы с некоторого нижнего уровня реализуются, естественно, по-разному.

**Уровень 9.** Этот уровень управляет объектами, гораздо более абстрактными, чем уровень 6. Если файлы, с которыми работает программа, расположены на другой физической машине, то для доступа к ним задействуется механизм коммуникаций.

**Уровень 10.** Этот уровень обеспечивает управление внешними устройствами, такими как принтер, дисплей, клавиатура. Для доступа к удаленным объектам этого уровня также может быть задействован механизм коммуникаций.

Важной особенностью уровней 8, 9, 10 является то, что на объектах этих уровней определены операции, имеющие одинаковые имена: создать, уничтожить, открыть, закрыть, прочитать, записать. Они различаются в реализации, но пользователь об этом может не задумываться. Он с помощью одинаковых вызовов будет брать данные из конвейера, из файла или из устройства. Такой прием называется поздним связыванием и известен из объектно-ориентированного программирования.

**Уровень 11.** На этом уровне осуществляется связывание внешних имен объектов, с которыми работает пользователь, с их внутренними именами, с которыми работает машина. Каталоги представляют собой таблицы соответствия внешних и внутренних имен, где внешние имена представляют собой цепочки символов, а внутренние - коды или адреса. Кроме того, каталоги хранят перечни методов, которые могут выполняться над объектами. Именно на этом уровне происходит «разрешение ссылок», т. е. определение своего метода для данного объекта не зависимо оттого, что имя у этого метода такое же, как и другого объекта.

**Уровень 12.** На данном уровне происходит управление процессами пользователя. Отличие от уровня 5 элементарных процессов состоит в том, что глубина контекста на уровне 10 существенно больше. Если на уровне 5 контекст состоит, как правило, из набора регистров и стека, то здесь контекст – это фактически целая виртуальная машина.

**Уровень 13.** На уровне 13 находится некоторый интерпретатор команд пользователя. Не важно, каким образом он реализован – с помощью командной строки или с помощью этикеток-иконок. В любом случае этот интерпретатор работает в бесконечном цикле следующего вида:

```cpp
while (true) {
	Ввод команды;
	Выполнение команды;
}
```

## Литература

1.	Таненбаум Э., Бос Х. Современные операционные системы. 4-е изд. — СПб.: Питер, 2015.
2.	Уорд Б. Внутреннее устройство Linux. — СПб.: Питер, 2016.
3.	Фуско Д. Linux. Руководство программиста. — СПб.: Питер, 2011.
4.	Лав Р. Linux. Системное программирование. 2-е изд. — СПб.: Питер, 2014.
5.	Керриск Майкл. Linux API. Исчерпывающее руководство. — СПб.: Питер, 2018.