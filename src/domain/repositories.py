"""
リポジトリインターフェース

データアクセス層の抽象化
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .entities import RaceInfo, HorseRaceInfo, PreviousRaceInfo


class RaceRepository(ABC):
    """レース情報リポジトリインターフェース"""
    
    @abstractmethod
    def get_race_data(self, start_year: int = 2019, end_year: int = 2024) -> List[RaceInfo]:
        """レース情報を取得する"""
        pass
    
    @abstractmethod
    def get_horse_race_data(self, race_ids: List[str]) -> List[HorseRaceInfo]:
        """馬ごとレース情報を取得する"""
        pass
    
    @abstractmethod
    def get_previous_race_data(self, ketto_toroku_bangos: List[str]) -> List[PreviousRaceInfo]:
        """前走ID情報を取得する"""
        pass


class ModelRepository(ABC):
    """モデル保存・読み込みリポジトリインターフェース"""
    
    @abstractmethod
    def save_model(self, model: Any, filepath: str) -> None:
        """モデルを保存する"""
        pass
    
    @abstractmethod
    def load_model(self, filepath: str) -> Any:
        """モデルを読み込む"""
        pass


class DataRepository(ABC):
    """データ出力リポジトリインターフェース"""
    
    @abstractmethod
    def save_prediction_results(self, results: List[Dict[str, Any]], filepath: str) -> None:
        """予測結果をCSVファイルに保存する"""
        pass 