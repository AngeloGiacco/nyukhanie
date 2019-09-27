import hashlib,glob

def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n") or x.endswith("\r"): return x[:-1]
    return x

pass_hash = raw_input("Enter hash: ")

word_filename = raw_input("Enter file name: ")
for txtfile in glob.glob("*.txt"):
    print(txtfile[:-4])
    if txtfile == word_filename: # is it name of file with or without extension
        pass
    elif txtfile[:-4] == word_filename:
        word_filename += ".txt"
    else:
        print("no file found")
        quit()

try:
    word_file = open(word_filename,"r")
except:
    print("no file found")
    quit()

for word in word_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("Password has been found.")
        print("Password is "+chomp(word))
        break
else:
    print("Password is not in the list.")
