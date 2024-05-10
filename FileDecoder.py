import main

ToDna = main.TO_DNA()
ToTxt = main.To_Txt()

decoded = open('decoded.txt', 'w', encoding='utf-8')
encoded = open('encoded.txt','r',encoding='utf-8')

enco = encoded.read()

deco = ToTxt.dna_to_txt(enco)

decoded.write(deco)