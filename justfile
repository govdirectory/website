@_default:
        just --list

build:
        snowman build --timeit

build-serve:
        snowman build --timeit && snowman server

build-static:
        snowman build --static

clear-query-cache:
        snowman cache --invalidate

bootstrap-cache:
        git clone https://github.com/govdirectory/website-cache .snowman

