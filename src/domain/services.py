"""
ドメインサービス

ビジネスロジックを実装するサービス
"""

from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Any
import numpy as np
from .entities import RaceInfo, HorseRaceInfo, PreviousRaceInfo, FeatureData, PredictionResult


class FeatureEngineeringService(ABC):
    """特徴量エンジニアリングサービス"""
    
    @abstractmethod
    def create_feature_data(
        self, 
        race_info: RaceInfo, 
        horses: List[HorseRaceInfo], 
        previous_races: Dict[str, List[Dict[str, Any]]]
    ) -> np.ndarray:
        """特徴量データを作成する"""
        pass
    
    @abstractmethod
    def normalize_features(self, features: np.ndarray) -> np.ndarray:
        """特徴量を正規化する"""
        pass


class DataSplitService(ABC):
    """データ分割サービス"""
    
    @abstractmethod
    def split_train_validation(
        self, 
        feature_data: List[FeatureData], 
        train_ratio: float = 0.8
    ) -> Tuple[List[FeatureData], List[FeatureData]]:
        """学習データと検証データに分割する"""
        pass


class ModelTrainingService(ABC):
    """モデル学習サービス"""
    
    @abstractmethod
    def train_model(
        self, 
        train_data: List[FeatureData], 
        validation_data: List[FeatureData]
    ) -> Any:
        """Transformerモデルを学習する"""
        pass
    
    @abstractmethod
    def predict_win_probabilities(self, model: Any, data: List[FeatureData]) -> List[float]:
        """勝率を予測する"""
        pass


class EvaluationService(ABC):
    """評価サービス"""
    
    @abstractmethod
    def calculate_accuracy(self, predictions: List[PredictionResult]) -> float:
        """予測精度を計算する"""
        pass
    
    @abstractmethod
    def calculate_correlation(
        self, 
        predicted_probabilities: List[float], 
        actual_orders: List[int]
    ) -> float:
        """予測勝率と実際の着順の相関を計算する"""
        pass
    
    @abstractmethod
    def calculate_rank_correlation(
        self, 
        predicted_ranks: List[int], 
        actual_orders: List[int]
    ) -> float:
        """予測順位と実際の着順の相関を計算する"""
        pass 