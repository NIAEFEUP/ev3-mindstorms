#EV3 Mindstorm blog

Para correrem na vossa consola, basta usar o seguinte comando 'jekyll server --watch --baseurl "" '. Por vezes, dependendo do ficheiro, o servidor pode nao reparar que ocorreu uma mudança e por isso é necessário fechar o servidor (CTRL + C), depois basta voltar a usar o comando para iniciar o servidor. Para ver as mudanças feitas, devem ir a localhost:4000.

Este é o link do blog : https://niaefeup.github.io/ev3-mindstorms/


Para meter uma imagem num post é da seguinte maneira :'![My helpful screenshot]({{ site.url }}/assets/screenshot.jpg)', penso que podem
por tambem como se fosse hmtl.


Para adicionarem um video a um post basta introduzir o seguinte :

```
<video width="100%" height="100%" controls>
  <source src="/../video/teste.mp4" type="video/mp4">
</video>
```

Quando estiverem a escrever um post podem (devem) escrever em markdown, nao precisam de por tags de html nem nada, apenas para o video.
