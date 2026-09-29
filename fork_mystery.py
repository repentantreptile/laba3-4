import os
import time

# Общая переменная, созданная до разветвления
shared_counter = 42

print(f"[РОДИТЕЛЬ] Начальный процесс. PID: {os.getpid()}, Адрес counter: {hex(id(shared_counter))}")
print("Выполняем системный вызов fork()...\n")

# Клонируем процесс на уровне ядра ОС
pid = os.fork()

# Код ниже этой строки выполняется ОДНОВРЕМЕННО в двух процессах!
if pid == 0:
    # Этот блок выполнится ТОЛЬКО в дочернем процессе
    print(f"[ПОТОМК] Я родился! Мой PID: {os.getpid()}, PID родителя: {os.getppid()}")
    print(f"[ПОТОМК] Значение counter до изменения: {shared_counter}, Адрес: {hex(id(shared_counter))}")
      
    # Модифицируем переменную
    shared_counter = 999
    print(f"[ПОТОМК] Изменил counter! Новое значение: {shared_counter}, Новый адрес: {hex(id(shared_counter))}")
else:
    # Этот блок выполнится ТОЛЬКО в родительском процессе
    # Даем дочернему процессу 1 секунду, чтобы он точно успел изменить переменную
    time.sleep(1)
      
    print(f"[РОДИТЕЛЬ] Проверяю переменную после паузы...")
    print(f"[РОДИТЕЛЬ] Значение counter: {shared_counter}, Адрес: {hex(id(shared_counter))}")
