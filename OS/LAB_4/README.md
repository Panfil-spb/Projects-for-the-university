# Создание и уничтожение процессов

Основным системным вызовом для создания нового процесса в операционных системах, поддерживающих стандарт POSIX, является следующий вызов:

```C++
pid_t fork(void).
```

Вызов `fork()`, сделанный в некотором процессе, который будем называть родительским, создает дочерний процесс, который является практически полной копией родительского процесса. При создании данные родительского процесса копируются в дочерний процесс и оба процесса начинают выполняться параллельно. Важным отличием родительского процесса от дочернего процесса является значение результата, возвращаемого функцией `fork()`. Дочернему процессу возвращается значение 0, а родительскому процессу возвращается идентификатор дочернего процесса, т.е.:

```C++
pid_t	pid	=	fork();
if (pid == 0) {
	//дочерний процесс
}else{
	//родительский процесс;
}
```

где `pid`– возвращаемое значение, `0` – дочернему процессу, больше `0` – родительскому процессу, `-1` – в случае ошибки.

Наиболее распространенной схемой выполнения пары процессов (родительский – дочерний), является схема, при которой родительский процесс приостанавливает свое выполнение до завершения дочернего процесса с помощью специальной функции:

```C++
pid_t waitpid(pid_t pid, int *status, int options),
```

где:</br>
`pid` – идентификатор дочернего процесса, завершение которого ожидается,</br>
`status` – результат завершения дочернего процесса,</br>
`options` – режим работы функции.</br>
В некоторых случаях вызов `fork()` используется программистом для организации параллельного выполнения процессов в рамках одной написанной программы.
В других случаях в качестве дочернего процесса необходимо выполнить внешнюю программу.
В этом случае для запуска внешней программы следует в дочернем процессе вызвать функцию семейства `exec()`.

Существуют следующие разновидности этой функции:

```C++
int execve(const char *pathname, char *const argv [], char *const envp[]);
int execl(const char *pathname, const char *arg, ...),
int execlp(const char *file, const char *arg, ...),
int execle(const char *pathname, const char *arg,..., char * const envp[]),
int execv(const char *pathname, char *const argv[]),
int execvp(const char *file, char *const argv[]),
int execvpe(const char *file, char *const argv[],char *const envp[]).
```

Если в имени функции присутствует символ `l`, то аргументы `arg` командной строки передаются в виде списка `arg0, arg1.... argn, NULL`.

Если в имени функции присутствует символ `v`, то аргументы командной строки передаются в виде массива `argv[]`. Отдельные аргументы адресуются через `argv[0], argv[1], ..., argv[n]`. Последний аргумент `(argv [n])` должен быть `NULL`.

Если в имени функции присутствует символ `e`, то последним аргументом функции является массив переменных среды `envp[]` (можно получить с помощью функциии `getenv("PATH")`)

Если в имени функции присутствует символ `p`, то программа с именем `file` ищется не только в текущем каталоге, но и в каталогах, определенных переменной среды `PATH`.

Если в имени функции отсутствует символ `p`, то программа с именем `path` ищется только в текущем каталоге, или имя `path` должно указывать полный путь к файлу.

Функция `execve()`, является основной в семействе, остальные функции обеспечивают интерфейс к ней.

В случае успешного выполнения вызова функция не возвращает никакого результата. В случае ошибки возвращается `-1`, а глобальной переменной `errno` присваивается значение в соответствии с видом ошибки.