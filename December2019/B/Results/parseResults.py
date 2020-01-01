import re, os, sys, json, getch

def compileUSACO():
    results = open("results.out", "r")
    for i in range(8):
        _ = results.readline()

    def normalize(s):
        s = s.replace(" ", "\t")
        return re.sub(r'\t+', '\t', s)

    c1, c2, c3 = normalize(results.readline()).split()[-3:]

    compiled = {'intl': []}

    s = results.readline()
    while s[:11] != "Pre-College":
        s = normalize(s).split()
        country = s[0]
        year = s[1]
        name = s[2] + " " + s[3]
        score = s[4]
        c1s = "".join(s[5:15])
        c2s = "".join(s[15:25])
        c3s = "".join(s[25:35])
        result = {"name": name, "year": year, "country": country, "score": {"total": score, c1: c1s, c2: c2s, c3: c3s}}
        compiled['intl'].append(result)
        s = results.readline()

    with open("compiledResults.out", "w+") as f:
        f.write(json.dumps(compiled, indent=4))

def optionChooser(again=False):
    try:
        if not again:
            print("USACO Results:\n\n(q) Quit\n(0) Compile Results\n(1) Get All Results\n(2) Search")
        chooser = getch.getch().lower()
        if chooser == '\x7f':
            chooser = optionChooser(True)
        if chooser not in ["q", "0", "1", "2"]:
            print("Invalid Option, please try again.")
            chooser = optionChooser(True)
        return chooser
    except ValueError:
        print("Invalid Option, please try again.")
        chooser = optionChooser(True)

def optionChooser2(again=False):
    try:
        if not again:
            print("Search by?\n\n(b) Back\n(n) Name\n(s) Score\n(c) Country")
        chooser = getch.getch().lower()
        if chooser == '\x7f':
            chooser = optionChooser2(True)
        if chooser not in ["b", "n", "s", "c"]:
            print("Invalid Option, please try again.")
            chooser = optionChooser2(True)
        return chooser
    except ValueError:
        print("Invalid Option, please try again.")
        chooser = optionChooser2(True)

def main(chooser=None, option=None):
    if not chooser:
        os.system("clear")
        chooser = optionChooser()
        os.system("clear")
    if chooser == "q":
        sys.exit(0)
    elif chooser == "0":
        compileUSACO()
    elif chooser == "1":
        try:
            with open("compiledResults.out", "r") as f:
                print(f.read())
                chooser = getch.getch()
                os.system("clear")
        except:
            compileUSACO()
            with open("compiledResults.out", "r") as f:
                print(f.read())
                chooser = getch.getch()
                os.system("clear")
                main()
    elif chooser == "2":
        if not option:
            option = optionChooser2()
        results = json.loads(open("compiledResults.out").read())
        if option == "b":
            main()
        elif option == "n":
            s = ""
            ch = ""
            os.system("clear")
            print("Name: ", end="", flush=True)
            while ch != '\n':
                ch = getch.getch()
                if ch == "\x7f":
                    s = s[:-1]
                if ch.isalpha() or ch == " ":
                    s += ch
                os.system('clear')
                print("Name: " + s, end="", flush=True)
            search = [result for result in results['intl'] if s.lower() == result["name"].lower()]
            if len(search) == 0: search = [result for result in results['intl'] if s.lower() in result["name"].lower()]
            os.system('clear')
            if len(search) == 0:
                print("Nothing was found. Go (h)ome.")
                getch.getch()
                main()
            if len(search) == 1:
                score = search[0]["score"]
                total = search[0]["score"]["total"]
                score.pop("total")
                print("Name: "+search[0]["name"] + "\nYear: " + search[0]["year"] + "\nCountry: " + search[0]["country"] + "\nScore: " + total)
                for key in score:
                    print("    " + key + ": " + score[key])
                getch.getch()
                main()
            else:
                print("There were multiple results. Which one?\n")
                for result in search:
                    print("(" + str(search.index(result) + 1) + ") " + result["name"] + "(" + result["year"] + ") from " + result["country"])
                try:
                    getchr = int(getch.getch())
                    if 1 <= int(getchr) <= len(search):
                        i = int(getchr) - 1
                        score = search[i]["score"]
                        total = search[i]["score"]["total"]
                        score.pop("total")
                        os.system("clear")
                        print("Name: "+search[i]["name"] + "\nYear: " + search[i]["year"] + "\nCountry: " + search[i]["country"] + "\nScore: " + total)
                        for key in score:
                            print("    " + key + ": " + score[key])
                        getch.getch()
                        main()
                except:
                    pass
                main("2", "n")
        elif option == "s":
            s = ""
            ch = ""
            os.system("clear")
            print("Score: ", end="", flush=True)
            while ch != '\n':
                ch = getch.getch()
                if ch == "\x7f":
                    s = s[:-1]
                if ch.isnumeric() or ch == " ":
                    s += ch
                os.system('clear')
                print("Score: " + s, end="", flush=True)
            search = [result for result in results['intl'] if s == result["score"]["total"]]
            os.system('clear')
            print(str(len(search)) + " number of people got this score:\n")
            for result in search:
                print("(" + str(search.index(result) + 1) + ") " + result["name"] + "(" + result["year"] + ") from " + result["country"])
            try:
                getchr = ""
                while "\n" not in getchr:
                    ch = str(getch.getch())
                    if ch == "q":
                        getchr = ""
                        break
                    getchr += str(getch.getch())
                getchr.replace("\n", "")
                if 1 <= int(getchr) <= len(search):
                    i = int(getchr) - 1
                    score = search[i]["score"]
                    total = search[i]["score"]["total"]
                    score.pop("total")
                    os.system("clear")
                    print("Name: "+search[i]["name"] + "\nYear: " + search[i]["year"] + "\nCountry: " + search[i]["country"] + "\nScore: " + total)
                    for key in score:
                        print("    " + key + ": " + score[key])
                    getch.getch()
                    main()
            except:
                pass
            main("2", "s")
        elif option == "c":
            s = ""
            ch = ""
            os.system("clear")
            print("Country Code: ", end="", flush=True)
            while ch != '\n':
                ch = getch.getch()
                if ch == "\x7f":
                    s = s[:-1]
                if ch.isalpha():
                    s += ch
                os.system('clear')
                print("Country Code: " + s, end="", flush=True)
            search = [result for result in results['intl'] if s == result["country"]]
            os.system('clear')
            print(str(len(search)) + " number of people did this USACO contest from " +  s + ":\n")
            for result in search:
                print("(" + str(search.index(result) + 1) + ") " + result["name"] + "(" + result["year"] + ") from " + result["country"])
            try:
                getchr = ""
                while "\n" not in getchr:
                    ch = str(getch.getch())
                    if ch == "q":
                        getchr = ""
                        break
                    getchr += str(getch.getch())
                getchr.replace("\n", "")
                if 1 <= int(getchr) <= len(search):
                    i = int(getchr) - 1
                    score = search[i]["score"]
                    total = search[i]["score"]["total"]
                    score.pop("total")
                    os.system("clear")
                    print("Name: "+search[i]["name"] + "\nYear: " + search[i]["year"] + "\nCountry: " + search[i]["country"] + "\nScore: " + total)
                    for key in score:
                        print("    " + key + ": " + score[key])
                    getch.getch()
                    main()
            except:
                pass
            main("2", "c")

if __name__ == "__main__":
    main()