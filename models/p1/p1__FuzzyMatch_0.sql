{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH FuzzyMatch_0 AS (

  {{ DatabricksSqlBasics.FuzzyMatch('', '', '', '', {  }, 80, false) }}

)

SELECT *

FROM FuzzyMatch_0
