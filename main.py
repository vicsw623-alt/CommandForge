import json
import os

class NoFileException(Exception):
    def __init__(self):
        super().__init__('No File')

file = 'data.json'

def set_cmd(Indata):
    colon_index = Indata.find(":")
    if colon_index > 4:
        cmd = Indata[4:colon_index]
        code = Indata[colon_index+1:]

        try:
            data = read_data_from_file(file)
        except NoFileException:
            new_data_file()
            data = []

        # 중복 체크
        for item in data:
            if item["cmd"] == cmd:
                print("This command already exists")
                return

        # 추가
        data.append({
            "cmd": cmd,
            "code": code
        })

        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

indata = []
def new_data_file():
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump(indata, f, indent=4 )

def read_data_from_file(file):
    if not os.path.exists(file):    
        raise NoFileException
    
    with open(file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f'[Exception] {e}')
    return data
def del_cmd(cmd,msg):
    try:
        data = read_data_from_file(file)
    except NoFileException:
        new_data_file()
    except:
        pass # log.. return... 마음대로
    new_data = []
    found = False

    for item in data:
        if item["cmd"] == cmd:
            found = True
        else:
            new_data.append(item)
    if found:
        with open(file, 'w') as f:
            json.dump(new_data, f, indent=4)
        print(msg)
    else:
        print(f"there is no cmd({cmd}) in file")
    
            

def del_all_cmd():
    redata = []
    with open(file, 'w') as f:
        json.dump(redata, f)
    print("deleted")

def rum_cmd(get_cmd):
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    found = False

    try:
        for item in data:
            if item["cmd"] == get_cmd: 
                print(f"[run]|{get_cmd}")
                exec(item["code"])
                found = True
                break
    except NameError:
        print(f"Wrong cmd({item['code']}).")
        agree = input("delet your code?(yes/no)")
        if agree == "yes":
            del_cmd(get_cmd)
        return
    except Exception as e:
        print(f"Fail to run cmd (Exception: {type(e).__name__} / detail: {e})") 
        return

    if not found:
        print(f"there is no cmd({get_cmd})")
new_data_file();

def help():
    print(
        "-------------------------------------\n"
        "set.<cmd>:<code> : make new cmd\n"
        "run.<cmd> : run cmd\n"
        "del.<cmd> deleted cmd\n"
        "show.<cmd> show the cmd's code\n"
        "mod.<cmd>:<code> : modify cmd\n"
        "delall : deleted all cmd\n"
        "list : show all cmd\n"
        "end : exit this program\n"
        "help : show help like this\n"
        "-------------------------------------"
    )

def show(show_cmd):
    data = read_data_from_file(file)

    found = False
    for item in data:
        if item["cmd"] == show_cmd:
            print(f'[show] {item["cmd"]}:{item["code"]}')
            found = True
            break

    if not found:
        print(f'there is no cmd({show_cmd})')

def list():
    print("-------------------------------------------------------")
    data = read_data_from_file(file)

    for item in data:
        print(item["cmd"])
    print("-------------------------------------------------------")

def mod(Indata):
    colon_index = Indata.find(":")
    if colon_index > 4:
        cmd = Indata[4:colon_index]
        del_cmd(cmd,"modified")
    set_cmd(Indata)

def main():
    while True:
        Indata = input("")
        colon_index = 0
        cmd = ""
        code = ""
        get_cmd = ""
        data = []

        if (Indata.lower() == "end"):
            break
        elif (Indata[0:4] == "set."):
            set_cmd(Indata)
        elif (Indata[0:4] == "del."):
            del_cmd(Indata[4:],"deleted")
        elif (Indata == "delall"):
            del_all_cmd()
        elif (Indata[0:4] == "run."):
            rum_cmd(Indata[4:])
        elif (Indata[0:5] == "help" or Indata[0] == "?"):
            help()
        elif (Indata[0:5] == "show."):
            show(Indata[5:])
        elif (Indata[0:4] == "list"):
            list()
        elif (Indata[0:4] == "mod."):
            mod(Indata)

if __name__=="__main__":
    main()