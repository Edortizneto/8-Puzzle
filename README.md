# 8-Puzzle
Implementação do 8 Puzzle utilizando o algoritmo do busca A*.
<br/><br/>
           Para resolver o 8 Puzzle, foi preciso determinar como os estados gerados nessa busca seriam feitos.  
Logo, cada estado representa a situação atual do "tabuleiro" e a transiçao de cada estado seria feita  
através dos respectivos sucessores, que foi escolhido como as diferentes posições que a parte vazia  
(no código, 0) assumiria. Portanto, como a parte vazia se move apenas uma posição por vez, a nova posição  
vai ser ou para cima ou para baixo, ou da esquerda para direita e vice-versa, contando com as restrições que  
esse vazio nunca pode sair do "tabuleiro".
<br/>
            Como o algoritmo A* busca pelo sucessor com a menor estimativa de custo (f(n)), foi preciso adotar  
como heurística (h(n)) a distância de Manhattan misturada com a sequência de Nilsson, já que o custo real (g(n)) é  
1 para cada sucessor gerado. Assim sendo, nosso algoritmo sempre buscaria o estado com o menor somatório de  
distâncias de Manhattan e com pré-disposição ao estado final de Caracol (sequência de Nilsson) melhorando a  
performance do A* e o possibilitando de resolver as possíveis soluções do 8 Puzzle, tanto as difíceis quanto  
as mais fáceis. 
<br/><br/>
# Testes
![testes](https://github.com/Edortizneto/8-Puzzle/blob/main/imgs/testes8Puzzle.png?raw=true)
<br/><br/>
# Cliente
<br/><br/>
## Cliente Shuffle
### Configuração Inválida
![shuffle_errado](https://github.com/Edortizneto/8-Puzzle/blob/main/imgs/geradoerrado.png?raw=true)
<br/><br/>
### Configuração Válida
![shuffle_certo](https://github.com/Edortizneto/8-Puzzle/blob/main/imgs/geradocerto.png?raw=true)
<br/><br/>
## Cliente escolhe estado pré-determinado
![estado6](https://github.com/Edortizneto/8-Puzzle/blob/main/imgs/estado6.png?raw=true)
<br/><br/>