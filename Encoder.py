import main

ToDna = main.TO_DNA()
ToTxt = main.To_Txt()

while 1:
  mode = input("wich mode ? TODNA, TOTXT or BOTH ? ")
  if mode.upper() == "TODNA":
    txt_in = input("your text : ")
    dna_out = ToDna.txt_to_dna(txt_in)
    print(dna_out)
  elif mode.upper() == "TOTXT":
    dna = input("your dna : ")
    txt_fin = ToTxt.dna_to_txt(dna)
    print(txt_fin)
  elif mode.upper() == "BOTH":
    txt_in = input("your text : ")
    dna_out = ToDna.txt_to_dna(txt_in)
    txt_fin = ToTxt.dna_to_txt(dna_out)
    print(txt_fin)
  else:
    print("error")

