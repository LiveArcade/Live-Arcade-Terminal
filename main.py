import os
import re
import time
import webbrowser
import subprocess
import sys
import signal
import psutil
from pytube import YouTube
from ping3 import ping, verbose_ping
import glob
import re
from tqdm import tqdm
import requests
import winreg
import ctypes
import socket
import psutil
import speedtest
import cpuinfo
import platform
import pygame
from pytube import YouTube, Playlist
from ytmusicapi import YTMusic
from pytube import extract
from pydub import AudioSegment
import datetime
import subprocess
import time
import urllib.request
import io
import vlc
import urllib.request
import shutil
import random
from termcolor import colored
import urllib.parse


os.system('title Командная строка Live Arcade - 1.1')
print("""
████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░  ██████╗░██╗░░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░  ██╔══██╗╚██╗░██╔╝
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░  ██████╦╝░╚████╔╝░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░  ██╔══██╗░░╚██╔╝░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗  ██████╦╝░░░██║░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝  ╚═════╝░░░░╚═╝░░░

██╗░░░░░██╗██╗░░░██╗███████╗  ░█████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗  ██╗███╗░░██╗░█████╗░
██║░░░░░██║██║░░░██║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██║████╗░██║██╔══██╗
██║░░░░░██║╚██╗░██╔╝█████╗░░  ███████║██████╔╝██║░░╚═╝███████║██║░░██║█████╗░░  ██║██╔██╗██║██║░░╚═╝
██║░░░░░██║░╚████╔╝░██╔══╝░░  ██╔══██║██╔══██╗██║░░██╗██╔══██║██║░░██║██╔══╝░░  ██║██║╚████║██║░░██╗
███████╗██║░░╚██╔╝░░███████╗  ██║░░██║██║░░██║╚█████╔╝██║░░██║██████╔╝███████╗  ██║██║░╚███║╚█████╔╝
╚══════╝╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═╝╚═╝░░╚══╝░╚════╝░
""")
print("""


░░███╗░░░░░░░███╗░░
░████║░░░░░░████║░░
██╔██║░░░░░██╔██║░░
╚═╝██║░░░░░╚═╝██║░░
███████╗██╗███████╗
╚══════╝╚═╝╚══════╝
""")
print("(c) Live Arcade Inc")
def print_gradient(text):
    colors = ['green', 'cyan', 'blue']
    gradient = []

    for i, char in enumerate(text):
        gradient.append(colored(char, colors[i % len(colors)]))

    print(''.join(gradient))

# С шансом 1 к 100 (1%) выводим градиент
if random.randint(1, 100) == 1:
    print_gradient('Ваша надпись здесь')
command_history = []
def calc(expression):
    result = eval(expression)
    print(f"Результат: {result}")

BROWSERS = {
    "chrome": {
        "32bit": "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BB1F81197-15E2-9FAC-4C7F-A86D6E2974D1%7D%26lang%3Den%26browser%3D3%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx86-stable-statsdef_1%26installdataindex%3Dempty/chrome/install/ChromeStandaloneSetup.exe",
        "64bit": "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BB1F81197-15E2-9FAC-4C7F-A86D6E2974D1%7D%26lang%3Den%26browser%3D3%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/chrome/install/ChromeStandaloneSetup64.exe",
        "default": "https://dl.google.com/chrome/install/375.126/chrome_installer.exe"
    },
    "opera": {
        "32bit": "https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=(direct)&utm_medium=doc&utm_campaign=(direct)&http_referrer=missing&utm_site=opera_com&",
        "64bit": "https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&utm_source=(direct)&utm_medium=doc&utm_campaign=(direct)&http_referrer=missing&utm_site=opera_com&"
    },
    "yandex": {
        "32bit": "https://browser.yandex.ru/download?os=win&bitness=32&statpromo=true&banerid=6301000000&partner_id=exp_new_identity_1",
        "64bit": "https://browser.yandex.ru/download?os=win&bitness=64&statpromo=true&banerid=6301000000&partner_id=exp_new_identity_1"
    }
}
trusted_domains = [
    'yandex.ru', 'browser.yandex.ru', 'yandex.com',
    'google.com', 'google.ru', 'dl.google.com',
    'net.geo.opera.com', 'www.opera.com', 'opera.com',
    'livearcade1.000webhostapp.com'
]

def is_trusted(url):
    domain = urllib.parse.urlparse(url).netloc
    return domain in trusted_domains

for browser, versions in BROWSERS.items():
    for version, url in versions.items():
        if is_trusted(url):
            print(f'The URL for {browser} ({version}) is trusted.')
        else:
            print(f'Warning: The URL for {browser} ({version}) is not trusted.')

def install(resource):
    try:
        resource_name, *resource_version = resource.split()
        resource_version = resource_version[0] if resource_version else "default"
        if resource_name.lower() in BROWSERS and resource_version in BROWSERS[resource_name.lower()]:
            url = BROWSERS[resource_name.lower()][resource_version]
            if not is_trusted(url):
                print(f"Warning: The URL for {resource_name} ({resource_version}) is not trusted.")
                return
            print(f"Начинается загрузка браузера {resource_name}...")
            filename = urllib.parse.quote(url, safe='')
            response = requests.get(url, stream=True)
            total = int(response.headers.get('content-length', 0))
            with open(filename, "wb") as file, tqdm(
                desc=filename,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for data in response.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
            print(f"Файл установки браузера {resource_name} успешно загружен.")
            print(f"Начинается установка браузера {resource_name}...")
            os.system(filename)
            print(f"Браузер {resource_name} успешно установлен.")
        else:
            response = requests.get(f"https://pypi.org/pypi/{resource}/json")
            if response.status_code == 200:
                user_input = input(f"Ресурс {resource} найден как пакет Python и браузер. Вы хотите установить пакет Python (введите 'p') или браузер (введите 'b')?")
                if user_input.lower() == 'p':
                    os.system(f"pip install {resource}")
                    print(f"Пакет Python {resource} успешно установлен.")
                elif user_input.lower() == 'b':
                    print("Пожалуйста, используйте команду install с именем браузера и версией (например, 'install chrome 64bit').")
                else:
                    print("Неверный ввод. Пожалуйста, введите 'p' для установки пакета Python или 'b' для установки браузера.")
            else:
                filename = resource.split("/")[-1]
                response = requests.get(resource, stream=True)
                total = int(response.headers.get('content-length', 0))
                with open(filename, "wb") as file, tqdm(
                    desc=filename,
                    total=total,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as bar:
                    for data in response.iter_content(chunk_size=1024):
                        size = file.write(data)
                        bar.update(size)
                print(f"Файл {filename} успешно загружен.")
    except Exception as e:
        print(f"Произошла ошибка при обработке ресурса {resource}: {str(e)}")
def run_site(url):
    webbrowser.open(url)  # Открывает URL в браузере по умолчанию

def run(program):
    os.system(program)  # Запускает программу или файл

def cd(path):
    os.chdir(path)  # Изменяет текущий рабочий каталог

def git(*args):
    subprocess.check_call(['git'] + list(args))  # Выполняет команды git

def python_code(code):
    exec(code)  # Выполняет код Python

def python3_code(code):
    exec(code)  # Выполняет код Python3

def restart_program():
    os.execv(sys.executable, ['python3'] + sys.argv)  # Перезапускает программу

def stop_program(program):
    for proc in psutil.process_iter():
        if proc.name() == program:
            proc.send_signal(signal.SIGTERM)  # Останавливает программу

def pip_install(package):
    # Проверяем, является ли ресурс пакетом Python
    response = requests.get(f"https://pypi.org/pypi/{package}/json")
    if response.status_code == 200:
        data = response.json()
        url = data["urls"][0]["url"]
        filename = url.split("/")[-1]

        # Загружаем файл
        response = requests.get(url, stream=True)
        total = int(response.headers.get('content-length', 0))
        with open(filename, "wb") as file, tqdm(
            desc=filename,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)

        # Устанавливаем пакет
        os.system(f"pip install {filename}")
        os.remove(filename)  # Удаляем файл после установки
        print(f"Пакет Python {package} успешно установлен.")
    else:
        print(f"Не удалось найти пакет Python {package}.")

def ls(path='.'):
    for file in os.listdir(path):
        print(file)
        
def mkdir(dirname):
    os.mkdir(dirname)

def rm(filename):
    os.remove(filename)

def mv(src, dst):
    os.rename(src, dst)

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (bytes_downloaded / total_size) * 100
    print("Скачано: {:0.2f}%".format(liveprogress))

def save(url):
    youtube = YouTube(url, on_progress_callback=progress_function)
    video = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download()
    print(f"Видео скачано: {youtube.title}")

def reboot():
    os.system('shutdown /r /t 1')

def shutdown():
    os.system('shutdown /s /t 1')

def remove(filename):
    # Проверяем, существует ли файл
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл {filename} успешно удален.")
    else:
        print(f"Файл {filename} не найден.")

def delete(filename):
    # Проверяем, существует ли файл
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Файл {filename} успешно удален.")
    else:
        print(f"Файл {filename} не найден.")
def ping_command(host, count='4', size='56', timeout='1'):
    # Преобразование аргументов в нужные типы данных
    count = int(count)
    size = int(size)
    timeout = int(timeout)

    print(f"Pinging {host} with {size} bytes of data:")
    for i in range(count):
        delay = ping(host, size=size, timeout=timeout)
        if delay is None:
            print("Request timed out.")
        else:
            delay = round(delay * 1000.0, 2)
            print(f"Reply from {host}: bytes={size} time={delay}ms")
    print()
def grep(pattern, filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if re.search(pattern, line):
            print(line.strip())

def history():
    for command in command_history:
        print(command)

def find(pattern, path='.'):
    for filename in glob.iglob(path + '**/' + pattern, recursive=True):
        print(filename)

def reload():
    """Функция для перезагрузки скрипта main.py"""
    os.execl(sys.executable, os.path.abspath('main.py'), *sys.argv)

def restart():
    """Функция для перезапуска скрипта main.py"""
    os.execv(sys.executable, ['python'] + sys.argv)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def SecurityHosts(status):
    if status == 'on':
        # Ваш код для запуска скрипта защиты hosts
        os.system('python SecurityHosts/HostsProtect.py')
        print("Защита hosts включена.")
    elif status == 'off':
        if not is_admin():
            print("Перезапускаю терминал с правами администратора...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv + ['SecurityHosts', 'off']), None, 1)
        else:
            # Ваш код для остановки скрипта защиты hosts
            os.system('taskkill /f /im python.exe /fi "WindowTitle eq HostsProtect.py"')

            # Удаляем скрипт из автозапуска
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(key, 'SecurityHosts')
            winreg.CloseKey(key)

            print("Защита hosts отключена.")
    else:
        print("Неверная команда. Пожалуйста, используйте 'SecurityHosts on' или 'SecurityHosts off'.")
def network_info():
    # Получаем имя хоста и IP-адрес
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(f"Имя хоста: {host_name}")
    print(f"IP-адрес: {ip_address}")

    # Получаем информацию о сетевых адаптерах
    adapters = psutil.net_if_addrs()
    for name, adapter in adapters.items():
        print(f"\nАдаптер: {name}")
        for info in adapter:
            print(f"  {info.family.name} адрес: {info.address}")
            if info.broadcast:
                print(f"  Широковещательный адрес: {info.broadcast}")
            if info.netmask:
                print(f"  Маска подсети: {info.netmask}")

    # Получаем скорость интернета
    st = speedtest.Speedtest()
    print(f"\nСкорость загрузки: {st.download() / 1024 / 1024:.2f} Mbit/s")
    print(f"Скорость отдачи: {st.upload() / 1024 / 1024:.2f} Mbit/s")
def system_info():
    # Информация о системе
    print(f"Операционная система: {platform.system()}")
    print(f"Версия операционной системы: {platform.release()}")
    print(f"Архитектура: {platform.architecture()[0]}")

    # Информация о процессоре
    cpu_info = cpuinfo.get_cpu_info()
    print(f"Процессор: {cpu_info['brand_raw']}")

    # Информация о памяти
    memory_info = psutil.virtual_memory()
    print(f"Общий объем оперативной памяти: {memory_info.total / 1024 / 1024 / 1024:.2f} GB")
    print(f"Доступная оперативная память: {memory_info.available / 1024 / 1024 / 1024:.2f} GB")

    # Информация о дисках
    disk_info = psutil.disk_usage('/')
    print(f"Общий объем дискового пространства: {disk_info.total / 1024 / 1024 / 1024:.2f} GB")
    print(f"Доступное дисковое пространство: {disk_info.free / 1024 / 1024 / 1024:.2f} GB")

    # Информация о сетевых адаптерах
    adapters = psutil.net_if_addrs()
    for name, adapter in adapters.items():
        print(f"\nАдаптер: {name}")
        for info in adapter:
            print(f"  {info.family.name} адрес: {info.address}")
            if info.broadcast:
                print(f"  Широковещательный адрес: {info.broadcast}")
            if info.netmask:
                print(f"  Маска подсети: {info.netmask}") 

def play_music(source):
    pygame.mixer.init()
    if source.startswith('http'):
        # Если источник - это URL, загружаем файл в память
        with urllib.request.urlopen(source) as url:
            s = io.BytesIO(url.read())
        pygame.mixer.music.load(s)
    else:
        # Если источник - это локальный файл, загружаем его напрямую
        pygame.mixer.music.load(source)
    pygame.mixer.music.play()

# Пример использования:
# play_music('https://example.com/music.mp3')
# play_music('music.mp3')
# play_music('sounds/music.mp3')
default_sound = 2
reminder_sounds = ["sounds/sound1.mp3", "sounds/sound2.mp3"]  # Предполагаем, что у вас есть эти звуковые файлы

def reminder(time_str=None, message="Напоминание!", settings=None):
    """Создает напоминание, которое отображается через указанное количество времени."""
    global default_sound
    # Если предоставлены настройки, обновляем звук
    if settings:
        if settings == 'sound1':
            default_sound = 1
        elif settings == 'sound2':
            default_sound = 2
        return

    # Разбиваем входную строку на единицы времени и их значения
    time_units = {'s': 1, 'm': 60, 'h': 3600}
    reminder_time = 0
    if time_str:  # Добавляем эту проверку
        time_values = re.split(' ', time_str)
        for value in time_values:
            unit = value[-1]
            if unit in time_units.keys():
                reminder_time += int(value[:-1]) * time_units[unit]

    # Ждем указанное количество времени
    time.sleep(reminder_time)

    # Отправляем уведомление
    print(f'{message}')

    # Воспроизводим звуковой файл
    pygame.mixer.init()
    pygame.mixer.music.load(reminder_sounds[default_sound-1])  # Загружаем выбранный звуковой файл
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)  # Музыка будет играть до тех пор, пока ее не остановят


def stop_music():
    """Останавливает воспроизведение музыки."""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print("Музыка остановлена.")
    else:
        print("Музыка не играет.")

def winlock():
    ctypes.windll.user32.LockWorkStation()



def get_weather(city):
    response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=983d770e8dde4aa4b38131658241804&query={city}')
    data = response.json()
    print(f"Погода в {city}: {data['current']['temp_c']}°C, {data['current']['condition']['text']}")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def bsod():
    print("Вы собираетесь вызвать искусственный BSOD. Все несохраненные данные будут потеряны, и ваш компьютер будет перезагружен.")
    confirm = input("Вы уверены, что хотите продолжить? (Y/N): ")
    if confirm.lower() == 'y':
        if not is_admin():
            print("Перезапускаю терминал с правами администратора...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            print("Выполнение команды BSOD...")
            os.system("powershell Start-Process cmd -ArgumentList '/c Wininit' -Verb runAs")
    else:
        print("Команда BSOD отменена.")

        import os
import ctypes
import winreg

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def enable_task_manager():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r"Software\Microsoft\Windows\CurrentVersion\Policies\System",
                         0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(key)

def restore_hosts():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts_path, "w") as file:
        file.write("#Live Arcade Inc 2024(c)\n# Copyright (c) 1993-2009 Microsoft Corp.\n#\n# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.\n#\n# This file contains the mappings of IP addresses to host names. Each\n# entry should be kept on an individual line. The IP address should\n# be placed in the first column followed by the corresponding host name.\n# The IP address and the host name should be separated by at least one\n# space.\n#\n# Additionally, comments (such as these) may be inserted on individual\n# lines or following the machine name denoted by a '#' symbol.\n#\n# For example:\n#\n#      102.54.94.97     rhino.acme.com          # source server\n#       38.25.63.10     x.acme.com              # x client host\n\n# localhost name resolution is handled within DNS itself.\n#	127.0.0.1       localhost\n#	::1             localhost")

def system_file_check():
    os.system("sfc /scannow")

def reboot_in_safe_mode():
    os.system("bcdedit /set {current} safeboot minimal")
    os.system("shutdown /r /t 0")

def windows_recovery():
    if not is_admin():
        print("Перезапускаю терминал с правами администратора...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        print("Восстановление Windows...")
        enable_task_manager()
        restore_hosts()
        system_file_check()
        reboot = input("Вы хотите перезагрузить компьютер в безопасном режиме? (Y/N): ")
        if reboot.lower() == 'y':
            reboot_in_safe_mode()
        else:
            print("Восстановление завершено без перезагрузки в безопасном режиме.")
def print_processes(sort_by='cpu'):
    print(f"{'PID':<10}{'Name':<25}{'CPU %':<10}{'Memory %':<10}{'Disk I/O':<15}{'Power Usage (W)':<15}")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'io_counters']):
        power_usage_w = 'N/A'  # Получение информации о потреблении энергии может потребовать дополнительных библиотек или зависеть от ОС
        disk_io = proc.info['io_counters'].read_bytes + proc.info['io_counters'].write_bytes if proc.info['io_counters'] else 'N/A'
        print(f"{proc.info['pid']:<10}{proc.info['name']:<25}{proc.info['cpu_percent']:<10}{proc.info['memory_percent']:<10}{disk_io:<15}{power_usage_w:<15}")

def stop_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
    except psutil.NoSuchProcess:
        print(f"No process with PID {pid} is currently running.")

def TaskManager():
    while True:
        command = input("\033[92mTaskManager Mode> \033[0m").split()  # Зеленый текст
        if command[0] == 'list':
            sort_by = command[1] if len(command) > 1 else 'cpu'
            print_processes(sort_by=sort_by)
        elif command[0] == 'stop':
            if len(command) > 1:
                stop_process(int(command[1]))
            else:
                print("Please specify the PID of the process to stop.")
        elif command[0] == 'TaskManager' and len(command) > 1 and command[1] == 'off':
            break
        else:
            print("Unknown command. Please use 'list', 'stop <PID>', or 'TaskManager off'.")


 #В разработке private_mode
# def private_mode():
    if not is_admin():
        print("Перезапускаю терминал с правами администратора...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        while True:
            command = input("\033[92mPrivate Mode> \033[0m").split()  # Зеленый текст
            if command[0] == 'install' and len(command) > 1 and command[1] == 'tor':
              #  install_tor()
          #  elif command[0] == 'change_wallpaper':
             #   change_wallpaper()
         #   elif command[0] == 'encrypt_input':
             #   encrypt_input()
      #      elif command[0] == 'block_trackers':
            #    block_trackers()
         #   elif command[0] == 'protect_folder' and len(command) > 2:
                folder_path = command[1]
                password = command[2]
              #  protect_folder(folder_path, password)
            elif command[0] == 'exit':
                break
            else:      
             print("Неизвестная команда. Пожалуйста, используйте 'install tor', 'change_wallpaper', 'encrypt_input', 'block_trackers', 'protect_folder <folder_path> <password>', или 'exit'.")
def update():
    # URL файла на GitHub
    url_file = 'https://livearcade1.000webhostapp.com/Terminal-txt-version/Terminal-1.2.txt'

    # Скачать текстовый файл с URL
    with urllib.request.urlopen(url_file) as f:
        repo_url = f.read().decode()

    # Проверить, пуст ли файл
    if not repo_url.strip():
        print("\033[91mНовых версий пока нет\033[0m")
        return

    # Получить текущий рабочий каталог
    local_dir = os.getcwd()

    # Проверить, существует ли локальный репозиторий
    if os.path.exists(local_dir):
        # Если репозиторий существует, обновить его
        repo = git.Repo(local_dir)
        origin = repo.remotes.origin
        origin.pull()
    else:
        # Если репозитория нет, клонировать его
        git.Repo.clone_from(repo_url, local_dir)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def Searchfile(filename, directory=None):
    # Проверить, пуст ли файл
    if not filename.strip():
        print("\033[91mИмя файла не может быть пустым\033[0m")
        return

    # Проверить, является ли пользователь администратором
    if not is_admin():
        print("Перезапускаю терминал с правами администратора...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    # Если каталог не указан, искать во всей системе
    if directory is None:
        drives = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
    else:
        drives = [directory]

    for drive in drives:
        print(f"Ищем файл {filename} на диске {drive}...")
        for root, dirs, files in os.walk(drive):
            # Пропустить каталог, если нет прав доступа
            if 'Windows' in dirs:
                dirs.remove('Windows')
            if filename in files:
                print(f"Файл найден: {os.path.join(root, filename)}")
                return

    # Если файл не найден, вернуть сообщение об ошибке
    print("\033[91mФайл не найден\033[0m")


def secure_delete(filename, passes=3):
    with open(filename, "ba+") as file:
        length = file.tell()
    with open(filename, "br+") as file:
        for _ in range(passes):
            file.seek(0)
            file.write(os.urandom(length))
    os.remove(filename)

def checkpasswordsecure(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*()' for char in password)
    has_sufficient_length = len(password) >= 8
    return has_upper and has_lower and has_digit and has_special and has_sufficient_length

def caesar_cipher(text, shift, mode='encrypt'):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    if mode == 'decrypt':
        shifted_alphabet, alphabet = alphabet, shifted_alphabet
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def secure_delete(filename, passes=3):
    with open(filename, "ba+") as file:
        length = file.tell()
    with open(filename, "br+") as file:
        for _ in range(passes):
            file.seek(0)
            file.write(os.urandom(length))
    os.remove(filename)
def checkdisk_usage():
    usage = psutil.disk_usage('/')
    return f"Total: {usage.total}, Used: {usage.used}, Free: {usage.free}"
def backup_files(source_directory, backup_directory):
    shutil.copytree(source_directory, backup_directory)
commands = {
    'calc': calc,
    'install': install,
    'run_site': run_site,
    'run': run,
    'cd': cd,
    'git': git,
    'python': python_code,
    'python3': python3_code,
    'restart': restart_program,
    'stop': stop_program,
    'pip_install': pip_install,
    'pip': pip_install,
    'ls': ls,
    'mkdir': mkdir,
    'rm': rm,
    'mv': mv,
    'save': save,
    'reboot': reboot,
    'shutdown': shutdown,
    'remove': remove,
    'delete': delete,
    'del': delete,
    'rm': remove,
    'ping': ping_command,
    'grep': grep,
    'history': history,
    'find': find,
    'reload': reload,
    'restart': restart,
    'ytsave': save,
    'youtube': save,
    'YouTube': save,
    'SecurityHosts': SecurityHosts,
    'network_info': network_info,
    'networkinfo': network_info,
    'internetinfo': network_info,
    'system': system_info,
    'system_info': system_info,
    'play_music': play_music,
    'play_musc': play_music,
    'music': play_music,
    'music_play': play_music,
    'playmusic': play_music,
    'musicplay': play_music,
    'reminder': reminder,
    'stop_music': stop_music,
    'winlock': winlock,
    'погода': get_weather,
    'weather': get_weather,
    'bsod': bsod,
    'wincrash': bsod,
    'windows_recovery': windows_recovery,
    'recovery': windows_recovery,
    'TaskManager': TaskManager,
    'TaskManagermode': TaskManager,
    'Update': update,
    'update': update,
    'Searchfile': Searchfile,
    'cps': checkpasswordsecure,
    'checkpasswordsecure': checkpasswordsecure,
    'caesar_cipher':caesar_cipher,
    'caecip':caesar_cipher,
    'secure_delete':  secure_delete,
    'secdel': secure_delete,
    'del': secure_delete,
    'checkdisk_usage': checkdisk_usage,
    'checkdisk': checkdisk_usage,
    'diskusage': checkdisk_usage,
    'backup_files': backup_files,
    "BF":backup_files,
    'print_gradient': print_gradient,
    'rpg': print_gradient,
}

# Список команд, которые не требуют аргументов
no_arg_commands = ['shutdown', 'reboot', 'stop', 'restart', 'history', 'reload', 'restart','network_info','networkinfo','internetinfo','system','system_info','stop_music', 'winlock', 'bsod', 'recovery', 'windows_recovery', 'TaskManager', 'update', 'checkdisk_usage',]

while True:
    user_input = input("Введите команду: ")
    command_name, *command_args = user_input.split()
    command = commands.get(command_name)

    if command:
        if command_name in no_arg_commands:
            command()
        elif not command_args:
            print(f"Ошибка: команда '{command_name}' требует хотя бы одного аргумента.")
        else:
            command(' '.join(command_args))
    else:
        print(f"Неизвестная команда: {command_name}")
