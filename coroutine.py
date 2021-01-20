def searcher():
    import time
    book="3 men in a boat"
    time.sleep(3)

    while True:
        text= (yield)
        if text in book:
            print("Your text is present in a book")
        else:
            print("Its not present")


search=searcher()
next(search)
search.send("men")
input("Press any key")
search.send("talib")
search.close()