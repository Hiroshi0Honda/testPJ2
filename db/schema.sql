create table public.race_shosai (
  insert_timestamp character(19)
  , update_timestamp character(19)
  , record_shubetsu_id character(2)
  , data_kubun character(1)
  , data_sakusei_nengappi character(8)
  , race_code character(16) not null
  , kaisai_nen character(4)
  , kaisai_gappi character(4)
  , keibajo_code character(2)
  , kaisai_kai character(2)
  , kaisai_nichime character(2)
  , race_bango character(2)
  , yobi_code character(1)
  , tokubetsu_kyoso_bango character(4)
  , kyosomei_hondai character varying(60)
  , kyosomei_fukudai character varying(60)
  , kyosomei_kakkonai character varying(60)
  , kyosomei_hondai_eng character varying(120)
  , kyosomei_fukudai_eng character varying(120)
  , kyosomei_kakkonai_eng character varying(120)
  , kyosomei_ryakusho_10 character varying(20)
  , kyosomei_ryakusho_6 character varying(12)
  , kyosomei_ryakusho_3 character varying(6)
  , kyosomei_kubun character(1)
  , jusho_kaiji character(3)
  , grade_code character(1)
  , henkomae_grade_code character(1)
  , kyoso_shubetsu_code character(2)
  , kyoso_kigo_code character(3)
  , juryo_shubetsu_code character(1)
  , kyoso_joken_code_2sai character(3)
  , kyoso_joken_code_3sai character(3)
  , kyoso_joken_code_4sai character(3)
  , kyoso_joken_code_5sai_ijo character(3)
  , kyoso_joken_code_saijakunen character(3)
  , kyoso_joken_meisho character varying(60)
  , kyori character(4)
  , henkomae_kyori character(4)
  , track_code character(2)
  , henkomae_track_code character(2)
  , course_kubun character(2)
  , henkomae_course_kubun character(2)
  , honshokin1 character(8)
  , honshokin2 character(8)
  , honshokin3 character(8)
  , honshokin4 character(8)
  , honshokin5 character(8)
  , honshokin6 character(8)
  , honshokin7 character(8)
  , henkomae_honshokin1 character(8)
  , henkomae_honshokin2 character(8)
  , henkomae_honshokin3 character(8)
  , henkomae_honshokin4 character(8)
  , henkomae_honshokin5 character(8)
  , fukashokin1 character(8)
  , fukashokin2 character(8)
  , fukashokin3 character(8)
  , fukashokin4 character(8)
  , fukashokin5 character(8)
  , henkomae_fukashokin1 character(8)
  , henkomae_fukashokin2 character(8)
  , henkomae_fukashokin3 character(8)
  , hasso_jikoku character(4)
  , henkomae_hasso_jikoku character(4)
  , toroku_tosu character(2)
  , shusso_tosu character(2)
  , nyusen_tosu character(2)
  , tenko_code character(1)
  , shiba_babajotai_code character(1)
  , dirt_babajotai_code character(1)
  , lap_time1 character(3)
  , lap_time2 character(3)
  , lap_time3 character(3)
  , lap_time4 character(3)
  , lap_time5 character(3)
  , lap_time6 character(3)
  , lap_time7 character(3)
  , lap_time8 character(3)
  , lap_time9 character(3)
  , lap_time10 character(3)
  , lap_time11 character(3)
  , lap_time12 character(3)
  , lap_time13 character(3)
  , lap_time14 character(3)
  , lap_time15 character(3)
  , lap_time16 character(3)
  , lap_time17 character(3)
  , lap_time18 character(3)
  , lap_time19 character(3)
  , lap_time20 character(3)
  , lap_time21 character(3)
  , lap_time22 character(3)
  , lap_time23 character(3)
  , lap_time24 character(3)
  , lap_time25 character(3)
  , shogai_mile_time character(4)
  , zenhan_3f character(3)
  , zenhan_4f character(3)
  , kohan_3f character(3)
  , kohan_4f character(3)
  , corner1 character(1)
  , shukaisu1 character(1)
  , kaku_tsuka_juni1 character varying(70)
  , corner2 character(1)
  , shukaisu2 character(1)
  , kaku_tsuka_juni2 character varying(70)
  , corner3 character(1)
  , shukaisu3 character(1)
  , kaku_tsuka_juni3 character varying(70)
  , corner4 character(1)
  , shukaisu4 character(1)
  , kaku_tsuka_juni4 character varying(70)
  , record_koshin_kubun character(1)
  , primary key (race_code)
);

create table public.umagoto_race_joho (
  insert_timestamp character(19)
  , update_timestamp character(19)
  , record_shubetsu_id character(2)
  , data_kubun character(1)
  , data_sakusei_nengappi character(8)
  , race_code character(16) not null
  , kaisai_nen character(4)
  , kaisai_gappi character(4)
  , keibajo_code character(2)
  , kaisai_kaiji character(2)
  , kaisai_nichiji character(2)
  , race_bango character(2)
  , wakuban character(1)
  , umaban character(2)
  , ketto_toroku_bango character(10) not null
  , bamei character varying(36)
  , umakigo_code character(2)
  , seibetsu_code character(1)
  , hinshu_code character(1)
  , moshoku_code character(2)
  , barei character(2)
  , tozai_shozoku_code character(1)
  , chokyoshi_code character(5)
  , chokyoshimei_ryakusho character varying(8)
  , banushi_code character(6)
  , banushimei_hojinkaku_nashi character varying(64)
  , fukushoku_hyoji character varying(60)
  , futan_juryo character(3)
  , henkomae_futan_juryo character(3)
  , blinker_shiyo_kubun character(1)
  , kishu_code character(5)
  , henkomae_kishu_code character(5)
  , kishumei_ryakusho character varying(8)
  , henkomae_kishumei_ryakusho character varying(8)
  , kishu_minarai_code character(1)
  , henkomae_kishu_minarai_code character(1)
  , bataiju character(3)
  , zogen_fugo character(1)
  , zogen_sa character(3)
  , ijo_kubun_code character(1)
  , nyusen_juni character(2)
  , kakutei_chakujun character(2)
  , dochaku_kubun character(1)
  , dochaku_tosu character(1)
  , soha_time character(4)
  , chakusa_code1 character(3)
  , chakusa_code2 character(3)
  , chakusa_code3 character(3)
  , corner1_juni character(2)
  , corner2_juni character(2)
  , corner3_juni character(2)
  , corner4_juni character(2)
  , tansho_odds character(4)
  , tansho_ninkijun character(2)
  , kakutoku_honshokin character(8)
  , kakutoku_fukashokin character(8)
  , kohan_4f character(3)
  , kohan_3f character(3)
  , aite1_ketto_toroku_bango character(10)
  , aite1_bamei character varying(36)
  , aite2_ketto_toroku_bango character(10)
  , aite2_bamei character varying(36)
  , aite3_ketto_toroku_bango character(10)
  , aite3_bamei character varying(36)
  , time_sa character(4)
  , record_koshin_kubun character(1)
  , mining_kubun character(1)
  , mining_yoso_soha_time character(5)
  , mining_yoso_gosa_plus character(4)
  , mining_yoso_gosa_minus character(4)
  , mining_yoso_juni character(2)
  , kyakushitsu_hantei character(1)
  , primary key (race_code, ketto_toroku_bango)
);

create table public.kyosoba_master2 (
  insert_timestamp character(19)
  , update_timestamp character(19)
  , record_shubetsu_id character(2)
  , data_kubun character(1)
  , data_sakusei_nengappi character(8)
  , ketto_toroku_bango character(10) not null
  , massho_kubun character(1)
  , toroku_nengappi character(8)
  , massho_nengappi character(8)
  , seinengappi character(8)
  , bamei character varying(36)
  , bamei_hankaku_kana character varying(36)
  , bamei_eng character varying(60)
  , jra_shisetsu_zaikyu_flag character(1)
  , umakigo_code character(2)
  , seibetsu_code character(1)
  , hinshu_code character(1)
  , moshoku_code character(2)
  , ketto1_hanshoku_toroku_bango character(10)
  , ketto1_bamei character varying(36)
  , ketto2_hanshoku_toroku_bango character(10)
  , ketto2_bamei character varying(36)
  , ketto3_hanshoku_toroku_bango character(10)
  , ketto3_bamei character varying(36)
  , ketto4_hanshoku_toroku_bango character(10)
  , ketto4_bamei character varying(36)
  , ketto5_hanshoku_toroku_bango character(10)
  , ketto5_bamei character varying(36)
  , ketto6_hanshoku_toroku_bango character(10)
  , ketto6_bamei character varying(36)
  , ketto7_hanshoku_toroku_bango character(10)
  , ketto7_bamei character varying(36)
  , ketto8_hanshoku_toroku_bango character(10)
  , ketto8_bamei character varying(36)
  , ketto9_hanshoku_toroku_bango character(10)
  , ketto9_bamei character varying(36)
  , ketto10_hanshoku_toroku_bango character(10)
  , ketto10_bamei character varying(36)
  , ketto11_hanshoku_toroku_bango character(10)
  , ketto11_bamei character varying(36)
  , ketto12_hanshoku_toroku_bango character(10)
  , ketto12_bamei character varying(36)
  , ketto13_hanshoku_toroku_bango character(10)
  , ketto13_bamei character varying(36)
  , ketto14_hanshoku_toroku_bango character(10)
  , ketto14_bamei character varying(36)
  , tozai_shozoku_code character(1)
  , chokyoshi_code character(5)
  , chokyoshimei_ryakusho character varying(8)
  , shotai_chiikimei character varying(20)
  , seisansha_code character(8)
  , seisanshamei_hojinkaku_nashi character varying(72)
  , sanchimei character varying(20)
  , banushi_code character(6)
  , banushimei_hojinkaku_nashi character varying(64)
  , heichi_honshokin_ruikei character(9)
  , shogai_honshokin_ruikei character(9)
  , heichi_fukashokin_ruikei character(9)
  , shogai_fukashokin_ruikei character(9)
  , heichi_shutokushokin_ruikei character(9)
  , shogai_shutokushokin_ruikei character(9)
  , sogo_1chaku character(3)
  , sogo_2chaku character(3)
  , sogo_3chaku character(3)
  , sogo_4chaku character(3)
  , sogo_5chaku character(3)
  , sogo_chakugai character(3)
  , chuo_gokei_1chaku character(3)
  , chuo_gokei_2chaku character(3)
  , chuo_gokei_3chaku character(3)
  , chuo_gokei_4chaku character(3)
  , chuo_gokei_5chaku character(3)
  , chuo_gokei_chakugai character(3)
  , shiba_choku_1chaku character(3)
  , shiba_choku_2chaku character(3)
  , shiba_choku_3chaku character(3)
  , shiba_choku_4chaku character(3)
  , shiba_choku_5chaku character(3)
  , shiba_choku_chakugai character(3)
  , shiba_migi_1chaku character(3)
  , shiba_migi_2chaku character(3)
  , shiba_migi_3chaku character(3)
  , shiba_migi_4chaku character(3)
  , shiba_migi_5chaku character(3)
  , shiba_migi_chakugai character(3)
  , shiba_hidari_1chaku character(3)
  , shiba_hidari_2chaku character(3)
  , shiba_hidari_3chaku character(3)
  , shiba_hidari_4chaku character(3)
  , shiba_hidari_5chaku character(3)
  , shiba_hidari_chakugai character(3)
  , dirt_choku_1chaku character(3)
  , dirt_choku_2chaku character(3)
  , dirt_choku_3chaku character(3)
  , dirt_choku_4chaku character(3)
  , dirt_choku_5chaku character(3)
  , dirt_choku_chakugai character(3)
  , dirt_migi_1chaku character(3)
  , dirt_migi_2chaku character(3)
  , dirt_migi_3chaku character(3)
  , dirt_migi_4chaku character(3)
  , dirt_migi_5chaku character(3)
  , dirt_migi_chakugai character(3)
  , dirt_hidari_1chaku character(3)
  , dirt_hidari_2chaku character(3)
  , dirt_hidari_3chaku character(3)
  , dirt_hidari_4chaku character(3)
  , dirt_hidari_5chaku character(3)
  , dirt_hidari_chakugai character(3)
  , shogai_1chaku character(3)
  , shogai_2chaku character(3)
  , shogai_3chaku character(3)
  , shogai_4chaku character(3)
  , shogai_5chaku character(3)
  , shogai_chakugai character(3)
  , shiba_ryo_1chaku character(3)
  , shiba_ryo_2chaku character(3)
  , shiba_ryo_3chaku character(3)
  , shiba_ryo_4chaku character(3)
  , shiba_ryo_5chaku character(3)
  , shiba_ryo_chakugai character(3)
  , shiba_yayaomo_1chaku character(3)
  , shiba_yayaomo_2chaku character(3)
  , shiba_yayaomo_3chaku character(3)
  , shiba_yayaomo_4chaku character(3)
  , shiba_yayaomo_5chaku character(3)
  , shiba_yayaomo_chakugai character(3)
  , shiba_omo_1chaku character(3)
  , shiba_omo_2chaku character(3)
  , shiba_omo_3chaku character(3)
  , shiba_omo_4chaku character(3)
  , shiba_omo_5chaku character(3)
  , shiba_omo_chakugai character(3)
  , shiba_furyo_1chaku character(3)
  , shiba_furyo_2chaku character(3)
  , shiba_furyo_3chaku character(3)
  , shiba_furyo_4chaku character(3)
  , shiba_furyo_5chaku character(3)
  , shiba_furyo_chakugai character(3)
  , dirt_ryo_1chaku character(3)
  , dirt_ryo_2chaku character(3)
  , dirt_ryo_3chaku character(3)
  , dirt_ryo_4chaku character(3)
  , dirt_ryo_5chaku character(3)
  , dirt_ryo_chakugai character(3)
  , dirt_yayaomo_1chaku character(3)
  , dirt_yayaomo_2chaku character(3)
  , dirt_yayaomo_3chaku character(3)
  , dirt_yayaomo_4chaku character(3)
  , dirt_yayaomo_5chaku character(3)
  , dirt_yayaomo_chakugai character(3)
  , dirt_omo_1chaku character(3)
  , dirt_omo_2chaku character(3)
  , dirt_omo_3chaku character(3)
  , dirt_omo_4chaku character(3)
  , dirt_omo_5chaku character(3)
  , dirt_omo_chakugai character(3)
  , dirt_furyo_1chaku character(3)
  , dirt_furyo_2chaku character(3)
  , dirt_furyo_3chaku character(3)
  , dirt_furyo_4chaku character(3)
  , dirt_furyo_5chaku character(3)
  , dirt_furyo_chakugai character(3)
  , shogai_ryo_1chaku character(3)
  , shogai_ryo_2chaku character(3)
  , shogai_ryo_3chaku character(3)
  , shogai_ryo_4chaku character(3)
  , shogai_ryo_5chaku character(3)
  , shogai_ryo_chakugai character(3)
  , shogai_yayaomo_1chaku character(3)
  , shogai_yayaomo_2chaku character(3)
  , shogai_yayaomo_3chaku character(3)
  , shogai_yayaomo_4chaku character(3)
  , shogai_yayaomo_5chaku character(3)
  , shogai_yayaomo_chakugai character(3)
  , shogai_omo_1chaku character(3)
  , shogai_omo_2chaku character(3)
  , shogai_omo_3chaku character(3)
  , shogai_omo_4chaku character(3)
  , shogai_omo_5chaku character(3)
  , shogai_omo_chakugai character(3)
  , shogai_furyo_1chaku character(3)
  , shogai_furyo_2chaku character(3)
  , shogai_furyo_3chaku character(3)
  , shogai_furyo_4chaku character(3)
  , shogai_furyo_5chaku character(3)
  , shogai_furyo_chakugai character(3)
  , shiba_short_1chaku character(3)
  , shiba_short_2chaku character(3)
  , shiba_short_3chaku character(3)
  , shiba_short_4chaku character(3)
  , shiba_short_5chaku character(3)
  , shiba_short_chakugai character(3)
  , shiba_middle_1chaku character(3)
  , shiba_middle_2chaku character(3)
  , shiba_middle_3chaku character(3)
  , shiba_middle_4chaku character(3)
  , shiba_middle_5chaku character(3)
  , shiba_middle_chakugai character(3)
  , shiba_long_1chaku character(3)
  , shiba_long_2chaku character(3)
  , shiba_long_3chaku character(3)
  , shiba_long_4chaku character(3)
  , shiba_long_5chaku character(3)
  , shiba_long_chakugai character(3)
  , dirt_short_1chaku character(3)
  , dirt_short_2chaku character(3)
  , dirt_short_3chaku character(3)
  , dirt_short_4chaku character(3)
  , dirt_short_5chaku character(3)
  , dirt_short_chakugai character(3)
  , dirt_middle_1chaku character(3)
  , dirt_middle_2chaku character(3)
  , dirt_middle_3chaku character(3)
  , dirt_middle_4chaku character(3)
  , dirt_middle_5chaku character(3)
  , dirt_middle_chakugai character(3)
  , dirt_long_1chaku character(3)
  , dirt_long_2chaku character(3)
  , dirt_long_3chaku character(3)
  , dirt_long_4chaku character(3)
  , dirt_long_5chaku character(3)
  , dirt_long_chakugai character(3)
  , kyakushitsu_keiko_nige character(3)
  , kyakushitsu_keiko_senko character(3)
  , kyakushitsu_keiko_sashi character(3)
  , kyakushitsu_keiko_oikomi character(3)
  , toroku_race_su character(3)
  , primary key (ketto_toroku_bango)
);

create table public.odds1_tansho (
  insert_timestamp character(19)
  , update_timestamp character(19)
  , record_shubetsu_id character(2)
  , data_kubun character(1)
  , data_sakusei_nengappi character(8)
  , race_code character(16) not null
  , kaisai_nen character(4)
  , kaisai_gappi character(4)
  , keibajo_code character(2)
  , kaisai_kaiji character(2)
  , kaisai_nichiji character(2)
  , race_bango character(2)
  , umaban character(2) not null
  , odds character(4)
  , ninki character(2)
  , primary key (race_code, umaban)
);

create table public.odds1_fukusho (
  insert_timestamp character(19)
  , update_timestamp character(19)
  , record_shubetsu_id character(2)
  , data_kubun character(1)
  , data_sakusei_nengappi character(8)
  , race_code character(16) not null
  , kaisai_nen character(4)
  , kaisai_gappi character(4)
  , keibajo_code character(2)
  , kaisai_kaiji character(2)
  , kaisai_nichiji character(2)
  , race_bango character(2)
  , umaban character(2) not null
  , odds_saitei character(4)
  , odds_saikou character(4)
  , ninki character(2)
  , primary key (race_code, umaban)
);

create table public.odds2_umaren (
  insert_timestamp character(19)
  , update_timestamp character(19)
  , record_shubetsu_id character(2)
  , data_kubun character(1)
  , data_sakusei_nengappi character(8)
  , race_code character(16) not null
  , kaisai_nen character(4)
  , kaisai_gappi character(4)
  , keibajo_code character(2)
  , kaisai_kaiji character(2)
  , kaisai_nichiji character(2)
  , race_bango character(2)
  , happyo_tsukihi_jifun character(8)
  , toroku_tosu character(2)
  , shusso_tosu character(2)
  , hatsubai_flag_umaren character(1)
  , kumiban character(4) not null
  , odds character(6)
  , ninki character(3)
  , umaren_hyosu_gokei character(11)
  , primary key (race_code, kumiban)
);

create table public.a_race (
  kaisai_nen text not null
  , kaisai_gappi text not null
  , keibajo_code text not null
  , race_bango text not null
  , tyaku text
  , mu numeric
  , primary key (kaisai_nen, kaisai_gappi, keibajo_code, race_bango)
);

create table public.a_uma_race (
  ketto_toroku_bango text not null
  , kaisai_nen text not null
  , kaisai_gappi text not null
  , keibajo_code text not null
  , race_bango text not null
  , t_mu numeric
  , t_sigma numeric
  , t_pre_mu numeric
  , t_pre_sigma numeric
  , d_mu numeric
  , d_sigma numeric
  , d_pre_mu numeric
  , d_pre_sigma numeric
  , s_mu numeric
  , s_sigma numeric
  , s_pre_mu numeric
  , s_pre_sigma numeric
  , primary key (ketto_toroku_bango, kaisai_nen, kaisai_gappi, keibajo_code, race_bango)
);

create table public.a_uma (
  ketto_toroku_bango text not null
  , t_mu numeric
  , t_sigma numeric
  , d_mu numeric
  , d_sigma numeric
  , s_mu numeric
  , s_sigma numeric
  , primary key (ketto_toroku_bango)
);

create table public.zensou (
  ketto_toroku_bango text not null
  , kaisai_nen text not null
  , kaisai_gappi text not null
  , pre_kaisai_nen text
  , pre_kaisai_gappi text
  , keibajo_code text not null
  , race_bango text not null
  , pre_keibajo_code text
  , pre_race_bango text
  , pre2_kaisai_nen text
  , pre2_kaisai_gappi text
  , pre2_keibajo_code text
  , pre2_race_bango text
  , pre3_kaisai_nen text
  , pre3_kaisai_gappi text
  , pre3_keibajo_code text
  , pre3_race_bango text
  , pre4_kaisai_nen text
  , pre4_kaisai_gappi text
  , pre4_keibajo_code text
  , pre4_race_bango text
  , pre5_kaisai_nen text
  , pre5_kaisai_gappi text
  , pre5_keibajo_code text
  , pre5_race_bango text
  , pre6_kaisai_nen text
  , pre6_kaisai_gappi text
  , pre6_keibajo_code text
  , pre6_race_bango text
  , pre7_kaisai_nen text
  , pre7_kaisai_gappi text
  , pre7_keibajo_code text
  , pre7_race_bango text
  , primary key (ketto_toroku_bango, kaisai_nen, kaisai_gappi, keibajo_code, race_bango)
);

CREATE MATERIALIZED VIEW public.jockey AS 
SELECT nur.kishumei_ryakusho,
    ''::bpchar AS keibajo_code,
    ''::bpchar AS track_code,
    ''::bpchar AS kyori,
    round((((count(((nur.kakutei_chakujun <= '02'::bpchar) OR NULL::boolean)))::numeric * 100.0) / (count(*))::numeric), 1) AS jockey_rate
   FROM (umagoto_race_joho nur
     JOIN race_shosai nr ON (((nr.kaisai_nen = nur.kaisai_nen) AND (nr.kaisai_gappi = nur.kaisai_gappi) AND (nr.keibajo_code = nur.keibajo_code) AND (nr.race_bango = nur.race_bango))))
  WHERE ((nur.kaisai_nen >= '2010'::bpchar) AND (nur.keibajo_code >= '01'::bpchar) AND (nur.keibajo_code <= '10'::bpchar) AND (nr.track_code < '30'::bpchar) AND (nur.kakutei_chakujun > '00'::bpchar))
  GROUP BY nur.kishumei_ryakusho
UNION
 SELECT nur.kishumei_ryakusho,
    nr.keibajo_code,
    nr.track_code,
    nr.kyori,
    round((((count(((nur.kakutei_chakujun <= '02'::bpchar) OR NULL::boolean)))::numeric * 100.0) / (count(*))::numeric), 1) AS jockey_rate
   FROM (umagoto_race_joho nur
     JOIN race_shosai nr ON (((nr.kaisai_nen = nur.kaisai_nen) AND (nr.kaisai_gappi = nur.kaisai_gappi) AND (nr.keibajo_code = nur.keibajo_code) AND (nr.race_bango = nur.race_bango))))
  WHERE ((nur.kaisai_nen >= '2010'::bpchar) AND (nur.keibajo_code >= '01'::bpchar) AND (nur.keibajo_code <= '10'::bpchar) AND (nr.track_code < '30'::bpchar) AND (nur.kakutei_chakujun > '00'::bpchar))
  GROUP BY nur.kishumei_ryakusho, nr.keibajo_code, nr.track_code, nr.kyori

CREATE MATERIALIZED VIEW public.sire AS 
SELECT nu.ketto1_bamei,
    ''::bpchar AS keibajo_code,
    ''::bpchar AS track_code,
    ''::bpchar AS kyori,
    round((((count(((nur.kakutei_chakujun <= '02'::bpchar) OR NULL::boolean)))::numeric * 100.0) / (count(*))::numeric), 1) AS sire_rate
   FROM ((umagoto_race_joho nur
     JOIN race_shosai nr ON (((nr.kaisai_nen = nur.kaisai_nen) AND (nr.kaisai_gappi = nur.kaisai_gappi) AND (nr.keibajo_code = nur.keibajo_code) AND (nr.race_bango = nur.race_bango))))
     JOIN kyosoba_master2 nu ON ((nur.ketto_toroku_bango = nu.ketto_toroku_bango)))
  WHERE ((nur.kaisai_nen >= '2010'::bpchar) AND (nur.keibajo_code >= '01'::bpchar) AND (nur.keibajo_code <= '10'::bpchar) AND (nr.track_code < '30'::bpchar) AND (nur.kakutei_chakujun > '00'::bpchar))
  GROUP BY nu.ketto1_bamei
UNION
 SELECT nu.ketto1_bamei,
    nr.keibajo_code,
    nr.track_code,
    nr.kyori,
    round((((count(((nur.kakutei_chakujun <= '02'::bpchar) OR NULL::boolean)))::numeric * 100.0) / (count(*))::numeric), 1) AS sire_rate
   FROM ((umagoto_race_joho nur
     JOIN race_shosai nr ON (((nr.kaisai_nen = nur.kaisai_nen) AND (nr.kaisai_gappi = nur.kaisai_gappi) AND (nr.keibajo_code = nur.keibajo_code) AND (nr.race_bango = nur.race_bango))))
     JOIN kyosoba_master2 nu ON ((nur.ketto_toroku_bango = nu.ketto_toroku_bango)))
  WHERE ((nur.kaisai_nen >= '2010'::bpchar) AND (nur.keibajo_code >= '01'::bpchar) AND (nur.keibajo_code <= '10'::bpchar) AND (nr.track_code < '30'::bpchar) AND (nur.kakutei_chakujun > '00'::bpchar))
  GROUP BY nu.ketto1_bamei, nr.keibajo_code, nr.track_code, nr.kyori

