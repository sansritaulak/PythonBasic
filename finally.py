def process_file():
    try:
        f = ("/home/sansrita/Desktop/Python/text.txt")
        x = 1/0
    except FileNotFoundError  as e:
        print("Inside Except")
    #code in finally block will excecute no matter what.
    finally:
        print("cleaning up file")
        f.close()
process_file()
