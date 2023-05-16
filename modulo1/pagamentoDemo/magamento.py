'''
 Um script para uma solução em que , introduzida uma quantia em euros para pagamento 
 de uma determinada mercadoria, cujo preço também deve ser introduzido, 
 indique o troco a ser entregue ao cliente e envie de seguida, 
 a mensagem PAGAMENTO EFETUADO. 
 No caso de não haver direito a troco, deve apresentar, anteriormente, 
 a mensagem QUANTIA ENTREGUE PELO CLIENTE IGUAL AO VALOR DA MERCADORIA.
'''
quantia = float(input("            Quantia em euros? "))
preco = float(  input("Preço da mercadoria em euros? "))

troco = quantia - preco
if troco > 0:
    # print("O troco é", str(troco) + '€')
    print("O troco é ", troco, '€', sep ='')
    print("PAGAMENTO EFETUADO")
elif troco == 0:
    print("QUANTIA ENTREGUE PELO CLIENTE IGUAL AO VALOR DA MERCADORIA")
    print("PAGAMENTO EFETUADO")
else:
    print("A quantia", str(quantia) + '€', "introduzida é insuficiente", end=' ')
    print("para pagar", str(preco) + '€')
    print("PAGAMENTO NÃO EFETUADO")
