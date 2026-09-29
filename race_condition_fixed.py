import threading
import time

shared_counter = 0
STEPS = 100000

# Создаем мьютекс
counter_lock = threading.Lock()

def worker():
    global shared_counter
    for _ in range(STEPS):
        with counter_lock:
            temp = shared_counter
            time.sleep(0)
            shared_counter = temp + 1

print("Запуск двух потоков С СИНХРОНИЗАЦИЕЙ (Lock)...")
start_time = time.time()

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Все потоки завершили работу за {time.time() - start_time:.4f} сек.")
print(f"Ожидаемый результат: {STEPS * 2}")
print(f"Фактический результат в памяти ОЗУ: {shared_counter}")
print(f"Разница (потерянные вычисления): {(STEPS * 2) - shared_counter}")
