import gdb
import string  
alphabet = string.ascii_uppercase + string.ascii_lowercase +string.digits+"{_}"
file_path = "/home/semloh/picoCTF/easy_GDB/input.txt"
flag = "picoCTF{"
gdb.execute("b*0x565559a7")
while ('}' not in flag):
    for c in alphabet:
        test = flag + c +'\n'
        gdb.execute("shell touch {}".format(file_path))
        with open(file_path, "w") as file:
         file.write(test)
        gdb.execute("run <input.txt\n")
        print(test)
        print("Number of word is correct: ",len(flag))
        address = "0xffffd3b4"
        gdb_output = gdb.execute("x/x {}".format(address), to_string=True)
        result = gdb_output.split()[1].strip()
        result = int(result,16)
        gdb.execute("shell rm {}".format(file_path))
        if(result > len(flag)):
            flag +=c
            print(flag)
            break

print("Found the flag: "+flag)