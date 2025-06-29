"""
依存性注入設定

アプリケーションの依存関係を管理
"""

import os
import logging
from typing import Dict, Any

from db.connector import get_connection
from src.infrastructure.database import PostgresRaceRepository
from src.infrastructure.storage import FileModelRepository, CsvDataRepository
from src.application.services import (
    FeatureEngineeringServiceImpl, DataSplitServiceImpl, 
    ModelTrainingServiceImpl, EvaluationServiceImpl
)
from src.application.usecases import HorseRacingAnalysisUseCase

logger = logging.getLogger(__name__)


class DatabaseConnector:
    """データベースコネクタのラッパークラス"""
    
    def __init__(self):
        """初期化"""
        pass
    
    def get_connection(self):
        """データベース接続を取得する"""
        return get_connection()
    
    def close_connection(self):
        """接続を閉じる（この実装では何もしない）"""
        pass


class DependencyContainer:
    """依存性注入コンテナ"""
    
    def __init__(self):
        """初期化"""
        self._services: Dict[str, Any] = {}
        self._configure_services()
    
    def _configure_services(self):
        """サービスの設定"""
        try:
            # データベースコネクタ
            self._services['database_connector'] = DatabaseConnector()
            
            # リポジトリ
            self._services['race_repository'] = PostgresRaceRepository(
                self._services['database_connector']
            )
            self._services['model_repository'] = FileModelRepository()
            self._services['data_repository'] = CsvDataRepository()
            
            # アプリケーションサービス
            self._services['feature_engineering_service'] = FeatureEngineeringServiceImpl()
            self._services['data_split_service'] = DataSplitServiceImpl()
            self._services['evaluation_service'] = EvaluationServiceImpl()
            
            # ユースケース
            self._services['horse_racing_analysis_usecase'] = HorseRacingAnalysisUseCase(
                race_repository=self._services['race_repository'],
                model_repository=self._services['model_repository'],
                data_repository=self._services['data_repository'],
                feature_engineering_service=self._services['feature_engineering_service'],
                data_split_service=self._services['data_split_service'],
                model_training_service=None,  # 動的に設定
                evaluation_service=self._services['evaluation_service']
            )
            
            logger.info("依存性注入の設定が完了しました")
            
        except Exception as e:
            logger.error(f"依存性注入の設定に失敗しました: {e}")
            raise
    
    def get_service(self, service_name: str) -> Any:
        """
        サービスを取得する
        
        Args:
            service_name: サービス名
            
        Returns:
            サービスインスタンス
        """
        if service_name not in self._services:
            raise KeyError(f"サービス '{service_name}' が見つかりません")
        
        return self._services[service_name]
    
    def set_model_training_service(self, feature_size: int):
        """
        モデル学習サービスを設定する
        
        Args:
            feature_size: 特徴量サイズ
        """
        from src.application.services import ModelTrainingServiceImpl
        
        self._services['model_training_service'] = ModelTrainingServiceImpl(feature_size)
        
        # ユースケースのモデル学習サービスを更新
        self._services['horse_racing_analysis_usecase'].model_training_service = \
            self._services['model_training_service']
    
    def cleanup(self):
        """リソースのクリーンアップ"""
        try:
            if 'database_connector' in self._services:
                self._services['database_connector'].close_connection()
            logger.info("リソースのクリーンアップが完了しました")
        except Exception as e:
            logger.error(f"リソースのクリーンアップに失敗しました: {e}")


# グローバルインスタンス
container = DependencyContainer() 