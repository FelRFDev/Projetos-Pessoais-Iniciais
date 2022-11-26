# **Screenshots**


<div align="center">
<img src="https://user-images.githubusercontent.com/89205473/161753471-90fb66a0-640e-47a0-9f2a-c5ffdf2be600.jpg" width="400px" />
<img src="https://user-images.githubusercontent.com/89205473/161753479-6b7d6991-cacf-402b-bb8d-9aa0053b9203.jpg" width="400px" />
<img src="https://user-images.githubusercontent.com/89205473/161753979-3c50754d-a584-4e46-8c1e-e6289018514a.jpg" width="400px" />
<img src="https://user-images.githubusercontent.com/89205473/161753981-e36f2293-49ef-438b-a043-308332de2d70.jpg" width="400px" />
<img src="https://user-images.githubusercontent.com/89205473/161753984-611a8c46-c929-4bb9-9953-b79fee5fddec.jpg" width="400px" />
</div>



# **Sobre o MY PASS**


<div align="left">
  Este projeto é uma versão criada e melhorada por mim, com base em um exercício encontrado no curso 100 days of code! A versão do exercício é bem simples, e conta somente com uma janela onde o usuário encontra alguns campos para preenchimento, e um botão para salvar as informações em um arquivo  de extensão .TXT. Com base nos conhecimentos adquiridos ao longo do curso e dos meus estudos, além de algumas pesquisas pela internet, procurei utilizar algumas ferramentas a mais para implementar diversas ideias que tive, afim de tornar o programa do exercício melhor e mais completo rendendo posteriormente muito aprendizado. Abaixo, você confere todas as novas funcionalidades e ferramentas as quais implementei. 
</div>

# **My Pass - Funcionalidades**

* - Sistema de Cadastro e Login para usuários:

Para usar o My Pass o usuário deverá primeiramente cadastrar um usuário e uma senha. Assim que este procedimento for feito, o programa automaticamente cria uma pasta com o nome do usuário, dentro de uma pasta principal. Esta pasta secundária com o nome do usuário contém os arquivos os quais servirão como "banco de dados", guardando informações como usuário e senha cadastrada para uso do programa e informações de Login cadastradas no programa, EX: (Website, Usuário e Senha). Esta funcionalidade, permite que vários usuários possam utilizar o programa tendo as suas informações salvas e organizadas e pastas diferentes, previnindo o acesso de outros usuários as informações cadastradas.

* - Sistema para cadastro, gerenciamento e visualização de informações:

A janela principal conta com botões para:

- Cadastrar senhas.
- Visualizar senhas. 
- Gerenciar senhas.

Em cadastrar senhas, o usuário deverá preencher 3 campos: O nome do Website ao qual estará cadastrando os seus dados para login, o usuário e a senha. Caso o usuário seja um endereço de e-mail, existe um botão que permite ao usuário escolher um dos domínios presentes para auto_preenchimento do campo usuário. Ou seja, caso ele use um e-mail do gmail, basta digitar o início do endereço de email, clicar em escolher dominio, selecionar g-mail, e o programa automaticamente preencherá o restante do campo com @gmail.com. Além disso, a janela Cadastrar Senhas também possui um botão para gerar senhas complexas automaticamente. O usuário poderá escolher se deseja que o programa inclua letras maiúsculas, minúsculas, símbolos, e números. Para isso, basta selecionar as opções desejadas e após confirmar, será gerada uma senha automaticamente que será preenchida no campo senha, e também copiada para a área de transferência permitindo ao usuário colar onde quiser. Após preencher todos os campos, basta clicar em adicionar para que todas as informações fiquem salvas dentro do arquivo em sua pasta com o seu nome. 

Em visualizar senhas, o programa irá exibir todas as inforamções cadastradas de forma tabular através de uma tabela com barra de rolagem. Inicialmente por padrão, as senhas virão ocultadas sendo que basta clicar no botão exibir para que o usuário possa visualizar as senhas ocultas, e clicar no mesmo botão para ocultá-las novamente.

Em gerenciar senhas, o usuário poderá remover uma informação do seu cadastro. A janela mostra todos os dados cadastrados da mesma forma apresentada em visualizar senhas. Assim, basta digitar no campo situado na parte inferior da janela, qual website deseja ser removido dos cadastros e clicar em REMOVER para que a informação seja removida do banco de dados. 

Em Limpar Cadastro, o usuário poderá remover TODAS AS INFORMAÇÕES CADASTRADAS NO PROGRAMA DE UMA VEZ SÓ. Ou seja, o banco de dados irá esvaziar todo o conteúdo cadastrado previamente sendo que está opção não permite resgatar tudo o que foi apagado. Sendo assim, recomenda-se cautela.

Em criar um arquivo TXT, o programa irá criar AUTOMATICAMENTE, dentro da pasta com o nome do usuário, um arquivo de extensão .txt contendo todas as informações cadastradas no programa. Esta funcionalidade permite ao usuário, manter um arquivo de backup, um meio de salvar o usuário e senha do próprio programa, além de permitir que o usuário tenha em mãos o arquivo salvo em qualquer dispositivo, facilitando a consulta as informações quando precisar!



## Requisitos


<div align="left">
  Para utilizar o programa você deve criar um cadastro com usuário e senha. Esta medida visa organizar os dados cadastrados, além de fornecer segurança ao usuário. Por ser um projeto com finalidade de estudo e prática, foram implementadas somente estas medidas, por mais simples que sejam. Fique a vontade caso queira fazer uso do projeto para implementar novas ideias e/ou funcionalidades.
</div>

## Contato

Dúvidas, sugestões e etc:

E-mail: comunidadehawks@gmail.com
Linkedin: https://www.linkedin.com/in/felipe-rodrigues-fonseca-843b9421a/
