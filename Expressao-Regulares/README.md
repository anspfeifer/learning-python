# Expressao Regulares

## Usando a funcao Match
```
resultado = re.match('Py','Python')
resultado.group()

resultado = re.match('[pP]y','Python')
resultado.group()

resultado = re.match('[A-Za-z]y','Python')
resultado.group()

resultado = re.match('[A-Za-z]y','Python ou jython')
resultado.group()
```

## Usando a funcao findAll
- Meta caracteres
```
- Queremos todas as palavras que começam com expressão [A-Za-z]y
resultados = re.findall('([A-Za-z]y)','Python ou jython')
resultados = re.findall('([A-Za-z]y[A-Za-z]+)','Python ou jython ou PyPy')

- Caso queiramos buscar qualquer caracter, inclusive considerando números,
podemos para isso podemos usar [A-Za-z0-9], o \w também incorpora números.
resultados = re.findall('(\wy\w+)','Python ou jython ou PyPy')
resultados = re.findall('(\wy\w+\d)','Python3 ou jython2 ou PyPy')

Por exemplo, a expressão [A-Za-z]+\d? pega qualquer palavra com as letra de A-Z
independente de minuscula ou maiúscula contendo opcionalmente um número:
resultados = re.findall('[A-Za-z]+\d?','Python3 ou jython ou PyPy44')

```

- Mais quantificadores
```
Buscar todos os nomes que começam com a letra F.
resultados = re.findall('([fF]\w+)','Nico Flavio Fabiana Romulo')

Buscar todos os nomes que começam com uma determinada letra, mas devem ter uma quantidade mínima de caracteres
resultados = re.findall(r'[fF]\w{6}','Nico Flavio Fabiana Romulo')
resultado = re.match(r'^#','#comentarios começam com tralha!')
```


