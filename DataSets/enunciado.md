---
title: Enunciado do TP1 - Análise de polaridade em PT
author: 
  - J.João
  - Filipe Cunha
date: Março 2024
---

# Análise de sentimento com sentilex PT

Pretende-se construir um módulo de __Sentiment Analysis__ para o Português
baseado em léxicos de sentimento.

Esses léxicos podem cobrir diversos aspectos:

- sentimento ligado à palavra (exemplo: besta → neg, valente → pos )
- sentimento ligado a termos multipalavra (deixa muito a desejar → neg)
- léxico ligado a __bosters__ (intensidade -- exemplo "muito" bom, )
- léxico ligado a __negadores__ (inversos -- exemplo: "não é" feliz; "nunca" venceu)

Para tal sugere-se que descarregue, e analise os recursos que conseguir
encontrar, incluindo:

- sentilex-pt
- LeIA
- etc

Construa uma ferramenta que calcule a polaridade de textos ou elementos textuais
permitindo:

1. procurar evidências positivas, negativas, negadores e intensidades;
2. anotá-las;
3. calcular (+, -, negadores, inteisidades, nº de palavras) e uma polaridade final;
4. calibrar as evidências positivas e negativas.
6. Construa 10 frases exemplo variadas, com polaridade, para teste.
5. (partindo de um corpus) calcule os termos (pos, neg, neg, intens) que mais contribuem 
para o cálculo da polaridade.

Partindo do livro Harry Potter e a Pedra Filosofal:

1. divida-o em capítulos e calcule as suas polaridades
2. calibre o calculador de polaridade de modo que a polaridade média
seja zero.
3. desenhe um histograma e compare com a versão Inglesa (calculada com
o módulo Vader, Blober ou outro semelhante.
4. compare com LeIA


# Sistema gerador com base em template-multifile

- usando jinja2
- construir a feramenta: template-multifile + metadados = árvore de ficheiros
- construir a feramenta: metadados + árvore de ficheiros = template-multifile.

