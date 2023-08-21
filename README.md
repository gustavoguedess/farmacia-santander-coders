# Projeto Final Santander Coders - POO

## Descrição do Trabalho

Este projeto teve como objetivo implementar os conceitos de Programação Orientada a Objetos na construção de uma aplicação para uma Farmácia que vende produtos por meio de um e-commerce. Durante a realização deste projeto, foi possível aplicar uma série de princípios fundamentais da POO, incluindo:

- Abstração: Criamos classes que representam abstrações do mundo real, como Cliente, Medicamento, Venda, entre outras. Essas classes encapsulam comportamentos e propriedades específicas, tornando a estrutura do programa mais organizada e intuitiva.
- Encapsulamento: Através do encapsulamento, ocultamos os detalhes internos de cada classe, revelando somente a interface necessária para o uso externo. Isso promove a modularização e facilita futuras modificações sem impactar o restante do sistema.
- Herança: Pudemos explorar o conceito de herança ao criar subclasses, como Medicamente Quimioterápico, herdando características e comportamentos da classe Medicamento.
- Polimorfismo: Implementamos polimorfismo ao utilizar métodos e interfaces comuns para classes diferentes. Isso permitiu tratar objetos de maneira uniforme, independente de suas implementações específicas.
- Métodos de Acesso: Utilizamos métodos de acesso, como getters e setters, para controlar o acesso aos atributos das classes, mantendo a integridade dos dados.
- Tratamento de Exceções: Implementamos tratamento de exceções para lidar com situações imprevistas de forma controlada, melhorando a robustez do programa.
- Composição: Utilizamos a composição para construir objetos complexos através da combinação de objetos menores, como na formação de uma Venda contendo diversos Medicamentos.
- Organização e Modularidade: Ao dividir o sistema em classes distintas, seguindo princípios de responsabilidade única, conseguimos criar um sistema mais modular e fácil de manter.
- Reutilização de Código: Através do uso de herança e composição, conseguimos reutilizar código, evitando duplicações e tornando o desenvolvimento mais eficiente.
- Flexibilidade: A POO permitiu que o sistema fosse mais flexível, possibilitando futuras expansões e modificações com menor impacto nas partes já existentes.

## Funcionamento

O projeto apresenta 7 classes **Cliente**, **Farmacia**, **Laboratorio**, **Medicamento**, **MedicamentoFitoterapico**, **MedicamentoQuimioterapico** e **Venda**. Todas elas são integradas e executadas em **main.py**.

### Main

Para executar o código é necessário rodar o comando `python main.py`. Primeiramente é criado um objeto farmácia da Classe Farmacia, esse objeto capta todos os dados já gravados. 

Esses dados estão localizados no diretório `dados/`. Em seguida a função `main` é chamada, ela é responsável pela geração de um menu com 6 opções:

- Opção 01: responsável por chamar a função cadastrar_laboratorio() permite o cadastro de um novo laboratório
- Opção 02: responsável por chamar a função cadastrar_cliente() possibilita o cadastro de um novo cliente
- Opção 03: responsável por chamar a função cadastrar_medicamento() permite o cadastro de novos medicamentos
- Opção 04: responsável por chamar a função cadastrar_venda() que permite o registro de uma nova venda
- Opção 05: responsável por chamar a função clientes() para listar os nomes dos clientes em ordem alfabética
- Opção 06: responsável por chamar a função medicamentos() para listar medicamentos em ordem alfabética
- Opção 07: responsável por chamar a função mediamentos_quimioterapicos() para listar medicamentos Quimioterapicos em ordem alfabética
- Opção 08: responsável por chamar a função medicamentos_fitoterapicos() para listar medicamentos Fitoterapicos em ordem alfabética
- Opção 09: responsável por chamar a função listar_estatisticas() para listar as estatísticas das vendas do dia
- Opção 10: responsável por chamar a função listar_informacoes() lista todos os medicamentos, laboratórios e clientes
- Opção 11: responsável por encerrar o menu interativo (break)

### Laboratório

Caso a opção selecionada pelo menu central seja Cadastrar Laboratório (1). A função cadastrar_laboratorio é chamada.

Nela são gerados alguns inputs:

- 01: Digite o nome do laboratório
- 02: Digite o endereço do laboratório
- 03: Digite o telefone do laboratório
- 04: Digite a cidade do laboratório
- 05: Digite o estado do laboratório

Todos os inputs são adicionados na Classe Laboratório e são adicionados pela Classe Farmacia dentro do método add_laboratorio, na qual serão gravados dentro do diretório `dados\` após o encerramento do programa (salvar_dados).

#### Classe Laboratório

Dentro da Classe Laboratório alguns conceitos de POO foram utilizados. Setters e Getters foram criados para cada atributo.

### Cliente

Caso a opção selecionada pelo menu central seja Cadastrar Cliente (2). A função cadastrar_cliente é chamada.

Nela são gerados alguns inputs:

- 01: Digite o nome do cliente
- 02: Digite o sobrenome do cliente
- 03: Digite o CPF do cliente
- 04: Digite a data de nascimento do cliente

Todos os inputs são adicionados na Classe Cliente e são adicionados pela Classe Farmacia dentro do método add_cliente, na qual serão gravados dentro do diretório `dados\` após o encerramento do programa (salvar_dados).

#### Classe Cliente

Dentro da Classe Cliente alguns conceitos de POO foram utilizados. Setters e Getters foram criados para cada atributo.

### Medicamentos

Caso a opção selecionada pelo menu central seja Cadastrar Medicamento (3). A função cadastrar_medicamento é chamada.

Nela são gerados alguns inputs:

- 01: Digite o nome do medicamento
- 02: Digite o principal composto do medicamento
- 03: Digite o laboratório do medicamento
- 04: Digite a descrição do medicamento
- 05: Digite o preço do medicamento

Após o envio das informações é iniciado um `while` na qual é necessário digitar "F" para selecionar a opção de medicamentos fitoterápicos e "Q" para medicamentos quimioterápicos.

Caso seja selecionado "F" é criado um objeto de nome medicamento no objeto MedicamentoFitoterapico.

Já quando é selecionado "Q" é gerado um input com o questionamento "O medicamento é controlado (S/N)". Caso seja "S" o medicamento é controlado e "N" o medicamento não é controlado. Em seguida, é criado um objeto de nome medicamento no objeto MeicamentoQuimioterapico.

Todos os inputs são adicionados pela Classe Farmacia dentro do método add_cliente, na qual serão gravados dentro do diretório `dados\` após o encerramento do programa (salvar_dados).

#### Classe Medicamento

A ClasseMedicamento é responsável possui os atributos: nome, principal_composto, laboratorio, descricao, preco. Setters e Getters foram criados para cada atributo.

#### Classe MedicamentoFisioterapico

Está é uma Classe filha da Classe Medicamento. Na qual são persistidos os dados os mesmos dados de Medicamento, sem a adição de novos atributos ou métodos.

#### Classe MedicamentoQuimioterapico

Esta é uma Classe filha da Classe Medicamento. Possui o atributo 'controlado' que especifica a necessidade de receita para a efetivação da compra do medicamento. Assim como os demais atributos, para este também foram implementados Getter e Setter.

### Venda

Caso a opção escolhida pelo menu central seja Cadastrar Venda (4). A função cadastrar_venda é chamada.

Nela são gerados alguns inputs:

- 01: Digite o CPF do cliente (Esse dado é guardado em uma lista)

Iniciado um while:

- 02: Digite o ID do medicamento
- 03: Deseja adicionar mais um medicamento (S/N)

Caso a opção "Deseja adicionar mais um medicamento (S/N)" adicionada seja "N" o menu é parado (break).

Todos os inputs são adicionados na Classe Farmacia dentro do método vender. Dentro do método vender são persistidos o id_cliente (int) e id_medicamento (list). Todas as informações dos clientes e medicamentos são obtidas por meio do id_cliente e id_medicamento.

#### Classe Venda

Os dados são persistidos no objeto venda da Classe Venda. Dentro desta classe são adicionados os atributos: cliente, medicamentos, são calculados os valores dos produtos e seus descontos para pessoas com mais de 65 anos ou para valores maiores que 150.

A verificação do produto também é realizada dentro da Classe venda no método verificar_produto e possui_controlado.

### Listar Informações

Caso a opção escolhida pelo menu central seja Listar Informações (5). A função listar_informacoes é chamada.

A função listar_informacoes permite listar todos os dados existentes no diretório `dados/`.

### Finalização do Programa
Caso a opção escolhida pelo menu central seja Sair (6), o programa é encerrado (break).

Ao finalizar os dados são salvos dentro do objeto farmácia da Classe Farmacia dentro do método salvar_dados.

## Grupo

O grupo que desenvolveu esse projeto é composto pelos seguintes integrantes:

- Danilo Freitas
- Gustavo Guedes
- Luana Nunes