import hashlib,glob
from threading import Thread
def chomp(x):
    if x.endswith("\r\n"): return x[:-2]
    if x.endswith("\n") or x.endswith("\r"): return x[:-1]
    return x

def get_file():
    word_filename = raw_input("Enter file name: ")
    for txtfile in glob.glob("*.txt"):
        if txtfile == word_filename: # is it name of file with or without extension
            pass
        elif txtfile[:-4] == word_filename:
            word_filename += ".txt"
        else:
            print("no file found")
            quit()
    try:
        word_file = open(word_filename,"r")
        return word_file
    except:
        print("no file found")
        quit()

def test_word(w,pass_hash):
    enc_wrd = w.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        flag = 1
        print("Password has been found.")
        print("Password is "+chomp(w))
        return True
    else:
        return False

def main():
    pass_hash = raw_input("Enter hash: ")
    word_file = get_file()
    flag = 0
    for word in word_file:
        t = Thread(target = test_word, args = (word,pass_hash))
        t.start()
    if flag == 0:
        print("Password is not in the list.")

if __name__ == '__main__':
    main()
