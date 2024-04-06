import os
import re
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
█
██╗░░░██╗  ░░███╗░░░░░░█████╗░  ██████╗░███████╗████████╗░█████╗░
██║░░░██║  ░████║░░░░░██╔══██╗  ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
╚██╗░██╔╝  ██╔██║░░░░░██║░░██║  ██████╦╝█████╗░░░░░██║░░░███████║
░╚████╔╝░  ╚═╝██║░░░░░██║░░██║  ██╔══██╗██╔══╝░░░░░██║░░░██╔══██║
░░╚██╔╝░░  ███████╗██╗╚█████╔╝  ██████╦╝███████╗░░░██║░░░██║░░██║
░░░╚═╝░░░  ╚══════╝╚═╝░╚════╝░  ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝
""")
print("(c) Live Arcade Inc")
command_history = []
def calc(expression):
    result = eval(expression)
    print(f"Результат: {result}")

def install(resource):
    try:
        # Проверяем, является ли ресурс пакетом Python
        response = requests.get(f"https://pypi.org/pypi/{resource}/json")
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
            print(f"Пакет Python {resource} успешно установлен.")
        elif 'youtube.com' in resource or 'youtu.be' in resource:
            # Это видео с YouTube
            youtube = YouTube(resource)
            video = youtube.streams.first()
            print(f"Начинается загрузка видео {youtube.title}...")
            filename = video.download(output_path=".", filename_prefix="youtube_")
            print(f"Видео {youtube.title} успешно загружено и сохранено как {filename}.")
        elif 'github.com' in resource:
            # Это репозиторий GitHub
            git.Git(".").clone(resource)
            print(f"Репозиторий {resource} успешно клонирован.")
        else:
            # Это файл для загрузки
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
}

while True:
    user_input = input("Введите команду: ").split()
    command = commands.get(user_input[0])

    if command:
        # Список команд, которые не требуют аргументов
        no_arg_commands = ['shutdown', 'reboot', 'stop', 'restart', 'history', 'reload', 'restart']

        if len(user_input) == 1 and user_input[0] not in no_arg_commands:
            print(f"Ошибка: команда '{user_input[0]}' требует хотя бы одного аргумента.")
        else:
            command(*user_input[1:])
    else:
        print(f"Неизвестная команда: {user_input[0]}")