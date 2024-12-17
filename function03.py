#percorrer toda a lista de produtos
#para cada produto, verificar se ele é bebida alcoolica
#se for bebida alcoolica, exibir a mensagem enviada
def ehacollico(bebida):
    bebida = bebida.upper()
    if "BSE" in bebida:
        return True
    else:
        return False
    
    
produtos = ["bse125","bse125","tfg123","beg1234"]

for produto in produtos:
    if ehacollico(produto):
        print(f"enviar produto\n {produto} para bebida aclica")