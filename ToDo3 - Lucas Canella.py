from os import system

notas = ['e5_t10_p8_s8','e10_t7_p7_s8','e8_t5_p4_s9','e2_t2_p2_s1', 'e10_t10_p8_s9']

while True:
    aprovados = []
    try:
        escolha = int(input('O que deseja?\n[1] Checar candidatos\n[2] Adicionar novo candidato \n[3] Verificar todos os candidatos\n[4] sair\nEscreva aqui: '))
    except:
        system("cls")
        print("por favor, selecione uma das opções.")
        continue   
    if escolha == 4: 
        break 
    elif escolha == 3:
        system("cls")
        for num, candidato in enumerate(notas, 1):
            print(f"candidato {num} - {candidato}")
        continue    
    elif escolha == 2:
        try:
            system("cls")
            e = int(input('Qual nota o(a) candidato(a) tirou na entrevista?'))
            t = int(input('Qual nota o(a) candidato(a) tirou no teste teórico?'))
            p = int(input('Qual nota o(a) candidato(a) tirou no teste prático?'))
            s = int(input('Qual nota o(a) candidato(a) tirou avaliação de soft skills?'))
        except:
            system("cls")
            print("Por favor, digite um valor válido!")
            continue
        notas.append(f"e{e}_t{t}_p{p}_s{s}")
        continue
    elif escolha == 1:
        pass
    else:
        print('Escolha inválida, por favor, escolha uma das seguintes opções!')
    try:
        e = int(input('Qual a nota mínima da entrevista?'))
        t = int(input('Qual a nota mínima do teste teórico?'))
        p = int(input('Qual a nota mínima do teste prático?'))
        s = int(input('Qual a nota mínima da avaliação de soft skills?'))
    except:
        system("cls")
        print("Por favor, digite um valor válido!")
        continue
    for nota in notas:
        candidato_e = int(nota[nota.find('e') + 1])
        candidato_t = int(nota[nota.find('t') + 1])
        candidato_p = int(nota[nota.find('p') + 1])
        candidato_s = int(nota[nota.find('s') + 1])
        if candidato_e == 1 and nota[nota.find('e') + 2] == "0":
            candidato_e = 10
        if candidato_t == 1 and nota[nota.find('t') + 2] == "0":
            candidato_t = 10
        if candidato_p == 1 and nota[nota.find('p') + 2] == "0":
            candidato_p = 10
        try:    
            if candidato_s == 1 and nota[nota.find('s') + 2] == "0":
                candidato_s = 10
        except:
            pass
        if candidato_e >= e and candidato_t >= t and candidato_p >= p and candidato_s >= s:
            aprovados.append(f"e{candidato_e}_t{candidato_t}_p{candidato_p}_s{candidato_s}")
    system("cls")
    print(f"Notas mínimas: \ne - {e}\nt - {t}\np - {p}\ns - {s}\n")   
    print("Notas dos candidatos aprovados:")        
    print('')
    for candidato in aprovados:
        print(f"candidato aprovado N°{notas.index(candidato) + 1} - {candidato}")