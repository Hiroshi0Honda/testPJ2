"""
データベースアクセス層

PostgreSQLデータベースからのデータ取得を実装
"""

import sys
import os
import logging
from typing import List, Dict, Any
import pandas as pd

# プロジェクトルートをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from db.connector import get_connection, fetch_query_from_file
from src.domain.entities import RaceInfo, HorseRaceInfo, PreviousRaceInfo
from src.domain.repositories import RaceRepository

logger = logging.getLogger(__name__)


class PostgresRaceRepository(RaceRepository):
    """PostgreSQLレース情報リポジトリ実装"""
    
    def __init__(self, connector):
        """
        初期化
        
        Args:
            connector: データベースコネクタ
        """
        self.connector = connector
    
    def get_race_data(self, start_year: int = 2019, end_year: int = 2024) -> List[RaceInfo]:
        """
        レース情報を取得する
        
        Args:
            start_year: 開始年
            end_year: 終了年
            
        Returns:
            レース情報のリスト
        """
        try:
            # SQLファイルを読み込み
            sql_path = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'get_race_data.sql')
            with open(sql_path, 'r', encoding='utf-8') as f:
                sql = f.read()
            
            # 年でフィルタリング
            sql = sql.replace(':start_year', str(start_year))
            sql = sql.replace(':end_year', str(end_year))
            
            # データベースから取得
            df = pd.read_sql(sql, get_connection())
            
            # エンティティに変換
            race_info_list = []
            for _, row in df.iterrows():
                race_info = RaceInfo(
                    race_id=str(row['race_id']),
                    keibajo_code=str(row['keibajo_code']),
                    track_code=str(row['track_code']),
                    kyori=int(row['kyori']),
                    babacd=int(row['babacd']),
                    tosu=int(row['tosu']),
                    grade_code=int(row['grade_code']),
                    mu=float(row['mu'])
                )
                race_info_list.append(race_info)
            
            logger.info(f"レース情報を{len(race_info_list)}件取得しました")
            return race_info_list
            
        except Exception as e:
            logger.error(f"レース情報の取得に失敗しました: {e}")
            raise
    
    def get_horse_race_data(self, race_ids: List[str]) -> List[HorseRaceInfo]:
        """
        馬ごとレース情報を取得する
        
        Args:
            race_ids: レースIDのリスト
            
        Returns:
            馬ごとレース情報のリスト
        """
        try:
            # SQLファイルを読み込み
            sql_path = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'get_umagoto_race.sql')
            with open(sql_path, 'r', encoding='utf-8') as f:
                sql = f.read()
            
            # レースIDでフィルタリング
            race_ids_str = "','".join(race_ids)
            sql = sql.replace(':race_ids', f"'{race_ids_str}'")
            
            # データベースから取得
            df = pd.read_sql(sql, get_connection())
            
            # エンティティに変換
            horse_race_info_list = []
            for _, row in df.iterrows():
                horse_race_info = HorseRaceInfo(
                    race_id=str(row['race_id']),
                    ketto_toroku_bango=str(row['ketto_toroku_bango']),
                    horse_id=str(row['horse_id']),
                    umaban=int(row['umaban']),
                    ketto1_bamei=str(row['ketto1_bamei']),
                    kisyu_id=str(row['kisyu_id']),
                    odds=float(row['odds']),
                    ninki=int(row['ninki']),
                    bataiju=int(row['bataiju']),
                    batai_zogen=int(row['batai_zogen']),
                    futan=float(row['futan']),
                    sire_rate=float(row['sire_rate']),
                    sire_joken_rate=float(row['sire_joken_rate']),
                    jockey_rate=float(row['jockey_rate']),
                    hensa=float(row['hensa']),
                    rate_diff=float(row['rate_diff']),
                    race_order=int(row['race_order']),
                    soha_time=int(row['soha_time']),
                    kohan_3f=int(row['kohan_3f']),
                    corner1=int(row['corner1']),
                    corner2=int(row['corner2']),
                    corner3=int(row['corner3']),
                    corner4=int(row['corner4'])
                )
                horse_race_info_list.append(horse_race_info)
            
            logger.info(f"馬ごとレース情報を{len(horse_race_info_list)}件取得しました")
            return horse_race_info_list
            
        except Exception as e:
            logger.error(f"馬ごとレース情報の取得に失敗しました: {e}")
            raise
    
    def get_previous_race_data(self, ketto_toroku_bangos: List[str]) -> List[PreviousRaceInfo]:
        """
        前走ID情報を取得する
        
        Args:
            ketto_toroku_bangos: 血統登録番号のリスト
            
        Returns:
            前走ID情報のリスト
        """
        try:
            # SQLファイルを読み込み
            sql_path = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'get_zensou_id.sql')
            with open(sql_path, 'r', encoding='utf-8') as f:
                sql = f.read()
            
            # 血統登録番号でフィルタリング
            ketto_str = "','".join(ketto_toroku_bangos)
            sql = sql.replace(':ketto_toroku_bangos', f"'{ketto_str}'")
            
            # データベースから取得
            df = pd.read_sql(sql, get_connection())
            
            # エンティティに変換
            previous_race_info_list = []
            for _, row in df.iterrows():
                previous_race_info = PreviousRaceInfo(
                    ketto_toroku_bango=str(row['ketto_toroku_bango']),
                    race_id=str(row['race_id']),
                    pre1_race_id=str(row['pre1_race_id']) if pd.notna(row['pre1_race_id']) else None,
                    pre2_race_id=str(row['pre2_race_id']) if pd.notna(row['pre2_race_id']) else None,
                    pre3_race_id=str(row['pre3_race_id']) if pd.notna(row['pre3_race_id']) else None,
                    pre4_race_id=str(row['pre4_race_id']) if pd.notna(row['pre4_race_id']) else None,
                    pre5_race_id=str(row['pre5_race_id']) if pd.notna(row['pre5_race_id']) else None
                )
                previous_race_info_list.append(previous_race_info)
            
            logger.info(f"前走ID情報を{len(previous_race_info_list)}件取得しました")
            return previous_race_info_list
            
        except Exception as e:
            logger.error(f"前走ID情報の取得に失敗しました: {e}")
            raise 