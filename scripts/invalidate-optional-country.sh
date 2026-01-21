#/bin/sh

if [[ $1 == "" ]]
  then
  echo "Missing the country argument."
  exit 0
fi

for i in $(find site/$1/* -type d);
  do
  qid=$(echo ${i%%/} | cut -f3 -d"/");
  echo $qid
  snowman cache sparql clear organization-optional.rq $qid
done
