# Add a country

This document describes how to add a country from [Wikidata:WikiProject Govdirectory](https://www.wikidata.org/wiki/Wikidata:WikiProject_Govdirectory).

## Background

The contents at govdirectory.org are driven by a set of SPARQL queries which together return all the data displayed.

Each country, therefore, got its own "generator" query, a query that for a given country returns all of the government organizations which should be included on Govdirectory as well as some basic information about them.

There is also a query in which one defines various country-level information, such as a description describing what content is currently included for the country in question, the name of the country, and the county's intended Govdirectory URL.

Each query is connected to a "View" a piece of configuration connecting the query, to the URL where the government organizations for a given country should be rendered.

## Setup

### The country generator query

Creating the country query is the most complex and tricky part of adding a country to Govdirectory. You can at any point ask for help over at our [GitHub discussions forum](https://github.com/govdirectory/website/discussions) or over at [Wikidata](https://www.wikidata.org/wiki/Wikidata_talk:WikiProject_Govdirectory).

Let's start by looking at the existing query for Sweden:

```sparql
# expected_result_count: 669
SELECT DISTINCT
  ?qid
  ?orgLabel
  ?orgDescription
  ?type
  ?typeLabel
  ?country
WHERE {
  BIND(wd:Q34 AS ?country)

  VALUES ?type {
    wd:Q68295960 # Swedish government agency(förvaltningsmyndighet) (249)
    wd:Q107407151 # Swedish government agency(myndighet under riksdagen) (5)
    wd:Q127448 # municipality of Sweden (290)
    wd:Q1754161 # regional council in Sweden (20)
    wd:Q196321 # county administrative board (21)
    wd:Q10397683 # AP-fund (6)
    wd:Q59603261 # state-ownded enterprise (3)
    wd:Q10330441 # state level departments (11)
    wd:Q341627 # court of appeal(hovrätten) (6)
    wd:Q2065704 # local court(tingsrätt) (48)
    wd:Q190752 # supreame court (2)
    wd:Q1289455 # administrative court of appeal (4)
    wd:Q18292311 # migration court (4)
  }
  ?org wdt:P31 ?type .

  ?org wdt:P17 ?country .

  MINUS { ?org wdt:P576 [] }
  MINUS { ?org wdt:P1366 [] }

  BIND(REPLACE(STR(?org), "http://www.wikidata.org/entity/", "") AS ?qid)

  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,sv" }
}
ORDER BY ?type ?orgLabel
```

Now Let's go through the parts one likely want to adapt to the country one wants to add.

```sparql
# expected_result_count: 669
```

The First line must be formatted like the one above, by stating the expected number of results automated checks can be performed and in case an unexpected number of results are returned an editor can quickly step in and solve the issue. Here all one should do is to update the number.

```sparql
  ?qid
  ?orgLabel
  ?orgDescription
  ?type
  ?typeLabel
  ?country
```

The section above illustrates which variables are expected by Govdirectory, one should not change these lines but they give one an insight into what is expected from the query. All except `?orgDescription`, `?type`, and `?typeLabel` are mandatory.

```sparql
  BIND(wd:Q34 AS ?country)
```

This line connects the query to a country in Wikidata, it's used to connect this query to the country configuration. Update the Wikidata identifier (Q-id).

```sparql
  VALUES ?type {
    wd:Q68295960 # Swedish government agency(förvaltningsmyndighet) (249)
    wd:Q107407151 # Swedish government agency(myndighet under riksdagen) (5)
    wd:Q127448 # municipality of Sweden (290)
    wd:Q1754161 # regional council in Sweden (20)
    wd:Q196321 # county administrative board (21)
    wd:Q10397683 # AP-fund (6)
    wd:Q59603261 # state-ownded enterprise (3)
    wd:Q10330441 # state level departments (11)
    wd:Q341627 # court of appeal(hovrätten) (6)
    wd:Q2065704 # local court(tingsrätt) (48)
    wd:Q190752 # supreame court (2)
    wd:Q1289455 # administrative court of appeal (4)
    wd:Q18292311 # migration court (4)
  }
```

These values are all of the various "instance of"/types the various government organizations might have, the labels of these will be displayed and used in Govdirectory. Note that the comments include the number of organizations each type should yield, this can be very useful if one needs to track down an error in the future.


```sparql
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,sv" }
```

All government organizations in a country might not have a name in English and therefore one should configure one or more fallback languages. In the example above Swedish is set as a fallback language.

Note that even with these changes in place one's query might still need additional information such as `MINUS` and `FILTER` clauses or triple patterns.

Finally, make sure to give a decent sort order of the agencies. This may vary by country, but a decent start may be to order be type and then label.

```sparql
  ORDER BY ?type ?orgLabel
```

Note that one can test the query in the Wikidata Query Service. One can also find more examples of [country queries here](https://github.com/govdirectory/website/tree/main/queries).

### The country configuration

The [`countries.rq`](https://github.com/govdirectory/website/blob/main/queries/countries.rq) query holds four pieces of information about a country:

 - The Wikidata URI
 - The name of the country as displayed to users of Govdirectory
 - The URL slug on which the country appears at on Govdirectory
 - A description of the content coverage

The configuration example below illustrates the configuration for Sweden and the United Kingdom. To add a new country one would create an additional line similar to the two found at lines 13-14 in the example below. The query will automatically include additional information.

```sparql
SELECT
  ?uri
  ?name
  ?safeName
  ?description
  (SAMPLE(?website) AS ?website)
  (SAMPLE(?nativeLabel) AS ?nativeLabel)
  (GROUP_CONCAT(DISTINCT ?typeOfGovLabel; separator=",") AS ?typeOfGovList)
  ?headOfStateLabel
  ?headOfGovLabel
WHERE {
  VALUES (?uri ?name ?safeName ?description) {
    (wd:Q34 'Sweden' 'sweden' 'Current content include municipalities, regional councils, and the courts of appeal.')
    (wd:Q145 'United Kingdom' 'united-kingdom' 'Current content only includes ministerial departments.')
  }
  
  OPTIONAL { ?uri wdt:P856 ?website }
  OPTIONAL { ?uri wdt:P35 ?headOfState }
  OPTIONAL { ?uri wdt:P6 ?headOfGov }
  OPTIONAL { ?uri wdt:P122 ?typeOfGov }
  OPTIONAL { ?uri wdt:P1705 ?nativeLabel }
  
  SERVICE wikibase:label {
    # this might need to be updated when new countries are added
    bd:serviceParam wikibase:language "en,sv" .
    ?headOfState rdfs:label ?headOfStateLabel .
    ?headOfGov rdfs:label ?headOfGovLabel .
    ?typeOfGov rdfs:label ?typeOfGovLabel .
  }
}
GROUP BY ?uri ?name ?safeName ?description ?headOfGovLabel ?headOfStateLabel

```

Note that one can test the query in the Wikidata Query Service.

### Configuring the view

Finally one only needs to tell the Govdirectory software about the new data. This is done in Govdirectory's "views.yaml" file. Here is an example of such a section connecting the query and the template:

```yaml
output: "sweden/{{qid}}/index.html"
query: "generators/sweden.rq"
template: "org.html"
```

All one needs to do here is to make section like the one above and "sweden"(in two places) with the URL slug of the country in question(as defined in one's country configuration). One can find more examples of [view configurations in the current "views.yaml" file](https://github.com/govdirectory/website/blob/main/views.yaml#L37).

### Get help

 - [GitHub discussions forum](https://github.com/govdirectory/website/discussions)
 - [Wikidata](https://www.wikidata.org/wiki/Wikidata_talk:WikiProject_Govdirectory)
