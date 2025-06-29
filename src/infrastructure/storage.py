"""
ストレージ層

モデル保存・読み込みとデータ出力を実装
"""

import os
import logging
from typing import List, Dict, Any
import pandas as pd
import pickle
import json

from src.domain.repositories import ModelRepository, DataRepository

logger = logging.getLogger(__name__)


class FileModelRepository(ModelRepository):
    """ファイルベースモデルリポジトリ実装"""
    
    def save_model(self, model: Any, filepath: str) -> None:
        """
        モデルを保存する
        
        Args:
            model: 保存するモデル
            filepath: 保存先ファイルパス
        """
        try:
            # ディレクトリが存在しない場合は作成
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # Kerasモデルの場合はsaveを使用
            if hasattr(model, 'save'):
                model.save(filepath)
                logger.info(f"モデルを保存しました: {filepath}")
            else:
                # その他の場合はpickleで保存
                with open(filepath, 'wb') as f:
                    pickle.dump(model, f)
                logger.info(f"モデルを保存しました: {filepath}")
                
        except Exception as e:
            logger.error(f"モデルの保存に失敗しました: {e}")
            raise
    
    def load_model(self, filepath: str) -> Any:
        """
        モデルを読み込む
        
        Args:
            filepath: モデルファイルパス
            
        Returns:
            読み込んだモデル
        """
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"モデルファイルが見つかりません: {filepath}")
            
            # Kerasモデルの場合はload_weightsを使用
            if filepath.endswith('.h5') or filepath.endswith('.keras'):
                from tensorflow import keras
                model = keras.models.load_model(filepath)
            else:
                # その他の場合はpickleで読み込み
                with open(filepath, 'rb') as f:
                    model = pickle.load(f)
            
            logger.info(f"モデルを読み込みました: {filepath}")
            return model
            
        except Exception as e:
            logger.error(f"モデルの読み込みに失敗しました: {e}")
            raise


class CsvDataRepository(DataRepository):
    """CSVデータ出力リポジトリ実装"""
    
    def save_prediction_results(self, results: List[Dict[str, Any]], filepath: str) -> None:
        """
        予測結果をCSVファイルに保存する
        
        Args:
            results: 予測結果のリスト
            filepath: 保存先ファイルパス
        """
        try:
            # ディレクトリが存在しない場合は作成
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # DataFrameに変換
            df = pd.DataFrame(results)
            
            # CSVファイルに保存
            df.to_csv(filepath, index=False, encoding='utf-8-sig')
            
            logger.info(f"予測結果を保存しました: {filepath}")
            
        except Exception as e:
            logger.error(f"予測結果の保存に失敗しました: {e}")
            raise 