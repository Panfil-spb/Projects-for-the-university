# Взаимодействие процессов через разделяемую память

В стандарте `POSIX` участок разделяемой памяти создается следующим вызовом:
```C++
int shm_open(const char *name, int oflag, mode_t mode),
```
где:</br>
`name` – имя участка разделяемой памяти;</br>
`oflag` – флаги, определяющие тип создаваемого участка разделяемой памяти;</br>
`mode` – права доступа к участку разделяемой памяти.
Установка размера участка разделяемой памяти производится следующим вызовом:</br>
```C++
int ftruncate(int fd, off_t length),
```
где:</br>
`fd` - дескриптор разделяемой памяти, полученный как результат вызова функции `shm_open()`;</br>
`length` – требуемый размер разделяемой памяти.

Отображение разделяемой памяти на локальный адрес создается вызовом:
```C++
void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset)
```
где:</br>
`addr` - начальный адрес отображения;</br>
`length` - размер отображения;</br>
`prot` – параметр, определяющий права чтения/записи отображения;</br>
`flags` – параметр, определяющий правила видимости отображения процессами;</br>
`fd` - дескриптор разделяемой памяти;</br>
`offset` – смещение на участке разделяемой памяти относительно начального адреса.</br>

Удаление отображения разделяемой памяти на локальный адрес производится вызовом:
```C++
int munmap(void *addr, size_t length)
```
где:</br>
`addr` – локальный адрес отображения;</br>
`length` -  размер отображения.</br>

Закрытие участка разделяемой памяти производится вызовом:
```C++
int close(int fd)
```
где:</br>
`fd` - дескриптор разделяемой памяти.

Удаление участка разделяемой памяти производится вызовом:
```C++
int shm_unlink(const char *name),
```
где:</br>
`name` – имя участка разделяемой памяти.</br>
В стандарте `SVID` участок разделяемой памяти создается вызовом:
```C++
int shmget(key_t key, int size, int shmflg)
```
где:</br>
`key_t key` – ключ, получаемый функцией `ftok()`;</br>
`int size` – требуемый размер памяти;</br>
`int shmflg` – флаги, задающие права доступа к памяти, например, `0644|IPC_CREAT`.

После создания участка разделяемой памяти его необходимо подсоединить к адресному пространству процесса. Это делается вызовом:
```C++
void *shmat(int shmid, const void *shmaddr, int shmflg)
```
где:</br>
`int shmid` – идентификатор сегмента;</br>
`const void *shmaddr` – адрес памяти;</br>
`int shmflg` - флаги, задающие права доступа к памяти.</br>

После использования памяти ее необходимо отсоединить от адресного пространства процесса вызовом:
```C++
int shmdt(const void *shmaddr)
```
где:</br>
`const void *shmaddr` – адрес памяти;</br>

А затем удалить вызовом:
```C++
int shmctl(int shmid, int cmd, struct shmid_ds *buf)
```
где:</br>
`int shmid` – идентификатор сегмента;</br>
`int cmd` – код команды, для удаления используется `IPC_RMID`;</br>
`struct shmid_ds *buf` – структура для хранения информации о сегменте разделяемой памяти, в случае удаления не используется.
