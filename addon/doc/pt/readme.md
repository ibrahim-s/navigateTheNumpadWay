# Emular O bloco numérico #

* Autor: Ibrahim Hamadeh
* Descarregar [versão de desenvolvimento 0.6][1]
* Compatibilidade com o NVDA: 2019.3 e posterior

## Introdução

Este addon foi feito em resposta a um pedido dum utilizador, que não tem  bloco numérico no seu teclado;
 permitindo-lhe, assim, beneficiar da funcionalidade de navegação através das teclas do bloco numérico.  

Por isso, penso que este extra será principalmente do interesse dos utilizadores que não têm um teclado numérico no seu computador.
 Pode escolher um dos formulários ou um conjunto de teclas disponíveis no teclado principal, para que emulem as teclas do teclado numérico e os respetivos comandos relacionados, no que diz respeito à revisão ou à navegação por objetos.

## Uso

Depois de instalar o addon, terá três modos

Modo normal, Numpad e nnúmeros, o modo números é ignorado por defeito, pelo que temos principalmente dois modos normal e numpad .

Pode alternar entre esses modos através do atalho NVDA+shift+f4. E, como sempre, pode modificá-lo indo para o menu do NVDA/preferências/definir comandos/emular o modo Numpad.

Os formulários disponíveis que podem ser emulados no modo numpad são

* form1:  
e r t  
d f g  
c v b  
* form2:  
y u i  
h j k  
n m ,  
* form3:  
7 8 9  
u i o  
j k l

Cada um desses formulários irá emular

numpad7 numpad8 numpad9  
numpad4 numpad5 numpad6  
numpad1 numpad2 numpad3  

Emulando a sua revisão ou navegação de objeto, usado sozinho ou em conjunto com as teclas shift ou NVDA.

## Configurações Do extra ##

Para aceder às definições do addon, aceda a: menu/Preferências NVDA,  
pressione enter e depois "e" para ir ao Painel emular o modo Numpad.

* Na caixa de combinação, Escolha o formulário para emular para o modo numpad: a partir daqui, pode escolher o formulário que gostaria de emular para o modo numpad; Form1 encontra-se definido por padrão.
* Em seguida,  ficará num controlo de edição múltipla de texto:  poderá usar as setas para cima e para baixo para navegar nas teclas do formulário.
* Caixa de verificação do modo Skipt numbers: está desmarcada ou ignorada por predefinição. O modo Numbers foi solicitado pelo utilizador que solicitou o addon, e eu queria mantê-lo, mesmo que pareça secundário e não seja utilizado pela maioria dos utilizadores.
* Rejeitar o numpadMode  pressionando escape caixa de seleção: encontra-se marcada por padrão, para que possa retornar ao modo normal, usando o comando moral do extra ou a tecla escape.

Nota Final:  
Nesta tradução, foram usados, indiscriminadamente, os termos "numpad" e "bloco numérico".

### Contribuidores ###

* umut korkmaz, obrigado por apoiar a tradução turca do addon.
* Ângelo Abrantes e Rui Fontes: tradução portuguesa.

[1]: https://github.com/ibrahim-s/emulateNumpadMode/releases/download/0.6-dev/emulateNumpadMode-0.6-dev.nvda-addon