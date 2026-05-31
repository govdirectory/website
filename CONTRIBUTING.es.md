# Contribuir a Govdirectory

Idioma:
[Ingles](CONTRIBUTING.md) | [Español](CONTRIBUTING.es.md)

🙇‍♀️ Gracias por contribuir!

Nos encantan los issues y pull request de cualquier persona.
Si no te sientes cómodo utilizando esas funciones de GitHub, tambien puedes [start a discussion](https://github.com/govdirectory/website/discussions).

## Dirección

Al contribuir, puede ser útil saber en qué queremos que se convierta esta herramienta.
Hemos definido nuestra **vision** como:

>Nuestra visión es un mundo donde las personas estén capacitadas para interactuar con sus gobiernos y garantizar una toma de decisiones receptiva, inclusiva, participativa y representativa en todos los niveles.

Y tambien hemos establecido la siguiente **mission**:

>Habilitar una comunidad que mantenga un directorio colaborativo donde la presencia en línea de cada organización pública sea fácil de encontrar, consultar y confiar.

Esperamos que esto te ayude a contribuir de manera significativa.
Para conocer como se está utilizando actualmente el sitio web, consulta nuestras [Analiticas de Matomo](https://matomo.wikimedia.se/index.php?module=CoreHome&idSite=7).
Si deseas más detalles y conocer lo que ya tenemos planificado, revisa nuestra [hoja de ruta](https://github.com/orgs/govdirectory/projects/2) y [los hitos](https://github.com/govdirectory/website/milestones).

## Contribuciónes con IA

Como colaborador, eres en última instancia responsable tanto de la calidad del trabajo que envías como de tener los derechos necesarios para publicar dicho contenido bajo la licencia CC0.

Como regla general, las contribuciones realizadas con IA que no puedan identificarse como generadas con IA son bienvenidas. Si tus comentarios, código u otras formas de contribución pueden identificarse como generados con IA, serás bloquedo y tus contribuciónes serán marcadas como `spam`. Informamos regularmente a los usuarios que no respetan el tiempo y el esfuerzo de otros colaboradores.

## Problemas, sugerencias y preguntas en los issues

Por favos, ayuda al desarrollo reportando problemas, sugiriendo cambios y realizando preguntas.
Para hacer eso puedes [Crear un issue en GitHub](https://help.github.com/articles/creating-an-issue/) para este proyecto a través de [Issues de GitHub para la página web](https://github.com/govdirectory/website/issues/new).

En particular, utilizamos las etiquetas [good first issue](https://github.com/govdirectory/website/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) para que puedas identificar por dónde empezar, y [help wanted](https://github.com/govdirectory/website/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) para señalar aquellas tareas en donde todavia necesitamos colaboración.

¡No es necesario modificar nuestro código o documentación para ser un colaborador!

## Hora semanal de colaboración

Todos los viernesa a las 15.00 CEST realizamos una sesión abierta en [Jitsi](https://meet.jit.si/GovdirectoryCollabHour) donde trabajamos conjuntamente en el proyecto y en los datos. Todas las personas son bienvenidas y el espacio está abierto para preguntas.

## Documentación y código mediante pull request

Si deseas agregar contenido a la documentación o al código de alguno de nuestros proyectos, debes crear un pull request.
No es necesario que un issue te sea asignado para poder trabajar en él (de hecho, eliminaremos los comentarios que soliciten que se les asigne un issue).

Si nunca has utilizado GitHub, te recomendamos ponerte al día con alguno de los excelentes cursos interactivos gratuitos de [GitHub learning lab](https://lab.github.com/) sobre el uso de GitHub y Markdown, el lenguaje de marcado utilizado en la documentación de este proyecto.

Este proyecto está [licenciado bajo CC-0](LICENSE.md),lo que significa esencialmente que el proyecto, junto con tus contribuciones, pertenece al dominio público en cualquier jurisdicción donde sea posible, y que cualquier persona puede hacer con él lo que desee.

### 1. Realiza tus cambios

En este proyecto utilizamos ramas (branches) para realizar cambios y normalmente no hacemos commits directamente en la rama principal (main).
Una vez que hayas hecho un fork de este repositorio, asegúrate de crear una rama de funcionalidad (feature branch).

- Crea un [fork](https://github.com/govdirectory/website/fork) del repositorio.
- Crea o utiliza una rama de funcionalidad (feature branch) existente para realizar tus commits.
- Agrega tus cambios mediante commits con [mensajes descriptivos y útiles](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message).
    Incluye en el mensaje del commit las decisiones o elecciones de documentación que hayas tomado, Esto permitirá que otras personas comprendan dichas decisiones en el futuro.

- Si agregas código, añade y actualiza la **documentation** relevante y las pruebas correspondientes antes de enviar tu pull request.
- Asegúrate de escribir pruebas que demuestren el comportamiento del código nuevo o modificado.

#### Estándares a seguir

Estos son los estándares que utiliza Govdirectory.
Te animamos a enviar tu contribución incluso si no estás seguro de que cumpla completamente con ellos.
Trabajaremos contigo para alinear tu contribución antes de que sea fusionada.

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [standard readme](https://github.com/RichardLitt/standard-readme/blob/main/spec.md) (aplicabe únicamente al archivo README)
- [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) formato extendido de fechas (por ejemplo, 2023-09-17)

Para lo íconos utilizamos las bibliotecas [Maki](https://labs.mapbox.com/maki-icons/) y [Temaki](https://rapideditor.github.io/temaki/docs/) con el fin de mantener un estilo consistente. Si no encuentras un icono adecuado en esos conjuntos, intenta emular su estilo o utilizar otros iconos similares.

Para las imágenes estáticas de mapa de bits, preferimos utilizar el formato .webp, ya que permite optimizar y comprimir imágenes de forma eficiente. Considera convertir las nuevas imágenes al formato .webp utilizando herramientas como TinyPNG o similares. Esto ayuda a garantizar que las imágenes estén optimizadas para su uso en el sitio web desde el principio, contribuyendo a una experiencia de navegación más rápida y eficiente.

Aunque aún no nos hemos comprometido a cumplir completamente con el [Standard for Public Code](https://standard.publiccode.net) agradeceríamos que las contribuciones acerquen a Govdirectory al cumplimiento de dicho estándar en lugar de alejarlo de él.

### 2. Pull request

Al enviar un pull request, por favor acompáñalo con una descripción del problema que intentas resolver y los números de los issues que dicho pull request corrige.

### 3. Mejorar

#### Pruebas

Las pruebas deben aprobarse antes de que tu código pueda ser fusionado.

Puedes ejecutarlas localmente y encontrarlas en scripts/tests.

#### Revisiones

Todas las contribuciones deben ser revisadas por alguien.

Actualmente, todos los mantenedores que realizan revisiones son voluntarios. Revisaremos las contribuciones tan rápido como nos sea posible, aunque podría pasar hasta una semana antes de que recibas una respuesta.

Es posible que un mantenedor pueda fusionar tu contribución inmediatamente.

Sin embargo, normalmente un nuevo pull request requiere algunas mejoras antes de poder ser fusionado.
Otros colaboradores (o robots de asistencia) podrían proporcionar comentarios y sugerencias.

Si este es el caso, el mantenedor encargado de la revisión te ayudará a mejorar tu documentación y tu código.

Una vez que tu documentación y tu código hayan superado la revisión humana, serán fusionados.

Para los revisores: comprueben que las contribuciones cumplen los estándares, la arquitectura general y otras decisiones documentadas, así como que se encuentren dentro del alcance del proyecto.

Comprueben también que las consultas nuevas o modificadas produzcan los resultados esperados y que se visualicen correctamente en el sitio web.

## Mejorar los datos en wikidata

Tambien puedes ayudar al proyecto mejorando los datos sobre organismos púbilos en wikidata [Wikidata](https://wikidata.org).
Actualmente necesitamos lo siguiente:

1. Agregar todos los organismos públicos. Puedes comenzar con los de tu país. Los organismos públicos son entidades relevantes por naturaleza, por lo que no necesitas preocuparte por eso. Añade fuentes y/o identificadores externos para que sea posible verificar su existencia.
2. Asegurarte de que sea posible diferenciar, mediante consultas, los organismos activos de los organismos históricos.
3. Añadir propiedades básicas como el país (P17) y el nivel administrativo al que pertenecen (estatal, regional, local, etc.). La forma de modelar esta información puede variar según el país. Si es posible, añade también el tipo de organismo (por ejemplo, protección ambiental o administración tributaria).
4. Añadir las plataformas en línea que puedas encontrar para ellos. Las más comunes son el canal de YouTube (P2397), Facebook (P2013), X (anteriormente Twitter) (P2002), Instagram (P2003) y LinkedIn (P4264). Estas son las plataformas que se muestran mediante iconos en el directorio. Sin embargo, también es útil añadir otras plataformas en las que la institución tenga actividad y que dispongan de propiedades en Wikidata, ya que también se mostrarán en la página de la institución.

### Requisitos especiales de los datos

La mayoría de los datos se obtienen de Wikidata sin requisitos particulares. Sin embargo, los datos indicados a continuación tienen requisitos adicionales que los colaboradores deben tener en cuenta:

| Dato | Requisito |
|--------|--------|
| Número de telefono | Para que un número de teléfono se muestre, debe estar respaldado por una o más referencias. |
| Texto normativo principal| Para que un texto normativo principal se muestre, el elemento que describe dicho texto debe contener las declaraciones full work available online at y title. |

Puedes comprobar si una organización en Wikidata cumple estos requisitos utilizando la siguiente consulta SPARQL:
[organization-optional.rq](https://github.com/govdirectory/website/blob/main/queries/organization-optional.rq)

## Añadir un país a la interfaz

Si los datos de un país tienen una calidad suficientemente alta, pueden añadirse al directorio.
La guía [Add a country](ADD_A_COUNTRY.md) explica como hacerlo.

## Comentarios y sugerencias

Tambien puedes ayudarnos [indacándonos](https://github.com/govdirectory/website/discussions) cómo te gustaria usar un recurso como este.

## Para los mantenedores

Las secciones siguientes están dirigidas a los mantenedores que gestionan repositorios, despliegues y otras funciones administrativas.

### Despliegue en govdirectory.org

consulta [DEPLOY.md](DEPLOY.md).

### Actualización del repositorio `website-cache`

El repositorio `website-cache` permite que los desarrolladores puedan inicializar su caché de Snowman al compilar el sitio web de Govdirectory localmente. Esto acelera considerablemente la primera compilación y evita miles de consultas a WDQS.

```sh
cd .snowman
# remove unused cache
snowman cache sparql clear --unused
git add *
git commit -m "updating cache"
git push --force
```

### Replicación del repositorio `website` en Codeberg.org

Configurar el destino de replicación:

```sh
git remote add codeberg https://codeberg.org/Govdirectory/website.git
```

Replicar la rama Principal:

```
git push codeberg main
```

