with sub as (
select
  ketto_toroku_bango, kaisai_nen, kaisai_gappi, keibajo_code, race_bango
  , kaisai_nen || kaisai_gappi || keibajo_code || race_bango as race_id
  , case when t_pre_mu is not null then t_pre_mu when d_pre_mu is not null then d_pre_mu else s_pre_mu end as mu
from a_uma_race
where keibajo_code between '01' and '10'
order by kaisai_nen, kaisai_gappi, keibajo_code, race_bango
)
select 
  nur.kaisai_nen || nur.kaisai_gappi || nur.keibajo_code || nur.race_bango as race_id
  , nur.ketto_toroku_bango
  , nu.bamei as horse_id
  , nur.umaban
  , nu.ketto1_bamei
  , replace(trim(nur.kishumei_ryakusho), '　', '') as kisyu_id
  , cast(nur.tansho_odds as numeric) / 10.0 as odds
  , cast(nur.tansho_ninkijun as integer) as ninki
  , cast(nur.bataiju as numeric)
  , case when zogen_sa <> '' then 
      case when zogen_fugo = '-'  then cast(zogen_sa as numeric) * (-1) else cast(zogen_sa as numeric) end
      else 0
    end as batai_zogen
  , cast(nur.futan_juryo as numeric) / 10.0 as futan
  , case when sire.sire_rate is not null then sire.sire_rate else 0 end as sire_rate
  , case when s2.sire_rate is not null then s2.sire_rate else 0 end as sire_joken_rate
  , case when jockey.jockey_rate is not null then jockey.jockey_rate else 0 end as jockey_rate
  , case when (STDDEV_POP(sub.mu) over(partition by sub.race_id)) > 0 then
    round(
      (50.0 + 10.0 * (sub.mu - (avg(sub.mu) over(partition by sub.race_id))) / (STDDEV_POP(sub.mu) over(partition by sub.race_id)))
    , 2)
    else 0.0 
  end as hensa
  , case when ar.mu - ar2.mu is not null then ar.mu - ar2.mu else 0 end as rate_diff
  , cast(nur.kakutei_chakujun as integer) as race_order
  , cast(substr(nur.soha_time, 1, 1) as integer) * 600 + cast(substr(nur.soha_time, 2, 3) as integer) as soha_time
  , cast(nur.kohan_3f as integer) as kohan_3f
  , cast(corner1_juni as integer) as corner1
  , cast(corner2_juni as integer) as corner2
  , cast(corner3_juni as integer) as corner3
  , cast(corner4_juni as integer) as corner4
from umagoto_race_joho nur
inner join race_shosai nr
  on nr.kaisai_nen = nur.kaisai_nen
  and nr.kaisai_gappi = nur.kaisai_gappi
  and nr.keibajo_code = nur.keibajo_code
  and nr.race_bango = nur.race_bango
inner join kyosoba_master2 nu
  on nu.ketto_toroku_bango = nur.ketto_toroku_bango
inner join a_uma_race aur
  on aur.ketto_toroku_bango = nur.ketto_toroku_bango
  and aur.kaisai_nen = nur.kaisai_nen
  and aur.kaisai_gappi = nur.kaisai_gappi
  and aur.keibajo_code = nur.keibajo_code
  and aur.race_bango = nur.race_bango
inner join sub
  on sub.ketto_toroku_bango = nur.ketto_toroku_bango
  and sub.kaisai_nen = nur.kaisai_nen
  and sub.kaisai_gappi = nur.kaisai_gappi
  and sub.keibajo_code = nur.keibajo_code
  and sub.race_bango = nur.race_bango
inner join zensou z
  on z.ketto_toroku_bango = nur.ketto_toroku_bango
  and z.kaisai_nen = nur.kaisai_nen
  and z.kaisai_gappi = nur.kaisai_gappi
  and z.keibajo_code = nur.keibajo_code
  and z.race_bango = nur.race_bango
left outer join sire
  on sire.ketto1_bamei = nu.ketto1_bamei
  and sire.keibajo_code = ''
left outer join sire s2
  on s2.ketto1_bamei = nu.ketto1_bamei
  and s2.keibajo_code = nr.keibajo_code
  and s2.track_code = nr.track_code
  and s2.kyori = nr.kyori
left outer join jockey
  on jockey.kishumei_ryakusho = nur.kishumei_ryakusho
  and jockey.keibajo_code = ''
inner join a_race ar
  on ar.kaisai_nen = z.kaisai_nen
  and ar.kaisai_gappi = z.kaisai_gappi
  and ar.keibajo_code = z.keibajo_code
  and ar.race_bango = z.race_bango
inner join a_race ar2
  on ar2.kaisai_nen = z.pre_kaisai_nen
  and ar2.kaisai_gappi = z.pre_kaisai_gappi
  and ar2.keibajo_code = z.pre_keibajo_code
  and ar2.race_bango = z.pre_race_bango
where
  nr.kaisai_nen >= '2017'
  and nr.keibajo_code between '01' and '10'
  and nr.track_code < '30'
  and nr.kyoso_joken_code_saijakunen in ('010','016','999')
order by nur.kaisai_nen, nur.kaisai_gappi, nur.keibajo_code, nur.race_bango, nur.umaban