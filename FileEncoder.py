import main

ToDna = main.TO_DNA()
ToTxt = main.To_Txt()

decoded = open('decoded.txt', 'r', encoding='utf-8')
encoded = open('encoded.txt','w',encoding='utf-8')

deco = decoded.read()

enco = ToDna.txt_to_dna(deco)

encoded.write(enco)