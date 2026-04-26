import json
import Code
import os

class NoFileException(Exception):
    def __init__(self):
        super().__init__('No File')

file = 'data.json'

def set_cmd(Indata):
    colon_index = Indata.find(":")
    if (colon_index>4):
        cmd = Indata[4:colon_index]
        code = Indata[colon_index+1:]
        print(cmd, code)
        try:
            data = read_data_from_file(file)
        except NoFileException:
            new_data_file()
        data.append({
            "cmd": cmd,
            "code": code
        })
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

def new_data_file():
    if not os.path.exists(file):
        open(file, 'x', )

def read_data_from_file(file):
    if not os.path.exists(file):    
        raise NoFileException
    
    with open(file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f'[Exception] {e}')
    return data
def del_cmd(cmd):
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
        print("deleted")
    else:
        print(f"there is no cmd({cmd}) in file")
    
            

def del_all_cmd():
    redata = []
    with open(file, 'w') as f:
        json.dump(redata, f)
    print("삭제됨")

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
                print(f"{get_cmd} 실행")
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
            del_cmd(Indata[4:])
        elif (Indata == "delall"):
            del_all_cmd()

        elif (Indata[0:4] == "run."):
            rum_cmd(Indata[4:])

if __name__=="__main__":
    main()