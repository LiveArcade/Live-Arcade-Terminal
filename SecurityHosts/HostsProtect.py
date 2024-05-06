import os
import sys
import time
import ctypes
import winreg


os.system('title HostsProtect.py')
    
print('Запущенно, пожалуйста старайтесь не отключать программу, ваш hosts под защитой!')

# Путь к файлу hosts
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Список заблокированных сайтов
blocked_sites_path = r"D:\Проекты\AntiBlockedHostsSite\siteslistblock.txt"

# Базовый файл hosts
default_hosts = """#Live Arcade Inc 2024(c)
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
"""

# Интервал проверки (в секундах)
check_interval = 60

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def add_to_startup():
    # Получаем путь к исполняемому файлу Python
    python_exe = sys.executable

    # Получаем путь к скрипту
    script_path = os.path.realpath(__file__)

    # Создаем команду для запуска скрипта
    command = f'"{python_exe}" "{script_path}"'

    # Открываем ключ реестра для автозапуска
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)

    # Добавляем наше приложение в автозапуск
    winreg.SetValueEx(key, 'SecurityHosts', 0, winreg.REG_SZ, command)

    # Закрываем ключ реестра
    winreg.CloseKey(key)

def main():
    while True:
        # Читаем файл hosts
        with open(hosts_path, "r") as file:
            hosts_content = file.read()

        # Если содержимое файла hosts отличается от базового, восстанавливаем базовый файл
        if hosts_content != default_hosts:
            print("Обнаружены изменения в файле hosts. Восстанавливаем базовый файл...")
            with open(hosts_path, "w") as file:
                file.write(default_hosts)

        # Ждем до следующей проверки
        time.sleep(check_interval)

if __name__ == "__main__":
    if not is_admin():
        print("Re-launching as admin!")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        add_to_startup()
        main()  # Already an admin here.
