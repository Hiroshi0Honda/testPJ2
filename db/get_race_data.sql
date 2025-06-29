select
  nr.kaisai_nen || nr.kaisai_gappi || nr.keibajo_code || nr.race_bango as race_id
  , nr.keibajo_code
  , nr.track_code
  , cast(nr.kyori as integer) as kyori
  , case when nr.shiba_babajotai_code > '0' then nr.shiba_babajotai_code else nr.dirt_babajotai_code end as babacd
  , cast(nr.shusso_tosu as integer) as tosu
  , case 
      when nr.grade_code is null or nr.grade_code = '' or nr.grade_code = ' ' then 5
      when nr.grade_code = 'A' then 1
      when nr.grade_code = 'B' then 2
      when nr.grade_code = 'C' then 3
      else 4 
    end as grade_code
  , ar.mu
from race_shosai nr
inner join a_race ar
  on ar.kaisai_nen = nr.kaisai_nen
  and ar.kaisai_gappi = nr.kaisai_gappi
  and ar.keibajo_code = nr.keibajo_code
  and ar.race_bango = nr.race_bango
where
  nr.kaisai_nen >= '2017'
  and nr.keibajo_code between '01' and '10'
  and nr.track_code < '30'
  and nr.kyoso_joken_code_saijakunen in ('010','016','999')
order by nr.kaisai_nen, nr.kaisai_gappi, nr.keibajo_code, nr.race_bango
