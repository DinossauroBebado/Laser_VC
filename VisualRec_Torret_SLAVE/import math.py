import math
import random

lista=[]


def Simpson(linf,lsup,precisao,adicionar,funcao,s,*args):

    passo=1/30
    n=(lsup-linf)/passo+1
    soma=adicionar
    cont=1
    x=linf
    while True:
        k=funcao(x,*args)
        brek=False
        
        if k<10**(-precisao-1):
            for i in range(5,0,-1):
                if k<10**(-precisao-i):
                    pular=True
                    print("O valor de {}({}) é 10^{} menor do que o necessário!".format(funcao.__name__,round(x,precisao),i))
                    try:
                        funcao(x+10*i*passo*precisao**3,*args)
                    except ValueError:
                        pular=False

                    if pular:
                        x+=10*i*passo*precisao**3
                        cont+=1
                        brek=True
                        break
            if brek:
                continue
        
        
        print("{}({})={}".format(funcao.__name__,round(x,precisao),round(funcao(x,*args),precisao)))
        if cont==n or x>=lsup:
            soma+=k
            break
        elif cont==1:
            k
            soma+=k
        elif cont%2==0:
            soma+=4*k
        elif cont%2==1:
            soma+=2*k      

        cont+=1
        x+=passo
    
    if s:
        print('\n')
        print(" {} ".format(lsup))
        print(" /")
        print(" | {}(x) dx = {}".format(funcao.__name__,round(soma*passo/3,precisao)))
        print(" /")
        print(" {}\n".format(linf))

    return(round(soma*passo/3,precisao))

def Beta(a,b):
    return math.gamma(a)*math.gamma(b)/math.gamma(a+b)

def teste(x):
    return(math.sqrt(1-x**2))

def tStudent(x,v):
    return ((1+x**2/v)**(-(v+1)/2)/math.sqrt(v)/Beta(1/2,v/2))

def Chi_quadrado(x,v):
    return(x**(v/2-1)*math.exp(-x/2)/(2**(v/2)*math.gamma(v/2)))

def F(x,v1,v2):
    return(1/Beta(v1/2,v2/2)*(v1/v2)**(v1/2)*x**(v1/2-1)*(1+v1*x/v2)**(-(v1+v2)/2))

def invSimpson(linf,adicionar,precisao,objetivo,funcao,passo_ajustavel,*args):
    if type(objetivo)==int or type(objetivo)==float:
        objetivo=[objetivo]
    
    passo_min=precisao**(-6)/2
    passo_max=precisao**(-4)
    ar=[round(x,precisao) for x in args]
    constante=math.floor(25/precisao)
    respostas=[]

    for obj in objetivo:
        soma=adicionar
        cont=0
        x=linf
        passo=1/((precisao)**4)

        while True:
            k=funcao(x,*args)
            if cont%constante==0 and passo_ajustavel:
                #print("amplitude de {:.3f}".format(50*passo))
                deriv=(funcao(x+constante*passo,*args)-k)/(constante*passo)
                #print("A derivada de {}({}) em [{:.3f},{:.3f}] é aproximadamente {:.3f}".format(funcao.__name__,ar,x,x+constante*passo,deriv))            
                if deriv!=0:
                    if passo_min<passo/(abs(deriv)+0.95)<passo_max:
                        passo/=abs(deriv)+0.95
                    elif passo/(abs(deriv)+0.95)>passo_max:
                        passo=passo_max
                    else:
                        passo=passo_min
                #    print("Ajustando passo para {:.3f}".format(passo))
                #print("Resultado parcial: {}".format(round(soma,precisao)))


            if cont>150/passo:
                print("O método inverso de simpson não convergiu para a função {}({}), com a sequencia acima ".format(funcao.__name__,ar))
                print("Passos dados: {}".format(cont))
                print("Objetivo={}\nResultado obtido até o erro: {}".format(round(obj,precisao),round(soma,precisao)))
                print("Posição de x: {:.3f}".format(x))
                if abs(obj-soma)<10**(-precisao):
                    print("Belo acerto!")
                elif abs(obj-soma)<10**(-precisao+1):
                    print("Razoável acerto...")
                else:
                    print("Erro grosseiro!")
                    x=0
                break
        
            brek=False
            if k<10**(-precisao-3):
                #print("Valor muito pequeno detectado")
                for i in range(5,2,-1):
                    if k<10**(-precisao-i):
                        pular=True
                #        print("O valor de {}({}) é 10^{} menor do que o necessário!".format(funcao.__name__,round(x,precisao),i))
                    
                        try:
                            alfa=funcao(x+precisao**i*passo,*args)
                            deriv1=(alfa-k)/(precisao**i*passo)
                #            print("A derivada de {}({}) em [{:.3f},{:.3f}] é aproximadamente {:.3f}".format(funcao.__name__,ar,x,x+precisao**i*passo,deriv1))
                        except ValueError:
                            pular=False

                        if deriv>0.1 or deriv1>0.5:
            #                print("A função cresce muito rapidamente, então não haverá pulos...")
                            pular=False

                        if pular:
                            x+=precisao**i*passo
                #            print("Pulamos para x={:.3f}".format(x))
                            cont+=1
                            brek=True
                            break
                if brek:
                    continue
        
            #print("{}({})={}".format(funcao.__name__,round(x,precisao),round(funcao(x,*args),precisao)))
            if abs(soma-obj)<10**(-precisao) or soma>obj:
                print("O método inverso de simpson convergiu para a função {}({}), com a sequencia acima ".format(funcao.__name__,ar))
                print("Passos dados: {}".format(cont))
                print("Objetivo={}\nResultado obtido: {}".format(round(obj,precisao),round(soma,precisao)))
                print("Posição de x: {:.3f}".format(x))
                if abs(obj-soma)<10**(-precisao):
                    print("Belo acerto!")
                elif abs(obj-soma)<10**(-precisao+1):
                    print("Razoável acerto...")
                else:
                    print("Erro grosseiro!")
            
                break
            elif cont==0:
                soma+=k*passo/3
            elif cont%2==1:
                soma+=4*k*passo/3
            elif cont%2==0:
                soma+=2*k*passo/3      

            cont+=1
            x+=passo
            #print("resultado parcial={}".format(round(soma*passo/3,precisao)))
            #print("Aperte enter")
            #input('')
        pontuacao=round(10**(-precisao)/((obj-soma)**2*cont),2)
        if pontuacao>50:
            pontuacao=50
        print("Pontuação: {:.3f}".format(pontuacao))
        print("Aperte enter")
        input('')
        respostas.append((round(x,precisao),pontuacao))
    return respostas

def Normal(valor,media,sigma):

    valorp=(valor-media)/sigma 
    
    return(math.exp(-valorp**2/2)/math.sqrt(2*math.pi))

def inv(k,precisao,funcao,*args):
    #retorna valor tal que P(x<=valor)=k

    linf=-4
    lsup=4
    valor=0
    cont=1

    while True:
        print("{}° tentativa de aproximar valor".format(cont))
        cont=cont+1

        valor=linf+(lsup-linf)*(k-funcao(linf,*args))/(funcao(lsup,*args)-funcao(linf,*args))


        norm=funcao(valor,*args)
        print("Valor: {:.4f}\nP(x<={:.4f})={:.4f}\n".format(valor,valor,norm))
        

        if abs(norm-k)<10**(-precisao):
            print("P(x<={:.4f})={:.4f}".format(valor,k))
            return(round(valor,precisao))
        elif norm<k:
            linf=valor
        elif norm>k:
            lsup=valor

def receber_sequencia():
    lista=[]
    denominador=10**int(input('Quantas casas decimais tem os dados?'))
    if denominador!=1:
        while True:
            valor=input('Digite um valor\n')
            if valor=='n':
                break
            lista.append(int(valor)/denominador)
    else:
        while True:
            valor=input('Digite um valor\n')
            if valor=='n':
                break
            lista.append(int(valor))
    return lista

def gerar_sequencia():
    lista=[]
    tamanho=random.randint(6,45)
    denominador=random.randint(0,2)
    for i in range(tamanho):
        lista.append(round(random.randint(10*10**denominador,100*10**denominador)*10**-denominador,denominador))
    print("Sequencia gerada:")
    print(lista)
    return lista

def testar_convergencia():
    while True:
        convergencias=0
        divergencias=0
        lt=[]
        for i in range(150):
            #l=[]
            print("\nTeste de convergência numero {}".format(i))
            #l=gerar_sequencia()
  

            #media=sum(l)/len(l)
            #desviop=0
            #for numero in l:
            #    desviop+=(numero-media)**2
            #desviop=(desviop/(len(l)-1))**(1/2)
            funcao=random.randint(0,3)
            if funcao==0:
                grau1=round(random.randint(1,20),2)
                grau2=round(random.randint(1,20),2)
                k,pont=invSimpson(0.00001,0,3,0.995,F,True,grau1,grau2)
                lt.append(pont)
            elif funcao==1:
                grau1=round(random.randint(1,30),2)
                k,pont=invSimpson(0.00001,0,3,0.995,Chi_quadrado,True,grau1)
                lt.append(pont)
            elif funcao==2:
                grau1=round(random.randint(1,30),2)
                k,pont=invSimpson(-63,0.005,3,0.995,tStudent,True,grau1)
                lt.append(pont)
            elif funcao==3:
                #media=round(random.randint(1,30),2)
                #var=round(random.randint(1,30),2)
                #k,pont=invSimpson(-4,0.0001,3,1,Normal,True,media,var)
                k,pont=invSimpson(-4,0.0001,3,1,Normal,True,0,1)
                lt.append(pont)
            if k==0:
                divergencias+=1
            else:
                convergencias+=1

    
        if divergencias==0:
            print("\n\nConvergências:{} Divergências: {}".format(convergencias,divergencias))
        else:
            print("\n\nConvergências:{} Divergências: {} Conv/Div: {}".format(convergencias,divergencias,round(convergencias/divergencias,2)))
            print("\nSequencia das pontuações com passo alternado ligado:\n")
            analisar_sequencia(lt)

        print("Aperte enter para um novo teste, ou digite n para encerrar")
        k=input('')
        if k=='n':
            exit()

def analisar_sequencia(lista):
    dicio={'Média Aritmética':0,'Média Geometrica':1,'Média Harmonica':0,'Desvio Padrão':0,'Desvio Médio':0,'Resultado do Estimador':0,'Tamanho':len(lista)}
    
    


    for numero in lista:
        dicio["Resultado do Estimador"]+=numero
        dicio["Média Aritmética"]+=numero
        dicio["Média Geometrica"]*=numero
        
        if numero!=0:
            dicio["Média Harmonica"]+=1/numero
            
    dicio["Média Aritmética"]/=len(lista)


    print('Média Aritmética: {:.4f}'.format(dicio["Média Aritmética"]))
    print('Média Geométrica: {:.4f}'.format(dicio["Média Geometrica"]**(1/len(lista))))
    print('Média Harmônica:  {:.4f}'.format(len(lista)/dicio["Média Harmonica"]))

    if len(lista)>1:
        for numero in lista:
        
            dicio["Desvio Padrão"]+=(numero-dicio["Média Aritmética"])**2
            dicio["Desvio Médio"]+=abs(numero-dicio["Média Aritmética"])

        dicio["Desvio Padrão"]=(dicio["Desvio Padrão"]/(len(lista)-1))**(1/2)
        print("Resultado do estimador: {:.4f}".format(dicio['Resultado do Estimador']/2/len(lista)))
        print('Desvio padrão: {:.4f}'.format(dicio["Desvio Padrão"]))
        print('Desvio médio {:.4f}'.format(dicio["Desvio Médio"]/len(lista)))
    print("Tamanho: {}".format(len(lista)))
    dicio['dpt']=dicio['Desvio Padrão']**2/dicio['Tamanho']
    return dicio

    #lista=sorted(lista)

    #def percentil(vh):
        #u=(len(lista)+1)*vh/100
        #alfa=math.floor(u)
        #return lista[alfa-1]+(u-alfa)*(lista[alfa]-lista[alfa-1])

    #print('Assimetria em quartis: {:.4f}'.format((percentil(75)+percentil(25)-2*percentil(50))/(percentil(75)-percentil(25))))

    #soma_estimador=soma_estimador/len(lista)

    #print('Resultado do estimador (assumindo uma distribuição Normal): {:.4f}'.format(soma_estimador))

    print("O que deseja fazer?")
    opcoes={"encontrar a diferença entre duas medias (dm)":['dm',]}
    
    return 

def teste(significancia,*dicionarios):

    
    print("Deseja um teste para (m)édia, (v)ariancia, (p)roporção ou (n)ão?")
    print("Digite d na frente caso queira a diferença entre duas coisas")
    entrada=input("")
    print("Qual é o tipo do teste?")
    print("Lateral a esquerda'<' Lateral a direita '>' bilateral '!=")
    print(" o teste certo completa o sinal: interesse ___ referência")
    tipo_teste=input('')

    def regiao_nao_critica(tipo_teste,z1,z2,estatistica,referencia,significancia):
        #Se a estatística estiver dentro desse intervalo, não rejeite a hipótese nula
        #z2 é igual a 0 no teste lateral a esquerda e lateral a direita
        if tipo_teste=='<':
            rejeitar=estatistica<z1
        elif tipo_teste=='>':
            rejeitar=estatistica>z1
        else:
            rejeitar=z1<estatistica<z2

        if not rejeitar:
            print("Interesse={} a {}% de significancia".format(referencia,100*significancia))
            print('A hipótese nula não deve ser rejeitada!')
            print("{:.3f}".format(estatistica+1))
        else:
            print("Interesse {} {} a {}% de significancia".format(tipo_teste,referencia,100*significancia))
            print('A hipótese nula deve ser rejeitada!')
            print("{:.3f}".format(estatistica-1))
        exit()


    if entrada=='n':
        exit('')
    else:
        print("Qual é a significancia desejada para o teste? Número entre 0 e 1")
        significancia=float(input(''))
        
        precisao=5

    if entrada=='m':
        print("Digite o desvio padrao populacional, ou n se não conhecê-lo")
    
        desviopp=input('')
    
        if desviopp=='n':
            l=receber_sequencia()
            carac=analisar_sequencia(l)

            #tcrit=math.sqrt(carac["Tamanho"])*(carac["Média Aritmética"]-21)/carac["Desvio Padrão"]

            zpar=1-confianca/2
            #zpar=0.05
            z,k=invSimpson(-63,0.005,precisao,zpar,tStudent,True,carac['Tamanho']-1)
        
            #if tcrit<z:
            #    print("Hipótese nula deve ser rejeitada a alfa={}".format(zpar))
            #else:
            #    print("Hipótese nula não deve ser rejeitada a alfa={}".format(zpar))

            #print(tcrit)

            #exit()


            dpzsqrt=round(carac['Desvio Padrão']*z/math.sqrt(carac['Tamanho']),precisao)
            print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),carac['Média Aritmética']-dpzsqrt,carac['Média Aritmética']+dpzsqrt))
            print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

            exit()
        else:


            funcao=Normal
            referencia=input("Digite a referencia do teste:")

            carac=analisar_sequencia(receber_sequencia())
            n=carac["Tamanho"]
            me=carac["Média Aritmética"]
            
            estatistica=math.sqrt(n)*(me-referencia)/desviopp
            if tipo_teste=='<':
                zpar=significancia
            elif tipo_teste=='>':
                zpar=1-significancia
            else:
                zpar=1-significancia/2
                print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,[0,1],zpar))
                z=input('')
                if z=='n':
                    z=invSimpson(-4,0,precisao,zpar,funcao,True,0,1)
                else:
                    z=float(z)
                regiao_nao_critica(tipo_teste,-z,z,estatistica,referencia,significancia)
            
            print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,[0,1],zpar))
            z=input('')
            if z=='n':
                z=invSimpson(-4,0,precisao,zpar,funcao,True,0,1)
            else:
                z=float(z)
            regiao_nao_critica(tipo_teste,z,0,estatistica,referencia,significancia)

    elif entrada=='dm':
        print("Digite os desvios padrões, ou n se não conhecê-los")
        desviopp=input('')
        if desviopp=='n':
            print('Eles são iguais?')
            desviopp=input('')
            if desviopp=='s':

                carac1=analisar_sequencia(receber_sequencia())
                carac2=analisar_sequencia(receber_sequencia())

                desviopp=round(math.sqrt(((carac1["Tamanho"]-1)*carac1['Desvio Padrão']**2+(carac2["Tamanho"]-1)*carac2['Desvio Padrão']**2)/(carac1['Tamanho']+carac2['Tamanho']-2)),precisao)

                tcrit=round(math.sqrt(carac1['Tamanho']*carac2["Tamanho"])*(carac1["Média Aritmética"]-carac2["Média Aritmética"])/(desviopp*math.sqrt(carac1["Tamanho"]+carac2["Tamanho"])),precisao)




                ep=desviopp*math.sqrt(1/carac1['Tamanho']+1/carac2['Tamanho'])
                #zpar=1-confianca/2
                zpar=1-0.01/2
                print("objetivo={}".format(zpar))

            

                z=round(invSimpson(-63,0.005,precisao+math.floor(math.log10(ep)),zpar,tStudent,True,carac1['Tamanho']+carac2['Tamanho']-2)[0],precisao)
            
                if abs(tcrit)>z:
                    print("Hipótese nula deve ser rejeitada a alfa={}".format(zpar))
                else:
                    print("Hipótese nula não deve ser rejeitada a alfa={}".format(zpar))

                print(tcrit)

                exit()
            
            
            
            
                dpzsqrt=round(ep*z,precisao)
                difmedia=carac1['Média Aritmética']-carac2['Média Aritmética']
                print("Intervalo: {} +/- {}*{}".format(round(difmedia,precisao),z,round(ep,precisao)))
                print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(difmedia-dpzsqrt,precisao),round(difmedia+dpzsqrt,precisao)))
                print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

                exit()
            else:

                carac1=analisar_sequencia(receber_sequencia())
                carac2=analisar_sequencia(receber_sequencia())

                ep=math.sqrt(carac1["Desvio Padrão"]**2/carac1["Tamanho"]+carac2["Desvio Padrão"]**2/carac2["Tamanho"])
                v=(carac1["Tamanho"]-1)*(carac2["Tamanho"]-1)*ep**4/((carac2["Tamanho"]-1)*carac1['Desvio Padrão']**4/carac1['Tamanho']**2+(carac1['Tamanho']-1)*carac2['Desvio Padrão']**4/carac2['Tamanho']**2)
                v=round(v)
            

                zpar=1-confianca/2
                print("objetivo={}".format(zpar))

        


                z=round(invSimpson(-63,0.005,precisao+math.floor(math.log10(ep)),zpar,tStudent,False,v),precisao)
                dpzsqrt=round(ep*z,precisao)
                difmedia=carac1['Média Aritmética']-carac2['Média Aritmética']
                print("Intervalo: {} +/- {}*{}".format(round(difmedia,precisao),z,round(ep,precisao)))
                print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(difmedia-dpzsqrt,precisao),round(difmedia+dpzsqrt,precisao)))
                print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

                exit()

        else:
            desviopp=desviopp.split(' ')
            desviopp1=float(desviopp[0])
            desviopp2=float(desviopp[1])

            carac1=analisar_sequencia(receber_sequencia())
            carac2=analisar_sequencia(receber_sequencia())

            ep=math.sqrt(desviopp1**2/carac1['Tamanho']+desviopp2**2/carac2['Tamanho'])
            zpar=1-confianca/2
            print("objetivo={}".format(zpar))

        

            z=round(invSimpson(-4,0.0001,precisao+math.floor(math.log10(ep)),zpar,Normal,True,0,1),precisao)
            dpzsqrt=round(ep*z,precisao)
            difmedia=carac1['Média Aritmética']-carac2['Média Aritmética']
            print("Intervalo: {} +/- {}*{}".format(round(difmedia,precisao),z,round(ep,precisao)))
            print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(difmedia-dpzsqrt,precisao),round(difmedia+dpzsqrt,precisao)))
            print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

            exit()

    elif entrada=='v':

        funcao=Chi_quadrado
            
        referencia=input("Digite a referencia do teste:")

        carac=analisar_sequencia(receber_sequencia())
        n=carac["Tamanho"]
        dp=carac["Desvio Padrão"]
        me=carac["Média Aritmética"]
            
        estatistica=(n-1)*dp**2/(referencia)**2
        if tipo_teste=='<':
            zpar=significancia
        elif tipo_teste=='>':
            zpar=1-significancia
        else:
            zpar1=significancia/2
            zpar2=1-significancia/2
            print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,n-1,zpar1))
            z1=input('')
            
            if z1=='n':
                z1=invSimpson(-4,0,precisao,zpar1,funcao,True,n-1)
                z2=invSimpson(-4,0,precisao,zpar2,funcao,True,n-1)
            else:
                z1=float(z1)
                z2=float(input(''))
            regiao_nao_critica(tipo_teste,z1,z2,estatistica,referencia,significancia)
            
        print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,n-1,zpar1))
        z=input('')
        if z=='n':
            z=invSimpson(-4,0,precisao,zpar,funcao,True,n-1)
        else:
            z=float(z)
        regiao_nao_critica(tipo_teste,z,0,estatistica,referencia,significancia)


    elif entrada=='dv':
        #carac1=analisar_sequencia(receber_sequencia())
        #carac2=analisar_sequencia(receber_sequencia())

        carac1={'Tamanho':20,'Desvio Padrão':1.5}
        carac2={'Tamanho':14,'Desvio Padrão':2.3}


        razao=round(carac1['Desvio Padrão']**2/carac2['Desvio Padrão']**2,precisao)      
        zpar1=1-confianca/2
        zpar2=confianca/2

        z1=round(invSimpson(0.00001,0,precisao,zpar1,F,True,carac1["Tamanho"]-1,carac2['Tamanho']-1)[0],precisao)
        z2=round(invSimpson(0.00001,0,precisao,zpar2,F,True,carac1["Tamanho"]-1,carac2['Tamanho']-1)[0],precisao)
        print(z1,z2,razao)
    
        print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(razao/z1,precisao),round(razao/z2,precisao)))
        print("Esse intervalo tem amplitude {}".format(razao*(1/z1-1/z2)))

        exit()

    elif entrada=='p':

        n=int(input('Digite quantos eventos foram testados\n'))
        p=int(input('Digite quantos eventos foram bem-sucedidos\n'))
    
        p=p/n
        zpar=1-significancia/2

        funcao=Normal
            
        referencia=input("Digite a referencia do teste:")

        carac=analisar_sequencia(receber_sequencia())
        n=carac["Tamanho"]
        dp=carac["Desvio Padrão"]
        me=carac["Média Aritmética"]
            
        estatistica=(n-1)*dp**2/(referencia)**2
        if tipo_teste=='<':
            zpar=significancia
        elif tipo_teste=='>':
            zpar=1-significancia
        else:
            zpar1=significancia/2
            zpar2=1-significancia/2
            print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,n-1,zpar1))
            z1=input('')
            
            if z1=='n':
                z1=invSimpson(-4,0,precisao,zpar1,funcao,True,n-1)
                z2=invSimpson(-4,0,precisao,zpar2,funcao,True,n-1)
            else:
                z1=float(z1)
                z2=float(input(''))
            regiao_nao_critica(tipo_teste,z1,z2,estatistica,referencia,significancia)
            
        print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,n-1,zpar1))
        z=input('')
        if z=='n':
            z=invSimpson(-4,0,precisao,zpar,funcao,True,n-1)
        else:
            z=float(z)
        regiao_nao_critica(tipo_teste,z,0,estatistica,referencia,significancia)





        z,k=invSimpson(-4,0.0001,precisao,zpar,Normal,True,0,1)
        ep=math.sqrt(p*(1-p)/n)
        print(z,ep)
        linf=round(p-z*ep,precisao)
        lsup=round(p+z*ep,precisao)

        print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),linf,lsup))
        print("Esse intervalo tem amplitude {}".format(lsup-linf))

        exit()

    elif entrada=='dp':
        n1=int(input('Digite quantos eventos foram testados\n'))
        p1=int(input('Digite quantos eventos foram bem-sucedidos\n'))

        n2=int(input('Digite quantos eventos foram testados\n'))
        p2=int(input('Digite quantos eventos foram bem-sucedidos\n'))
    
        p1=p1/n1
        p2=p2/n2
        zpar=1-confianca/2

    
        z,k=invSimpson(-4,0.0001,precisao,zpar,Normal,True,0,1)
        ep=math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2)
        print(z,ep)
        linf=round(p1-p2-z*ep,precisao)
        lsup=round(p1-p2+z*ep,precisao)

        print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),linf,lsup))
        print("Esse intervalo tem amplitude {}".format(lsup-linf))

        exit()


        return

def parear_sequencia(lista1,lista2):
    lista3=[]
    for i in range(len(lista1)):
        lista3.append(lista1[i]-lista2[i])
    return lista3
#gerar_sequencia()

def regiao_nao_critica(tipo_teste,z1,z2,estatistica,referencia,significancia):
        #Se a estatística estiver dentro desse intervalo, não rejeite a hipótese nula
        #z2 é igual a 0 no teste lateral a esquerda e lateral a direita
        if tipo_teste=='<':
            rejeitar=estatistica<z1
        elif tipo_teste=='>':
            rejeitar=estatistica>z1
        else:
            rejeitar=z1<estatistica<z2

        if not rejeitar:
            print("Interesse={} a {}% de significancia".format(referencia,100*significancia))
            print('A hipótese nula não deve ser rejeitada!')
            print("{:.3f}".format(estatistica+1))
        else:
            print("Interesse {} {} a {}% de significancia".format(tipo_teste,referencia,100*significancia))
            print('A hipótese nula deve ser rejeitada!')
            print("{:.3f}".format(estatistica-1))
        exit()


def estatistica_Q(matriz):
    def E(linha,coluna,s):
        s1=0
        s2=0
        for k in range(len(matriz[linha])):
            s1+=matriz[linha][k]
        for k in range(len(matriz)):
            s2+=matriz[k][coluna]
        print("E({},{})={}".format(linha,coluna,s1*s2/s))
        return(s1*s2/s)

    s=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            s+=matriz[i][j]
    
    estatistica=0
    opa=False
    if len(matriz)==2 and len(matriz[0])==2:

        if s>40:
            for i in range(len(matriz)):
                if opa:
                    break
                for j in range(len(matriz[i])):
                    e=E(i,j,s)
                    if e<5:
                        opa=True
                        break      
        else:
            opa=True

    if opa:
        estatistica=0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                e=E(i,j,s)
                estatistica+=(abs(matriz[i][j]-e)-0.5)**2/e
        print("A estatistica corrigida foi utilizada")
    else:
        estatistica=0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                e=E(i,j,s)
                estatistica+=(matriz[i][j]-e)**2/e
        print("A estatistica não corrigida foi utilizada")

    return estatistica



#print(estatistica_Q([[12,5],[4,17]]),invSimpson(0.0001,0.001,4,1-confianca,Chi_quadrado,True,1))
carac1=analisar_sequencia(receber_sequencia())
exit()
carac2=analisar_sequencia(receber_sequencia())
#carac1={"Média Aritmética":1.67,"Desvio Padrão":1.2,"Tamanho":16,'dpt':16.5/50}
#carac2={"Média Aritmética":6.47,"Desvio Padrão":1.8,"Tamanho":16,'dpt':118.17/15}
#print(lista)

#print(estatistica_Q([[65,41],[110,96]]))



print("Digite a significancia")
significancia=float(input(''))
precisao=5

v=(carac1["Tamanho"]-1)*(carac2["Tamanho"]-1)*(carac1['dpt']+carac2['dpt'])**2/((carac2["Tamanho"]-1)*carac1['dpt']**2+(carac1['Tamanho']-1)*carac2['dpt']**2)
v=round(v)
par=[v]
estatistica=math.sqrt(carac1['Tamanho']*carac2['Tamanho'])*(carac1['Média Aritmética']-carac2['Média Aritmética'])/math.sqrt(carac2['Tamanho']*carac1['Desvio Padrão']**2+carac1['Tamanho']*carac2['Desvio Padrão']**2)
#(dm,desvios padroes desconhecidos e diferentes)

#estatistica=math.sqrt(carac1['Tamanho'])*carac1['Média Aritmética']/carac1['Desvio Padrão']
#par=
#(m pareada, desvios padroes desconhecidos)

#estatistica=math.sqrt(carac1['Tamanho']*carac2['Tamanho'])*(carac1['Média Aritmética']-carac2['Média Aritmética'])/math.sqrt(carac2['Tamanho']+carac1['Tamanho'])/(math.sqrt(((carac1["Tamanho"]-1)*carac1['Desvio Padrão']**2+(carac2["Tamanho"]-1)*carac2['Desvio Padrão']**2)/(carac1['Tamanho']+carac2['Tamanho']-2)))
#par=(carac1['Tamanho']+carac2['Tamanho']-2)
#dm, desvios padroes desconhecidos e iguais

#referencia=900
#estatistica=(carac1['Tamanho']-1)*carac1['Desvio Padrão']**2/referencia
#par=carac1['Tamanho']-1
#teste de variancia

#estatistica=carac1['Desvio Padrão']**2/carac2['Desvio Padrão']**2
#par=carac1['Tamanho']-1,carac2['Tamanho']-1
#comparacao de variancias


#referencia=0.15
#p=0.25
#carac1={'Tamanho':150}
#carac2={'Tamanho':200}
#estatistica=math.sqrt(carac1['Tamanho'])*(p-referencia)/math.sqrt(referencia*(1-referencia))
#par=0,1
#proporcao

#p1=71/150
#p2=110/200
#pg=(carac1['Tamanho']*p1+carac2['Tamanho']*p2)/(carac1['Tamanho']+carac2['Tamanho'])
#estatistica=math.sqrt(carac1['Tamanho']*carac2['Tamanho'])*(p1-p2)/math.sqrt((carac2['Tamanho']+carac1['Tamanho'])*(pg)*(1-pg))
#par=0,1
#comparacao de proporcoes


zpar=[1-significancia/2]

z=invSimpson(0,0.001,precisao,zpar,tStudent,True,*par)
z=[i[0] for i in z]
print("t({}),zpar={}, estatistica={},z={}".format(par,zpar,estatistica,z))





def talvez_seja_usada(tStudent, invSimpson, regiao_nao_critica, significancia, precisao):
    funcao=tStudent
           
    referencia=input("Digite a referencia do teste:")

    if tipo_teste=='<':
        zpar=significancia
    elif tipo_teste=='>':
        zpar=1-significancia
    else:
        zpar1=significancia/2
        zpar2=1-significancia/2
        print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,v,zpar1))
        z1=input('')
            
        if z1=='n':
            z1=invSimpson(-4,0,precisao,zpar1,funcao,True,v)
            z2=invSimpson(-4,0,precisao,zpar2,funcao,True,v)
        else:
            z1=float(z1)
            z2=float(input(''))
        regiao_nao_critica(tipo_teste,z1,z2,estatistica,referencia,significancia)
            
    print("Digite o valor de z~{}({}) para z({}), ou n caso queira que o computador estime esse valor".format(funcao.__name__,v,zpar1))
    z=input('')
    if z=='n':
        z=invSimpson(-4,0,precisao,zpar,funcao,True,v)
    else:
        z=float(z)
    regiao_nao_critica(tipo_teste,z,0,estatistica,referencia,significancia)

#talvez_seja_usada(tStudent, invSimpson, regiao_nao_critica, significancia, precisao)


def regiao_nao_critica(tipo_teste,z1,z2,estatistica,referencia,significancia):
        #Se a estatística estiver dentro desse intervalo, não rejeite a hipótese nula
        #z2 é igual a 0 no teste lateral a esquerda e lateral a direita
        if tipo_teste=='<':
            rejeitar=estatistica<z1
        elif tipo_teste=='>':
            rejeitar=estatistica>z1
        else:
            rejeitar=z1<estatistica<z2

        if not rejeitar:
            print("Interesse={} a {}% de significancia".format(referencia,100*significancia))
            print('A hipótese nula não deve ser rejeitada!')
            print("{:.3f}".format(estatistica+1))
        else:
            print("Interesse {} {} a {}% de significancia".format(tipo_teste,referencia,100*significancia))
            print('A hipótese nula deve ser rejeitada!')
            print("{:.3f}".format(estatistica-1))
        exit()


print("Deseja um intervalo de confiança para (m)édia, (v)ariancia, (p)roporção ou (n)ão?")
print("Digite d na frente caso queira a diferença entre duas coisas")
entrada=input("")

if entrada=='n':
    exit('')
else:
    print("Qual é a confiança desejada para o intervalo?")
    confianca=float(input(''))

    if confianca>1:
        confianca=confianca/100
    confianca=1-confianca

    print("Quantas casas decimais de precisao?")
    precisao=int(input(''))

if entrada=='m':
    print("Digite o desvio padrao populacional, ou n se não conhecê-lo")
    
    desviopp=input('')
    
    if desviopp=='n':
        l=receber_sequencia()
        carac=analisar_sequencia(l)

        #tcrit=math.sqrt(carac["Tamanho"])*(carac["Média Aritmética"]-21)/carac["Desvio Padrão"]

        zpar=1-confianca/2
        #zpar=0.05
        z,k=invSimpson(-63,0.005,precisao,zpar,tStudent,True,carac['Tamanho']-1)
        
        #if tcrit<z:
        #    print("Hipótese nula deve ser rejeitada a alfa={}".format(zpar))
        #else:
        #    print("Hipótese nula não deve ser rejeitada a alfa={}".format(zpar))

        #print(tcrit)

        #exit()


        dpzsqrt=round(carac['Desvio Padrão']*z/math.sqrt(carac['Tamanho']),precisao)
        print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),carac['Média Aritmética']-dpzsqrt,carac['Média Aritmética']+dpzsqrt))
        print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

        exit()
    else:
        desviopp=float(desviopp)
        
        zpar=1-confianca/2 
        
        l=receber_sequencia()
        carac=analisar_sequencia(l)

        zpar=1-confianca/2
        print("objetivo={}".format(zpar))
        z=inv(zpar,precisao,Normal,0,1,False)
        dpzsqrt=round(desviopp*z/math.sqrt(carac['Tamanho']),precisao)

        print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),carac['Média Aritmética']-dpzsqrt,carac['Média Aritmética']+dpzsqrt))
        print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

        exit()

elif entrada=='dm':
    print("Digite os desvios padrões, ou n se não conhecê-los")
    desviopp=input('')
    if desviopp=='n':
        print('Eles são iguais?')
        desviopp=input('')
        if desviopp=='s':

            carac1=analisar_sequencia(receber_sequencia())
            carac2=analisar_sequencia(receber_sequencia())

            desviopp=round(math.sqrt(((carac1["Tamanho"]-1)*carac1['Desvio Padrão']**2+(carac2["Tamanho"]-1)*carac2['Desvio Padrão']**2)/(carac1['Tamanho']+carac2['Tamanho']-2)),precisao)

            tcrit=round(math.sqrt(carac1['Tamanho']*carac2["Tamanho"])*(carac1["Média Aritmética"]-carac2["Média Aritmética"])/(desviopp*math.sqrt(carac1["Tamanho"]+carac2["Tamanho"])),precisao)




            ep=desviopp*math.sqrt(1/carac1['Tamanho']+1/carac2['Tamanho'])
            #zpar=1-confianca/2
            zpar=1-0.01/2
            print("objetivo={}".format(zpar))

            while True:
                if round(zpar,precisao)<zpar:
                    precisao+=1
                else:
                    break

            z=round(invSimpson(-63,0.005,precisao+math.floor(math.log10(ep)),zpar,tStudent,True,carac1['Tamanho']+carac2['Tamanho']-2)[0],precisao)
            
            if abs(tcrit)>z:
                print("Hipótese nula deve ser rejeitada a alfa={}".format(zpar))
            else:
                print("Hipótese nula não deve ser rejeitada a alfa={}".format(zpar))

            print(tcrit)

            exit()
            
            
            
            
            dpzsqrt=round(ep*z,precisao)
            difmedia=carac1['Média Aritmética']-carac2['Média Aritmética']
            print("Intervalo: {} +/- {}*{}".format(round(difmedia,precisao),z,round(ep,precisao)))
            print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(difmedia-dpzsqrt,precisao),round(difmedia+dpzsqrt,precisao)))
            print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

            exit()
        else:

            carac1=analisar_sequencia(receber_sequencia())
            carac2=analisar_sequencia(receber_sequencia())

            ep=math.sqrt(carac1["Desvio Padrão"]**2/carac1["Tamanho"]+carac2["Desvio Padrão"]**2/carac2["Tamanho"])
            v=(carac1["Tamanho"]-1)*(carac2["Tamanho"]-1)*ep**4/((carac2["Tamanho"]-1)*carac1['Desvio Padrão']**4/carac1['Tamanho']**2+(carac1['Tamanho']-1)*carac2['Desvio Padrão']**4/carac2['Tamanho']**2)
            v=round(v)
            

            zpar=1-confianca/2
            print("objetivo={}".format(zpar))

            while True:
                if round(zpar,precisao)<zpar:
                    precisao+=1
                else:
                    break


            z=round(invSimpson(-63,0.005,precisao+math.floor(math.log10(ep)),zpar,tStudent,False,v),precisao)
            dpzsqrt=round(ep*z,precisao)
            difmedia=carac1['Média Aritmética']-carac2['Média Aritmética']
            print("Intervalo: {} +/- {}*{}".format(round(difmedia,precisao),z,round(ep,precisao)))
            print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(difmedia-dpzsqrt,precisao),round(difmedia+dpzsqrt,precisao)))
            print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

            exit()

    else:
        desviopp=desviopp.split(' ')
        desviopp1=float(desviopp[0])
        desviopp2=float(desviopp[1])

        carac1=analisar_sequencia(receber_sequencia())
        carac2=analisar_sequencia(receber_sequencia())

        ep=math.sqrt(desviopp1**2/carac1['Tamanho']+desviopp2**2/carac2['Tamanho'])
        zpar=1-confianca/2
        print("objetivo={}".format(zpar))

        while True:
            if round(zpar,precisao)<zpar:
                precisao+=1
            else:
                break

        z=round(invSimpson(-4,0.0001,precisao+math.floor(math.log10(ep)),zpar,Normal,True,0,1),precisao)
        dpzsqrt=round(ep*z,precisao)
        difmedia=carac1['Média Aritmética']-carac2['Média Aritmética']
        print("Intervalo: {} +/- {}*{}".format(round(difmedia,precisao),z,round(ep,precisao)))
        print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(difmedia-dpzsqrt,precisao),round(difmedia+dpzsqrt,precisao)))
        print("Esse intervalo tem amplitude {}".format(2*dpzsqrt))

        exit()

elif entrada=='v':

    l=receber_sequencia()
    carac=analisar_sequencia(l)
    
    zpar1=1-confianca/2
    zpar2=confianca/2
    
    z1=invSimpson(0,0.0001,precisao,zpar1,Chi_quadrado,False,carac['Tamanho']-1)
    z2=invSimpson(0,0.0001,precisao,zpar2,Chi_quadrado,False,carac['Tamanho']-1)

    linf=round((carac['Tamanho']-1)*carac['Desvio Padrão']**2/z1,precisao)
    lsup=round((carac['Tamanho']-1)*carac['Desvio Padrão']**2/z2,precisao)

    print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),linf,lsup))
    print("Esse intervalo tem amplitude {}".format(lsup-linf))

    exit()

elif entrada=='dv':
    carac1=analisar_sequencia(receber_sequencia())
    carac2=analisar_sequencia(receber_sequencia())

    #carac1={'Tamanho':20,'Desvio Padrão':1.5}
    #carac2={'Tamanho':14,'Desvio Padrão':2.3}


    razao=round(carac1['Desvio Padrão']**2/carac2['Desvio Padrão']**2,precisao)      
    zpar1=1-confianca/2
    zpar2=confianca/2

    print(zpar1,zpar2,carac1['Tamanho']-1,carac2['Tamanho']-1)


    z1=round(invSimpson(0.00001,0,precisao,zpar1,F,True,carac1["Tamanho"]-1,carac2['Tamanho']-1)[0][0],precisao)
    z2=round(invSimpson(0.00001,0,precisao,zpar2,F,True,carac1["Tamanho"]-1,carac2['Tamanho']-1)[0][0],precisao)
    print(z1,z2,razao)
    
    print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),round(razao/z1,precisao),round(razao/z2,precisao)))
    print("Esse intervalo tem amplitude {}".format(razao*(1/z1-1/z2)))
    print("E ponto médio {}".format(round((razao/z1+razao/z2)/2,precisao)))
    exit()

elif entrada=='p':

    n=int(input('Digite quantos eventos foram testados\n'))
    p=int(input('Digite quantos eventos foram bem-sucedidos\n'))
    
    p=p/n
    zpar=1-confianca/2

    
    z,k=invSimpson(-4,0.0001,precisao,zpar,Normal,True,0,1)
    ep=math.sqrt(p*(1-p)/n)
    print(z,ep)
    linf=round(p-z*ep,precisao)
    lsup=round(p+z*ep,precisao)

    print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),linf,lsup))
    print("Esse intervalo tem amplitude {}".format(lsup-linf))

    exit()

elif entrada=='dp':
    n1=int(input('Digite quantos eventos foram testados\n'))
    p1=int(input('Digite quantos eventos foram bem-sucedidos\n'))

    n2=int(input('Digite quantos eventos foram testados\n'))
    p2=int(input('Digite quantos eventos foram bem-sucedidos\n'))
    
    p1=p1/n1
    p2=p2/n2
    zpar=1-confianca/2

    
    z,k=invSimpson(-4,0.0001,precisao,zpar,Normal,True,0,1)
    ep=math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2)
    print(z,ep)
    linf=round(p1-p2-z*ep,precisao)
    lsup=round(p1-p2+z*ep,precisao)

    print("Posso afirmar com {:.0f}% de certeza que a média dessa população está no intervalo [{},{}]".format(100*(1-confianca),linf,lsup))
    print("Esse intervalo tem amplitude {}".format(lsup-linf))

    exit()