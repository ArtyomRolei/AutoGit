import os
import datetime


class GitInitException(Exception):
    pass


class GitAddDotException(Exception):
    pass


class GitCommitInitialException(Exception):
    pass


class GitRemoteAddOriginLinkException(Exception):
    pass


class GitPullRebaseOriginMasterException(Exception):
    pass


class GitPushKeyUOriginMasterException(Exception):
    pass


class GitAddKeyAException(Exception):
    pass


class GitCommitKeyMException(Exception):
    pass


class GitPushOriginMasterException(Exception):
    pass


print("Укажите полный путь до папки:")
path = input()

os.chdir(path)
dirs = os.listdir()
if ".git" in dirs:
    print("Гит хранилище уже создано в данной папке, приступаю к коммиту и пушу.")
    result = os.system("git add -A")
    if result != 0:
        print("ошибка при выполнении git add -A")
        raise GitAddKeyAException

    print("Создаю коммит с текущей датой.")
    now = datetime.datetime.now()
    result = os.system("git commit -m \"Commit " + str(now) + "\"")
    if result != 0:
        print("ошибка при выполнении git commit -m \"Commit " + str(now) + "\"")
        raise GitCommitKeyMException

    print("Сохраняю содержимое на гитхаб.")
    result = os.system("git push origin master")
    if result != 0:
        print("ошибка при выполнении git push origin master")
        raise GitPushOriginMasterException

    print("Успех!")

else:
    print("Здесь нет гит хранилища, создаю и подготавливаю.")
    result = os.system("git init")
    if result != 0:
        print("ошибка при выполнении git init")
        raise GitInitException

    print("Укажите ссылку до хранилища на гитхабе:")
    link = input()

    print("Добавляю в локальное хранилище все файлы.")
    result = os.system("git add .")
    if result != 0:
        print("ошибка при выполнении git add .")
        raise GitAddDotException

    print("Первый коммит.")
    result = os.system("git commit -m \"the initial edition\"")
    if result != 0:
        print("ошибка при выполнении git commit -m 'the initial edition'")
        raise GitCommitInitialException

    print("Связываю локальное хранилище с хранилищем на гитхабе.")
    result = os.system("git remote add origin " + link)
    if result != 0:
        print("ошибка при выполнении git remote add origin " + link)
        raise GitCommitInitialException

    print("Синхронизирую локальное хранилище.")
    result = os.system("git pull --rebase origin main")
    if result != 0:
        print("ошибка при выполнении git pull --rebase origin main")
        raise GitPullRebaseOriginMasterException

    print("Сохраняю содержимое на гитхаб.")
    result = os.system("git push -u origin master")
    if result != 0:
        print("ошибка при выполнении git push -u origin master")
        raise GitPushKeyUOriginMasterException

    print("Успех!")
