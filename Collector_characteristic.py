import platform
import socket
import uuid
import getpass
import json
import psutil
info = {
    "os": platform.system(),
    "os_release": platform.release(),
    "os_version": platform.version(),
    "architecture": platform.machine(),
    "hostname": socket.gethostname(),
    "user": getpass.getuser(),
    "python": platform.python_version(),
    "cpu": platform.processor(),
    "cpu_logical": psutil.cpu_count(),
    "cpu_physical": psutil.cpu_count(logical=False),  # потому  что физические ядра
    "ram_info": round(psutil.virtual_memory().total / 1024**3, 2),  #перевод в гб из байт
    "mac": ":".join(f"{b:02x}" for b in uuid.getnode().to_bytes(6, "big")),
}
for key, value in info.items():# метод возвращает ключ занчение
    print(key, value)
with open("user_info.json", "w", encoding = "utf-8") as json_file:
    json.dump(info, json_file, indent = 4, ensure_ascii=False)
