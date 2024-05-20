import threading
import time

# Crear un semaforo con un contador inicial de 2
semaphore = threading.Semaphore(2)

def tarea(id):
	print(f"Cajero {id} intentando acceder a la base de datos")
	with semaphore:
		print(f"Cajero {id} ha adquirido el semaforo")
		time.sleep(2)
		print(f"Cajero {id} ha liberado el semaforo")
		
threads = []
for i in range(5):
	thread = threading.Thread(target=tarea, args=(i,))
	threads.append(thread)
	thread.start()
	
for thread in threads:
	thread.join()
	
