#!/bin/sh

#create and change dir
if [ ! -d "github" ]; then
  mkdir githubdata
fi
cd githubdata

#get python repos with ai topic sorted by creation date
curl -H 'Accept: application/vnd.github.v3.text-match+json' -o python.ai.json \
  https://api.github.com/search/repositories?q=language:python+topic:ai&sort=created_at&order=desc

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o all.ai.json \
  https://api.github.com/search/repositories?q=topic:ai&sort=created_at&order=desc

