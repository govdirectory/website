@_default:
        just --list

# build the full project
build:
        snowman build --timeit

# build the full project and once done, start the development server
build-serve:
        snowman build --timeit && snowman server

# only update the static files of the last build
build-static:
        snowman build --static

# clear all queries from the cache
clear-cache:
        snowman cache --invalidate

# setup a new cache from our remote cache repository
bootstrap-cache:
        git clone https://github.com/govdirectory/website-cache .snowman

