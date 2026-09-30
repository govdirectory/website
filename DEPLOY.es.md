# Instrucciónes de despliegue

Idioma:
[Ingles](DEPLOY.md) | [Español](DEPLOY.es.md)

## Descripción general

Govdirectory es un sitio estático, lo que significa que todos los archivos se generan antes del despliuegue. Govdirectory se genera utilizando[Snowman](https://github.com/glaciers-in-archives/snowman) y su comando `build`. Al ejecutar este comando se genera un directorio llamado `site`. Esta carpeta contiene todos los archivos necesarios para el sitio web Govdirectory.org.

Actualmente, Govdirectory se publica utilizando [GitHub Pages](https://pages.github.com/) y su fuente es la rama [`gh-pages` branch](https://github.com/govdirectory/website/tree/gh-pages) de este repositorio. Para desplegar el sitio:

 - Revisa la rama `gh-pages`.
 - Elimina todo el contenido de esa rama (si utilizas un gestro de archivos, no elimines `.git`)
 - Copia todo el contenido del directorio `site` que deseas desplegar dentro de la rama `gh-pages` branch.
 - Realiza un commit de todos los archivos y cambios.
 - Envia tu commit a `origin`.

GitHub desplegará automáticamente el sitio. Los cambios pueden tardar un poco en hacerse efectivos.

## Despliegue parciales

De forma predeterminada, Snowman almacena en caché todos los datos del endpoint de SPARQL utilizado. Por lo tanto, para actualizar los datos es necesario limpiar la caché (`snowman cache --invalidate`). Sin embargo, para un sitio grande como Govdirectory, a menudo queremos actualizar solo partes especificas del sitio para reducir la carga sobre el endpoint SPARQL y disminuir los tiempos de compilación.

### Actualizar todos los datos de un país

Govdirectory incluye un script auxiliar para limpiar la caché de todas las agencias pertenecientes a un país determinado. El argumento del país debe coincidir con el "safe-name" de la consulta correspondiente.

`./scripts/invalidate-social-media-country.sh sweden`

### Actiualizar todos los datos de una consulta SPARQL especifica.

En ocasiones puede ser necesario limpliar la caché únicamente para una consulta específica. La forma de hacerlo se describe en la [documentación snowman](https://github.com/glaciers-in-archives/snowman#invalidate-cache).
