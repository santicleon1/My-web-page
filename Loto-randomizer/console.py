import Igre

igra = input("Moguće igre:\nEuro Jackpot\nLoto 7\nLoto 6\nSve ili Ništa\nIzaberi igru: ")

if igra == "Euro Jackpot":
    import Igre.eurojackpot

elif igra == "Loto 7":
    import Igre.loto7

elif igra == "Loto 6":
    import Igre.loto6

elif igra == "Sve ili Ništa":
    import Igre.sveilinista

input("Stisni Enter da zatvoriš prozor.")