import threading
import time

# Общий ресурс, за который будут драться потоки
shared_counter = 0
# Количество итераций для каждого потока
STEPS = 100000

def worker():
    global shared_counter
    for _ in range(STEPS):
        temp = shared_counter
        time.sleep(0)  # Принудительно отдаем квант времени другому потоку
        shared_counter = temp + 1

print("Запуск двух потоков без синхронизации...")
start_time = time.time()

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()

# Ждем завершения обоих потоков
t1.join()
t2.join()

print(f"Все потоки завершили работу за {time.time() - start_time:.4f} сек.")
print(f"Ожидаемый результат: {STEPS * 2}")
print(f"Фактический результат в памяти ОЗУ: {shared_counter}")
print(f"Разница (потерянные вычисления): {(STEPS * 2) - shared_counter}")
