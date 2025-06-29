select
  z.ketto_toroku_bango
  , z.kaisai_nen || z.kaisai_gappi || z.keibajo_code || z.race_bango as race_id
  , z.pre_kaisai_nen || z.pre_kaisai_gappi || z.pre_keibajo_code || z.pre_race_bango as pre1_race_id
  , z.pre2_kaisai_nen || z.pre2_kaisai_gappi || z.pre2_keibajo_code || z.pre2_race_bango as pre2_race_id
  , z.pre3_kaisai_nen || z.pre3_kaisai_gappi || z.pre3_keibajo_code || z.pre3_race_bango as pre3_race_id
  , z.pre4_kaisai_nen || z.pre4_kaisai_gappi || z.pre4_keibajo_code || z.pre4_race_bango as pre4_race_id
  , z.pre5_kaisai_nen || z.pre5_kaisai_gappi || z.pre5_keibajo_code || z.pre5_race_bango as pre5_race_id
from zensou z
inner join kyosoba_master2 nu
  on nu.ketto_toroku_bango = z.ketto_toroku_bango
inner join race_shosai nr
  on nr.kaisai_nen = z.kaisai_nen
  and nr.kaisai_gappi = z.kaisai_gappi
  and nr.keibajo_code = z.keibajo_code
  and nr.race_bango = z.race_bango
where
  nr.kaisai_nen >= '2017'
  and nr.keibajo_code between '01' and '10'
  and nr.track_code < '30'
  and nr.kyoso_joken_code_saijakunen in ('010','016','999')
order by z.ketto_toroku_bango, z.kaisai_nen || z.kaisai_gappi || z.keibajo_code || z.race_bango