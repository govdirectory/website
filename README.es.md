# Govdirectory

Idioma:
[Ingles](README.md) | [Español](README.es.md)

[![CC0 1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENCIA)
[![Pacto de Contribuyentes](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)
[![compatible con standard-readme](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme)
[<img src="https://github.com/govdirectory/website/blob/main/static/dpgbadge.svg" width="69"/>](https://www.digitalpublicgoods.net/r/govdirectory)
[![Mastodon](https://fedi-badge.deno.dev/@govdirectory@wikis.world/followers.svg?style=flat)](https://wikis.world/@govdirectory)

Repositorio del sitio web de Govdirectory: un directorio colaborativo y verificado de cuentas y servicios oficiales gubernamentales en línea.

Govdirectory tiene como objetivo convertirse en un directorio global de agencias gubernamentales y su presencia en internet utilizando Wikidata.
La comunidad de Wikidata, la verificabilidad de las fuentes, el versionado y las posibles herramientas personalizadas que creemos garantizarán que la información no solo sea correcta, sino que, cuando no lo sea debido a vandalismo u otros motivos, los usuarios puedan —y se les recomiende— verificarla.
El objetivo es que este directorio sea útil para periodistas, archivistas web, investigadores y muchas otras personas, incluyendo por supuesto a ciudadanos comunes.

> [!TIP]
> Todos los viernes a las 15:00 CET/CEST tenemos una sesión abierta en [Jitsi](https://meet.jit.si/GovdirectoryCollabHour) donde programamos y trabajamos juntos en los datos. Todos son bienvenidos y el espacio está abierto para preguntas.

## Configuración de desarrollo

Govdirectory es un sitio estático, lo que significa que todas sus páginas ya están generadas cuando un visitante accede a él. Govdirectory utiliza Snowman y [SPARQL](https://www.w3.org/TR/sparql11-query/) para lograr esto.

> [!TIP]
> Algunos de los comandos de desarrollo más comunes están disponibles mediante [Just](https://github.com/casey/just). Si no utilizas Just, igualmente puedes revisar el archivo `justfile` para obtener referencias.

### Requisitos previos

- [Git](https://git-scm.com/)
- [Snowman](https://github.com/glaciers-in-archives/snowman)

1\. Clonar el proyecto:

```shell
git clone https://github.com/govdirectory/website --single-branch

2. Obtener una copia reciente de la caché de compilación:

cd website
git clone https://github.com/govdirectory/website-cache .snowman

3. Compilar el sitio web y ejecutar el servidor de desarrollo:

snowman build && snowman server
Temas avanzados
Snowman: Working with cache
Uso

Pensado para ser utilizado a través del sitio web en govdirectory.org.

Mantenedores
Abbe98
Ainali

Por ahora, los mantenedores tienen la decisión final en todos los asuntos, aunque tomamos en consideración todas las opiniones de los contribuidores.
A medida que la comunidad crezca, planeamos migrar hacia un modelo de gobernanza con responsabilidades compartidas.
Además de contactarnos mediante issues, pull requests y discussions, también puedes encontrarnos en Mastodon como @ainali y @abbe98.

Agradecimientos
Programa acelerador Unlock

Este proyecto participó en el programa Unlock accelerator program (solicitud original).

Durante el acelerador, que finalizó en octubre de 2021, definimos un Producto Mínimo Viable (MVP):
"Como MVP queremos crear un sitio web funcional donde las personas puedan buscar, filtrar y agregar datos sobre instituciones públicas suecas y británicas y sus cuentas de redes sociales."

En particular, queremos agradecer toda la ayuda que nuestro mentor Fabian Gampp nos brindó. Además de su excelente mentoría general, probablemente no habríamos tomado una dirección tan ambiciosa para el diseño del sitio web sin él.

Servidor Matomo

Wikimedia Sverige nos proporciona generosamente análisis mediante Matomo. El panel se ha hecho públicamente accesible.

Open Social Fund

Este proyecto recibió una subvención para destacar aspectos del Fediverso por parte de NLnet Foundation a través de su Open Social Fund.

Contribuir

Estamos buscando personas como tú para contribuir a este proyecto sugiriendo mejoras y ayudando a desarrollarlo. Comienza leyendo nuestra guía para contribuidores.

Ten en cuenta que este proyecto se desarrolla bajo un código de conducta. Al participar en este proyecto, aceptas respetar sus términos. Por favor, sé amable con todos los demás miembros de la comunidad.

Licencia

Este repositorio y todas las contribuciones realizadas en él están licenciados bajo la CC0 1.0 Universal public domain dedication, salvo que se indique lo contrario dentro de un archivo o directorio.