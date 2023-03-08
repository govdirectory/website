# Govdirectory

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/govdirectory/website)

Website repository for Govdirectory - a crowdsourced and fact-checked directory of official governmental online accounts and services.

Govdirectory aims to become a global directory of government agencies and their online presence by utilizing Wikidata.
Wikidatas community, sourceability, versioning, and potential custom tooling that we create will ensure that not only should the information be correct but when it isn't, because of vandalism or something else, users will be able, and suggested, to validate the information.
The goal is for this directory to be useful to journalists, web-archivists, researchers and many others, certainly including regular citizens.

## Development setup

Govdirectory is a static site meaning that it already has all of its pages generated when a visitor visits it. Govdirectory uses Snowman and SPARQL to do this.

Because each initial build of Snowman issues thousands (yes thousands) of SPARQL queries one should never an **initial** build against `query.wikidata.org` but rather against a local WDQS instance. However, because setting up a WDQS instance is nontrival we provide a copy of a [Snowman build cache directory](https://github.com/govdirectory/website-cache), if in use, this will ensure Snowman only queries Wikidata when a query is updated.

### Prerequisites

 - [Git](https://git-scm.com/)
 - [Snowman](https://github.com/glaciers-in-archives/snowman)
 - **Optinally**: A local Wikidata Query Service (WDQS) instance 

1\. Clone the project:
```shell
git clone https://github.com/govdirectory/website
```
2\. Get a rencent build cache:
```shell
cd website
git clone https://github.com/govdirectory/website-cache .snowman
```
3\. Build the website and run the development server:
```shell
snowman build && snowman server
```

### Advanced topics

 - [Setting up your own WDQS instance](https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual#Standalone_service)
 - [Snowman: Working with cache](https://github.com/glaciers-in-archives/snowman#working-with-cache)

## Usage

Intended to be used through the website at [govdirectory.org](https://govdirectory.org).

## Maintainers

* [Abbe98](https://github.com/Abbe98)
* [Ainali](https://github.com/Ainali)

Besides pinging us in [issues](https://github.com/govdirectory/website/issues), [pull requests](https://github.com/govdirectory/website/pulls) and [discussions](https://github.com/govdirectory/website/discussions), you can also reach us on Twitter where we are [@Jan_Ainali](https://twitter.com/Jan_Ainali/) and [@AlbinPCLarsson](https://twitter.com/AlbinPCLarsson).

## Acknowledgements

### Unlock accelerator program

This project participated in the [Unlock accelerator program](https://www.wikimedia.de/unlock/) program ([original application](https://www.wikidata.org/wiki/User:Ainali/Social_media_for_public_organizations/Unlock)).

During the accelerator, which ended in October 2021, we defined a Minimale Viable Product (MVP) to: "As an MVP we want to create a working website where people can search, filter, and add data about Swedish and British public institutions and their social media accounts."

Specifically, we want to acknowledge all the help our coach [Fabian Gampp](https://www.fabiangampp.de/) gave to us. Besides general good mentorship, we wouldn't have had such a bold direction of the design of the website without him.

### Matomo server

[Wikimedia Sverige](https://github.com/Wikimedia-Sverige) is graciously providing us with Matomo analytics. [The dashboard](https://matomo.wikimedia.se/index.php?module=CoreHome&idSite=7) has been made publicly accessible.

## Contributing

We are looking for people like you to [contribute](CONTRIBUTING.md) to this project by suggesting improvements and helping develop it. Get started by reading our [contributors guide](CONTRIBUTING.md).

Please note that this project is developed with a [code of conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms. Please be lovely to all other community members.

## License

This repository and all contributions made to it are licensed under the [CC0 1.0 Universal public domain dedication](LICENSE) if not otherwise stated within a file or directory.
