# aprendendo-python-via-js

Provavelmente isso não ajude ninguém, mas achei interessante escrever algumas correlações simples q fiz,
pois estou aprendendo Python me baseando no que quero fazer, pois já fiz tudo em JS.

Logo, a forma mais fácil, IMHO, de aprender uma lang nova é tentar *codar* as coisas que vc já conhece.


# "Ementa"

- request HTTP
- transformação de Array em Objetos/Dicts
- separar valores definidos para "variáveis"
- datas

# Primeiras impressões

Não gostei mto de tudo parecer meio "global", tanto q já tive problemas de versão.

Tirando isso, qualquer coisa demanda muito menos tempo e linhas q no JS.

## Datas

Uma coisa que achei BEM ESTRANHA é que o Python trabalha o timestamp em SEGUNDOS e não milisegundos.
O mais engraçado que é mais simples e lógico porém tem uma coisa que destoou disso tudo, mas vou deixar
que você mesmo analise, caso nada tenha chamado sua atenção, melhor ainda.

JS: 

```js
dateNow = new Date()
days = 5
dateNow.setDate(dateNow.getDate() - days);
console.log(dateNow)
```

PY:

```py
from datetime import date, timedelta
days = 5
dateNow = date.today() - timedelta(days)
print(dateNow)
```

