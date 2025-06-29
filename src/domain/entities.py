"""
ドメインエンティティ

競馬データ分析におけるビジネスエンティティを定義
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from datetime import datetime


@dataclass
class RaceInfo:
    """レース情報エンティティ"""
    race_id: str
    keibajo_code: str
    track_code: str
    kyori: int
    babacd: int
    tosu: int
    grade_code: int
    mu: float


@dataclass
class HorseRaceInfo:
    """馬ごとレース情報エンティティ"""
    race_id: str
    ketto_toroku_bango: str
    horse_id: str
    umaban: int
    ketto1_bamei: str
    kisyu_id: str
    odds: float
    ninki: int
    bataiju: int
    batai_zogen: int
    futan: float
    sire_rate: float
    sire_joken_rate: float
    jockey_rate: float
    hensa: float
    rate_diff: float
    race_order: int
    soha_time: int
    kohan_3f: int
    corner1: int
    corner2: int
    corner3: int
    corner4: int


@dataclass
class PreviousRaceInfo:
    """前走ID情報エンティティ"""
    ketto_toroku_bango: str
    race_id: str
    pre1_race_id: Optional[str]
    pre2_race_id: Optional[str]
    pre3_race_id: Optional[str]
    pre4_race_id: Optional[str]
    pre5_race_id: Optional[str]


@dataclass
class FeatureData:
    """特徴量データエンティティ"""
    race_id: str
    race_info: RaceInfo
    horses: List[HorseRaceInfo]
    previous_races: Dict[str, List[Dict[str, Any]]]  # horse_id -> [previous_race_data]


@dataclass
class PredictionResult:
    """予測結果エンティティ"""
    race_id: str
    horse_id: str
    predicted_win_probability: float
    actual_race_order: int
    odds: float
    predicted_rank: int 