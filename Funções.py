import PySimpleGUI as sg

def janelaInicial():
    
    sg.theme('DefaultNoMoreNagging')
    sg.set_options(font = ('Roboto Light', 10), text_color='white')

    Text_size = (25, 1)
    Combox_size = (15, 0)
    COLOR = 'midnight blue'

    coluna_esq = [
        [sg.Text('Área Danificada', size=Text_size,background_color=COLOR), sg.Combo(['Baixas Áreas', 'Espalhado', 'Áreas Superiores', 'Campo Inteiro'], key='areaDamaged',
                  enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Lesão de Cancro', size=Text_size,background_color=COLOR), sg.Combo(['Sem Resposta', 'Marrom', 'dk-marrom-blk', 'Bronzeado'], key='canker-lesion',
                  enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Histórico de Cultura', size=Text_size,background_color=COLOR), sg.Combo(
            ['Diferente do primeiro ano', 'Mesmo do primeiro ano', 'Mesmo do ultimo ano', 'Mesmo do ultimo dois anos'],
            key='crop-hist', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Data', size=Text_size,background_color=COLOR),sg.Combo(
            ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro'], key='date', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Decadência Externa', size=Text_size,background_color=COLOR),sg.Combo(['Ausente', 'Firme e Seco'], key='external decay', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Manchas de Frutas', size=Text_size,background_color=COLOR),sg.Combo(['Não tem resposta', 'Ausente', 'Marrom com manchas pretas', 'Colorido'], key='manchasdeFrutas', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Corpos de Frutificação', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Presente'], key='corposdeFrutificacao', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Vagens de Frutas', size=Text_size,background_color=COLOR), sg.Combo(['Não tem resposta', 'pouco presente', 'Normal', 'Doente'], key='vagensdeFrutas', enable_events=True,readonly=True, size = Combox_size)],

        [sg.Text('Germinação', size=Text_size,background_color=COLOR), sg.Combo(['abaixo de 80%', '80-89 %', '90-100%'], key='germinacao', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Saudação', size=Text_size,background_color=COLOR), sg.Combo(['Não', 'Sim'], key='saudacao', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Descoloração', size=Text_size,background_color=COLOR), sg.Combo(['Nenhum', 'Preto'], key='descoloracao', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Folha-Malf', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Presente'], key='folhaMalf', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Folha-Suave', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Baixo surf', 'Alto surf'], key='folhaSuave', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Folhagem', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Presente'], key='folhagem', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Manchas-Halo', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Sem halo amarelo', 'halo amarelo'], key='manchasHalo', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Tamanho da Mancha', size=Text_size,background_color=COLOR), sg.Combo(['Nenhuma das alternativas', 'Abaixo de 1/8', 'Acima de 1/8'], key='tamanhodaMancha',enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Manchas de Folhas-Marg', size=Text_size,background_color=COLOR), sg.Combo(['Nenhuma das alternativas', 'no-w-s-marg', 'w-s-marg'], key='manchasdeFolhasMarg',enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Folhas', size=Text_size,background_color=COLOR), sg.Combo(['Anormal', 'Normal'], key='folhas', enable_events=True, readonly=True, size = Combox_size)]

    ]
    
    coluna_dir = [
        [sg.Text('Alojamento', size=Text_size,background_color=COLOR), sg.Combo(['Não', 'Sim'], key='alojamento', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Crescimento de Mofo', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Presente'], key='crescimentodeMofo', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Micélio', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Presente'], key='micelio', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Crescimento da Planta', size=Text_size,background_color=COLOR), sg.Combo(['Anormal', 'Normal'], key='crescimentodaPlanta', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Estande de Plantas', size=Text_size,background_color=COLOR), sg.Combo(['Abaixo do normal', 'Normal'], key='estandedePlantas', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Precipício', size=Text_size,background_color=COLOR),sg.Combo(['Abaixo do normal', 'Normal', 'Acima do Normal'], key='precipício', enable_events=True,readonly=True, size = Combox_size)],

        [sg.Text('Raízes', size=Text_size,background_color=COLOR),sg.Combo(['Cistos de Vesícula', 'Normal', 'Apodrecido'], key='raiz', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Sclerotia', size=Text_size,background_color=COLOR),sg.Combo(['Ausente', 'Presente'], key='sclerotia', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Semente', size=Text_size,background_color=COLOR),sg.Combo(['Anormal', 'Normal'], key='semente', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Descoloração da Semente', size=Text_size,background_color=COLOR),sg.Combo(['Ausente ', 'Presente'], key='descoloracaodaSemente', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Tamanho da Semente', size=Text_size,background_color=COLOR),sg.Combo(['Abaixo do normal', 'Normal'], key='tamanhodaSemente', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Semente-Tmt', size=Text_size,background_color=COLOR),sg.Combo(['Nenhum', 'Fungicida', 'Outros'], key='sementeTmt', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Gravidade', size=Text_size,background_color=COLOR), sg.Combo(['Menor', 'Grave', 'Severo'], key='gravidade', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Murchando', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Presente'], key='murchando', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Tronco', size=Text_size,background_color=COLOR), sg.Combo(['Anormal', 'Normal'], key='tronco', enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Cancros do Caule', size=Text_size,background_color=COLOR), sg.Combo(['Ausente', 'Abaixo do Solo', 'Acima do Solo', 'Acima do Segundo'], key='cancrosdoCaule',enable_events=True, readonly=True, size = Combox_size)],

        [sg.Text('Temperatura', size=Text_size,background_color=COLOR),sg.Combo(['Abaixo do normal', 'Normal', 'Acima do Normal'], key='temperatura',enable_events=True, readonly=True, size = Combox_size)]
    ]
   
    # Janela principal 

    layout = [
        [sg.Text('Novo caso problema: ', background_color='white', text_color='black')],
        [sg.Column(coluna_esq, vertical_alignment='top'), sg.Column(coluna_dir, vertical_alignment='top')],
        [sg.Column([  # Coluna da esquerda
            [sg.Text('Limite CNF', background_color='white', text_color='black'),
            sg.Input('0', key='porcentagem', size=(3, 1), text_color='black'),
            sg.Text('%', background_color='white', text_color='black')]
            ], element_justification='left', expand_x=True, background_color='white'),
     
        sg.Column([  # Coluna da direita
            [sg.Button('Continuar', key='botao'), sg.Button('Exit', key='-EXIT-')]
         ], element_justification='right', expand_x=True, background_color='white')]
    ]

    
    return sg.Window('Sistema RBC', layout=layout, finalize=True, background_color='white')
    

def janelaSecundaria(lista, lista2, lista3, cursor):
    listadoencas = []
    listaP1 = []
    listaP = []
    listaPP = []
    listaP1.append('area-damaged')
    listaP1.append('canker-lesion')
    listaP1.append('crop-hist')
    listaP1.append('date')
    listaP1.append('external decay')
    listaP1.append('fruit spots')
    listaP1.append('fruiting-bodies')
    listaP1.append('fruit-pods')
    listaP1.append('germination')
    listaP1.append('hail')
    listaP1.append('int-discolor')
    listaP1.append('leaf-malf')
    listaP1.append('leaf-mild')
    listaP1.append('leaf-shread')
    listaP1.append('leafspots-halo')
    listaP1.append('leafspot-size')
    listaP1.append('leafspots-marg')
    listaP1.append('leaves')
    listaP1.append('lodging')
    listaP1.append('mold-growth')
    listaP1.append('mycelium')
    listaP1.append('plant-growth')
    listaP1.append('plant-stand')
    listaP1.append('precip')
    listaP1.append('roots')
    listaP1.append('sclerotia')
    listaP1.append('seed')
    listaP1.append('seed-discolor')
    listaP1.append('seed-size')
    listaP1.append('seed-tmt')
    listaP1.append('severity')
    listaP1.append('shriveling')
    listaP1.append('stem')
    listaP1.append('stem-cankers')
    listaP1.append('temp')
    
    for n in range(len(listaP1)):
        
        listaP2 = [listaP1[n], lista[n]]
        listaP.append(listaP2)

    coluna1 = [
        [sg.Table(values=listaP, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'], auto_size_columns=False, expand_x=True, expand_y=True, key='-TB-', col_widths=[15,15])]
    ]

    for casos in lista2: # ListaDoencas
        cursor.execute("SELECT DescDoenca FROM bancoprincipal WHERE Caso = ?", (casos[0],))
        resultado = cursor.fetchall()
        listadoencas.append(resultado[0])
    for n in range(len(lista2)):
        listaP3 = [lista2[n][0], listadoencas[n], str(lista3[n])+'%']
        listaPP.append(listaP3)
    coluna3 = [
        [sg.Table(values=listaPP, select_mode=sg.SELECT_MODE_BROWSE, headings=[' Caso ', 'Doenca', 'Porcentagem'], auto_size_columns=False, expand_x=True, expand_y=True, key='-TB2-', enable_events=True)]
    ]

    layout = [

        [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna3)]

    ]
    return sg.Window('Resultados da busca', layout=layout, finalize=True), listaPP, listaP

def janelaFinal(listaP, casoSel, cursor):
    lista = []
    coluna1 = [
        [sg.Table(values=listaP, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'],
                  auto_size_columns=False, expand_x=True, expand_y=True,key='-TB3-', col_widths=[15,15])]
    ]
    cursor.execute("SELECT * FROM bancoprincipal WHERE Caso = ?", (casoSel,))
    resultado = cursor.fetchall()
    for n in range(len(listaP)):
        listaprov = [listaP[n][0], resultado[0][3+n]]
        lista.append(listaprov)
    coluna2 = [
        [sg.Table(values=lista, select_mode=sg.SELECT_MODE_BROWSE, headings=['  Caso  ', 'Problema'],
                  auto_size_columns=False, expand_x=True, expand_y=True, key='-TB4-', col_widths=[15,15])]
    ]
    layout = [
        [sg.Text('Solução:' + resultado[0][2], text_color='black')],
        [sg.Column(coluna1), sg.VerticalSeparator(), sg.Column(coluna2)]
    ]
    return sg.Window('Caracteristicas do caso', layout=layout, finalize=True)