#!/bin/sh

#create and change dir
if [ ! -d "github.repos" ]; then
  mkdir github.repos
fi

#get python repos without topic per year
curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2010.json \
  https://api.github.com/search/repositories?q=created:2010

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2011.json \
  https://api.github.com/search/repositories?q=created:2011

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2012.json \
  https://api.github.com/search/repositories?q=created:2012

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2013.json \
  https://api.github.com/search/repositories?q=created:2013

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2014.json \
  https://api.github.com/search/repositories?q=created:2014

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2015.json \
  https://api.github.com/search/repositories?q=created:2015

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2016.json \
  https://api.github.com/search/repositories?q=created:2016

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.repos/all.2017.json \
  https://api.github.com/search/repositories?q=created:2017


#TODO: read keywords
#create and change dir for keyword
if [ ! -d "github.ai" ]; then
  mkdir github.ai
fi

#get python repos with ai topic per year
curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2010.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2010

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2011.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2011

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2012.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2012

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2013.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2013

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2014.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2014

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2015.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2015

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2016.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2016

curl -H 'Accept: application/vnd.github.v3.text-match+json' -o ./github.ai/ai.2017.json \
  https://api.github.com/search/repositories?q=topic:ai+created:2017

