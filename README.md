Recentemente no meu trabalho precisei tratar um arquivo público da Febraban (disponível no site "Taxonomia Verde - Febraban") e optei por fazer isso utilizando python, na ocasião eu converti em csv para utilizar em um fluxo de dados que posteriormente iria para o SQL Server, aqui, optei por deixar em xlsx mesmo.

No Arquivo Original temos a coluna de Código CNAE (Código Nacional de Atividade Econômica) e suas respectivas classificações da Febraban. porém este arquivo esta cheio de linhas em branco, e também problemas de carácteres que iriam causar problemas no SQL Server.

### Código 

* primeiramente importamos a biblioteca pandas.
* localizamos arquivo original no mesmo diretório.
* print para visualizar dados, e também os tipos dos dados.
* criado um novo DataFrame para guardar os dados limpos.
* limpamos as linhas em branco.
* tiramos os "-" e "/" do código para ficar somente numérico (necessário para relacionar com outra tabela).
* tiramos os colchetes de uma das colunas de classificação.
* print novamente para visualizar novo DataFrame agora tratado.
* Carregando em novo arquivo xlsx.

### Tecnologias Usadas:
* Python com bibliotaca Pandas.

