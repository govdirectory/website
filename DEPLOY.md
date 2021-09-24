# Deployment instructions

## Overview

Govdirectory is a static site, meaning that all files are generated pre-deployment. Govdriectory is generated using [Snowman](https://github.com/glaciers-in-archives/snowman) and its `build` command. Using the build command generates a `site` directory. This folder contains all files necessary for the govdirectory.org website.

Govdirectory is currently published using [Github Pages](https://pages.github.com/) and its source is the [`gh-pages` branch](https://github.com/govdirectory/website/tree/gh-pages) in this repository. To deploy the site:

 - Checkout the `gh-pages`.
 - Delete all the contents of that branch(if your are using your file manager, skip `.git`)
 - Copy all the contents of the `site` directory you want to deploy into the `gh-pages` branch.
 - Commit all files and changes.
 - Push your commit to origin.

Github will now automatically deploy the site. It might take a while for the changes to go into effect.

## Partial deploys

By default Snowman caches all data from the used SPARQL endpoint. therefore, to update data one needs to clear the cache(`snowman cache --invalidate`). However, for a large site like Govdirectory we often want to update only partial parts of the site to decrease to load on the SPARQL endpoint and to decrease build times.

### Update all data for a country

Govdirectory contains a helper script to clear the cache for all agencies under a given country. The country argument should match the "safe-name" of the intended query.

`./scripts/invalidate-social-media-country.sh sweden`

### Update all data for a specific SPARQL query

Sometimes you might need to only clear the cache for a specific query. How to do this is described in the [Snowman docummentation](https://github.com/glaciers-in-archives/snowman#invalidate-cache).
