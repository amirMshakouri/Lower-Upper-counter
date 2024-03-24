def letters(alphabet):
    upper_letters = alphabet.count("A") + alphabet.count("B") + alphabet.count("C") + alphabet.count("D") + alphabet.count("E") + alphabet.count("F") + alphabet.count("G") + alphabet.count("H") + alphabet.count("I") + alphabet.count("J") + alphabet.count("K") + alphabet.count("L") + alphabet.count("M") + alphabet.count("N") + alphabet.count("O") + alphabet.count("P") + alphabet.count("Q") + alphabet.count("R") + alphabet.count("S") + alphabet.count("T") + alphabet.count("U") + alphabet.count("V") + alphabet.count("W") + alphabet.count("X") + alphabet.count("Y") + alphabet.count("Z") 
    lower_letters = alphabet.count("a") + alphabet.count("b") + alphabet.count("c") + alphabet.count("d") + alphabet.count("e") + alphabet.count("f") + alphabet.count("g") + alphabet.count("h") + alphabet.count("i") + alphabet.count("j") + alphabet.count("k") + alphabet.count("l") + alphabet.count("m") + alphabet.count("n") + alphabet.count("o") + alphabet.count("p") + alphabet.count("q") + alphabet.count("r") + alphabet.count("s") + alphabet.count("t") + alphabet.count("u") + alphabet.count("v") + alphabet.count("w") + alphabet.count("x") + alphabet.count("y") + alphabet.count("z") 

    print(f"number of lowercase letters is {lower_letters} ")
    print(f"number of uppercase letters is {upper_letters} ")

a = input(" please enter your praghraph : ")
letters(a)
