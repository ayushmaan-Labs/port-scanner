import socket
import threading
from queue import Queue

# Target host and range of ports
target_host = 'scanme.nmap.org'
port_range = range(1, 1025)
num_threads = 100

# Queue for threads
task_queue = Queue()

# Scan a specific port and try to grab the banner
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target_host, port))
        try:
            banner = s.recv(1024).decode("utf-8").strip()
        except:
            banner = "No banner retrieved"
        print(f"[+] Port {port} is open | Banner: {banner}")
        s.close()
    except:
        pass

def worker():
    while True:
        port = task_queue.get()
        scan_port(port)
        task_queue.task_done()

# Main execution
if __name__ == "__main__":
    for port in port_range:
        task_queue.put(port)

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        threads.append(t)

    task_queue.join()
    print("Scan complete!")
