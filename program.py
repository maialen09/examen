import operator
text= "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."


dic = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'Ñ': 0, 'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

for letra in text:

  if letra in dic:
     dic[letra]= dic[letra] + 1
    
dicm = {1: 'E', 2: 'A',3:'O' ,4: 'L', 5:'S', 6: 'N', 7:'D' , 8: 'R', 9:'U' , 10:'I' , 11: 'T', 12:'C' , 13: 'P', 14: 'M', 15:'Y'  , 16: 'Q', 17:'B' , 18:'H' , 19:'G' , 20: 'F', 21:'V' , 22:'J' , 23: 'Ñ', 24: 'Z', 25: 'X', 26: 'K', 27:'W' }
i = 1; 

while (i <= 27):   
  max_key = max(dic.items(), key=operator.itemgetter(1))[0]
  dicm[i] = max_key
  del(dic[max_key])
  i = i+1



dicp = {'E': 1, 'A': 2,'O':3 ,'L': 4, 'S':5 , 'N': 6, 'D':7 , 'R': 8, 'U':9 , 'I':10 , 'T': 11, 'C':12 , 'P': 13, 'M': 14, 'Y':15  , 'Q': 16, 'B':17 , 'H':18 , 'G':19 , 'F': 20, 'V':21 , 'J':22 , 'Ñ': 23, 'Z': 24, 'X': 25, 'K': 26, 'W':27 }

 
for letra in text:
  if letra in dicp:
    num = dicp[letra]
    let = dicm[num]
  else:
    let = letra 
  print(let,end='')
     
textonuevo = "AZF EBWWBGN PZWNX ÑH ENWNRÑFGÑ CBÑ, X JB PXFÑWX, PÑVZW ÑUTWÑJXQX AZPZ AZPQXGNW XH KXJANJPZ EÑJEÑ BF AWNGÑWNZ EÑ NFEÑTÑFEÑFANX EÑ AHXJÑ, X ENKÑWÑFANX EÑH AZHXQZWXANZFNJPZ KWÑFGÑTZTBHNJGX EÑ HX ENWÑAANZF XFXWCBNJGX. EBWWBGN KBÑ BF KXAGZW EÑ TWNPÑW ZWEÑF ÑF ÑH TXTÑH EÑ HX AHXJÑ ZQWÑWX ÑF AXGXHBFMX ÑF VBHNZ EÑ 1936. TÑWZ EBWWBGN, AZPZ ZABWWÑ AZF HXJ TÑWJZFXHNEXEÑJ ÑF HX DNJGZWNX, FZ AXMZ EÑH ANÑHZ. TÑWJZFNKNAXQX HX GWXENANZF WÑvZHBANZFXWNX EÑ HX AHXJÑ ZQWÑWX. JB ÑFZWPÑ TZTBHXWNEXE ÑFGWÑ HX AHXJÑ GWXQXVXEZWX, WÑKHÑVXEX ÑF ÑH ÑFGNÑWWZ PBHGNGBENFXWNZ ÑF QXWAÑHZFX ÑH 22 EÑ FZvNÑPQWÑ EÑ 1936, PBÑJGWX ÑJX NEÑFGNKNAXANZF. JB PBÑWGÑ KBÑ JNF EBEX BF RZHTÑ ZQVÑGNvZ XH TWZAÑJZ WÑvZHBANZFXWNZ ÑF PXWADX. JNF EBWWBGN CBÑEZ PXJ HNQWÑ ÑH AXPNFZ TXWX CBÑ ÑH ÑJGXHNFNJPZ, AZF HX AZPTHNANEXE EÑH RZQNÑWFZ EÑH KWÑFGÑ TZTBHXW M EÑ HX ENWÑAANZF XFXWCBNJGX, GÑWPNFXWX ÑF PXMZ EÑ 1937 HX GXWÑX EÑ HNCBNEXW HX WÑvZHBANZF, EÑJPZWXHNIXFEZ X HX AHXJÑ ZQWÑWX M KXANHNGXFEZ AZF ÑHHZ ÑH TZJGÑWNZW GWNBFKZ KWXFCBNJGX."

textonuevo = textonuevo.replace('E', 'd')
textonuevo = textonuevo.replace('Ñ', 'e')
textonuevo = textonuevo.replace('H', 'l')
textonuevo = textonuevo.replace('F', 'n')
textonuevo = textonuevo.replace('X', 'a')
textonuevo = textonuevo.replace('Z', 'o')
textonuevo = textonuevo.replace('P', 'm')
textonuevo = textonuevo.replace('Q', 'b')
textonuevo = textonuevo.replace('W', 'r')
textonuevo = textonuevo.replace('A', 'c')
textonuevo = textonuevo.replace('N', 'i')
textonuevo = textonuevo.replace('V', 'j')
textonuevo = textonuevo.replace('J', 's')
textonuevo = textonuevo.replace('B', 'u')
textonuevo = textonuevo.replace('G', 't')
textonuevo = textonuevo.replace('K', 'f')
textonuevo = textonuevo.replace('T', 'p')
textonuevo = textonuevo.replace('R', 'g')
textonuevo = textonuevo.replace('M', 'y')
textonuevo = textonuevo.replace('U', 'x')
textonuevo = textonuevo.replace('I', 'z')
textonuevo = textonuevo.replace('C', 'q')
textonuevo = textonuevo.replace('D', 'h')
print("----------------------------------------------------------------")
print(textonuevo)


  
  




