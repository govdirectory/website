# Añadir un país

Este documento decribe cómo añadir un país desde [Wikidata:WikiProject Govdirectory](https://www.wikidata.org/wiki/Wikidata:WikiProject_Govdirectory).

Idioma:
[Ingles](ADD_A_COUNTRY.md) | [Español](ADD_A_COUNTRY.es.md)

## Antecedentes

El contenido de govdirectory.org se genera a partir de un conjunto de consultas SPARQL que, en conjunto, devuelven todos los datos mostrados en el sitio.

Por lo tanto, cada país tiene su propia consulta generadora (generator query), una consulta que devuelve, para un país determinado, todas las organizaciones gubernamentales que deben incluirse en Govdirectory, junto con información básica sobre ellas.

También existe una consulta en la que se define diversa información a nivel de país, como una descripción que indica qué contenido está incluido actualmente para el país en cuestión, el nombre del país y la URL prevista de Govdirectory para dicho país.

Cada consulta está asociada a una View, una parte de la configuración que conecta la consulta con la URL donde deben mostrarse las organizaciones gubernamentales de un país determinado.

## Configuración

### La consulta generadora del país

La creación de la consulta del país es la parte más compleja y delicada del proceso de añadir un país a Govdirectory. En cualquier momento puedes solicitar ayuda a través de nuestro  [foro de discusiónes de GitHub](https://github.com/govdirectory/website/discussions) o en [Wikidata](https://www.wikidata.org/wiki/Wikidata_talk:WikiProject_Govdirectory).

Comencemos observando la consulta existente para Suecia:

```sparql
# expected_result_count: 669
SELECT DISTINCT
  ?qid
  ?orgLabel
  ?orgDescription
  ?type
  ?typeLabel
  ?country
WHERE {
  BIND(wd:Q34 AS ?country)

  VALUES ?type {
    wd:Q68295960 # Swedish government agency(förvaltningsmyndighet) (249)
    wd:Q107407151 # Swedish government agency(myndighet under riksdagen) (5)
    wd:Q127448 # municipality of Sweden (290)
    wd:Q1754161 # regional council in Sweden (20)
    wd:Q196321 # county administrative board (21)
    wd:Q10397683 # AP-fund (6)
    wd:Q59603261 # state-owned enterprise (3)
    wd:Q10330441 # state level departments (11)
    wd:Q341627 # court of appeal(hovrätten) (6)
    wd:Q2065704 # local court(tingsrätt) (48)
    wd:Q190752 # supreme court (2)
    wd:Q1289455 # administrative court of appeal (4)
    wd:Q18292311 # migration court (4)
  }
  ?org wdt:P31 ?type .

  ?org wdt:P17 ?country .

  MINUS { ?org wdt:P576 [] }
  MINUS { ?org wdt:P1366 [] }

  BIND(REPLACE(STR(?org), "http://www.wikidata.org/entity/", "") AS ?qid)

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul,sv" }
}
ORDER BY ?type ?orgLabel
```

Ahora revisaremos las partes que normalmente será necesario adaptar para el país que se desea añadir.

```sparql
# expected_result_count: 669
```

La primera línea debe tener el formato mostrado arriba, indicando el número esperado de resultados.

De esta manera, pueden realizarse comprobaciones automáticas y, si se devuelve una cantidad inesperada de resultados, un editor podrá detectar rápidamente el problema e intervenir para resolverlo.

En este caso, lo único que debe hacerse es actualizar el número para que coincida con la cantidad esperada de resultados de la consulta.

```sparql
  ?qid
  ?orgLabel
  ?orgDescription
  ?type
  ?typeLabel
  ?country
```

La sección anterior muestra las variables que Govdirectory espera recibir. No se deben modificar estas líneas, pero proporcionan una idea de la información que se espera de la consulta.
Todas son obligatorias excepto `?orgDescription`, `?type`, and `?typeLabel` .

```sparql
  BIND(wd:Q34 AS ?country)
```

Esta línea vincula la consulta con un país en Wikidata. Se utiliza para conectar esta consulta con la configuración del país correspondiente. Debes actualizar el idetificador de wikidata (Q-id).

```sparql
  VALUES ?type {
    wd:Q68295960 # Swedish government agency(förvaltningsmyndighet) (249)
    wd:Q107407151 # Swedish government agency(myndighet under riksdagen) (5)
    wd:Q127448 # municipality of Sweden (290)
    wd:Q1754161 # regional council in Sweden (20)
    wd:Q196321 # county administrative board (21)
    wd:Q10397683 # AP-fund (6)
    wd:Q59603261 # state-owned enterprise (3)
    wd:Q10330441 # state level departments (11)
    wd:Q341627 # court of appeal(hovrätten) (6)
    wd:Q2065704 # local court(tingsrätt) (48)
    wd:Q190752 # supreme court (2)
    wd:Q1289455 # administrative court of appeal (4)
    wd:Q18292311 # migration court (4)
  }
```

Estos valores representan los distintos tipos o categorías  "instance of" que pueden tener las diferentes organizaciones gubernamentales, las etiquetas de estos tipos se mostrarán y utilizarán en Govdirectory. Ten en cuenta que los comentarios incluyen la cantidad de organizaciones que debería devolver cada tipo, esta información puede resultar muy útil si en el futuro es necesario investigar o corregir algún problema.


```sparql
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul,sv" }
```

Es posible que no todas las organizaciones gubernamentales de un país tengan un nombre disponible en inglés. Por ello, se recomienda configurar uno o más idiomas de respaldo (fallback languages), en el ejemplo anterior, el sueco (sv) está configurado como idioma de respaldo.

Ten en cuenta que, incluso después de realizar estos cambios, la consulta podría requerir información adicional, como cláusulas `MINUS` , `FILTER` o patrones de triples.

Por último, asegúrate de definir un criterio de ordenación adecuado para las agencias, esto puede variar según el país, pero una buena opción inicial suele ser ordenar primero por tipo y después por etiqueta.

```sparql
  ORDER BY ?type ?orgLabel
```

Ten en cuenta que puedes probar una consulta en Wikidata Query Service. Tambien puedes encontrar mas ejemplos de países en el [directorio queries del repositorio](https://github.com/govdirectory/website/tree/main/queries).

### La configuración del país

La consulta [`countries.rq`](https://github.com/govdirectory/website/blob/main/queries/countries.rq) contiene cuatro elementos de información sobre cada país:

 - El URI de Wikidata.
 - El nombre del país exactamente como se muestra a los usuarios de Govdirectory.
 - El slug de la URL en la que aparece el país dentro de Govdirectory.
 - Una descripción de la cobertura del contenido.

El ejemplo siguiente de configuración muestra la configuración para Suecia y el Reino Unido. Para añadir un nuevo país, se debe crear una línea adicional similar a las que aparecen en las líneas 13 y 14 del ejemplo mostrado a continuación, la consulta incluirá automáticamente la información adicional correspondiente.

```sparql
SELECT
  ?uri
  ?name
  ?safeName
  ?description
  ?parts
  (SAMPLE(?website) AS ?website)
  (SAMPLE(?nativeLabel) AS ?nativeLabel)
  (GROUP_CONCAT(DISTINCT ?typeOfGovLabel; separator=",") AS ?typeOfGovList)
  ?headOfStateLabel
  ?headOfGovLabel
  ?geoshape
  ?wikipedia
WHERE {
  VALUES (?uri ?name ?safeName ?description ?parts) {
    (wd:Q34 'Sweden' 'sweden' 'All Swedish government agencies are included.' '')
    (wd:Q223 'Greenland' 'greenland' 'Current content includes municipalities.' '')
  }

  OPTIONAL {
    ?uri wdt:P856 ?website .
    ?uri wdt:P37 ?lang .
    OPTIONAL {
      ?uri p:P856 ?ws .
      ?ws pq:P407 ?language .
      FILTER (?language IN  (?lang, wd:Q1860 ))
    }
  }
  OPTIONAL { ?uri wdt:P35 ?headOfState }
  OPTIONAL { ?uri wdt:P6 ?headOfGov }
  OPTIONAL { ?uri wdt:P122 ?typeOfGov }
  OPTIONAL { ?uri wdt:P1705 ?nativeLabel }

  ?uri wdt:P3896 ?geoshape .
  OPTIONAL {
    ?wikipedia schema:about ?uri ;
               schema:isPartOf <https://en.wikipedia.org/> .
  }
  SERVICE wikibase:label {
    # this might need to be updated when new countries are added
    bd:serviceParam wikibase:language "en,mul,sv,de" .
    ?headOfState rdfs:label ?headOfStateLabel .
    ?headOfGov rdfs:label ?headOfGovLabel .
    ?typeOfGov rdfs:label ?typeOfGovLabel .
  }
}
GROUP BY ?uri ?name ?safeName ?description ?parts ?headOfGovLabel ?headOfStateLabel ?geoshape ?wikipedia
ORDER BY ?name
```

Ten en cuenta que puedes probar la consulta en Wikidata Query Service.

### Configuración de la vista

Por último, solo es necesario informar al software de Govdirectory sobre los nuevos datos. Esto se realiza en el archivo "views.yaml" de Govdirectory. A continuación se muestra un ejemplo de una sección que conecta la consulta con la plantilla:

```yaml
output: "sweden/{{qid}}/index.html"
query: "generators/sweden.rq"
template: "org.html"
```

Lo único que debe hacerse aquí es crear una sección similar a la anterior y sustituir "sweden"(en ambos lugares) por el slug de URL del país correspondiente (tal como fue definido en la configuración del país). Puedes encontrar más ejemplos de [vistas en el archivo "views.yaml" actual](https://github.com/govdirectory/website/blob/main/views.yaml#L37).

## Obtener ayuda

 - [Foro de discusiones de GitHub](https://github.com/govdirectory/website/discussions)
 - [Wikidata](https://www.wikidata.org/wiki/Wikidata_talk:WikiProject_Govdirectory)
