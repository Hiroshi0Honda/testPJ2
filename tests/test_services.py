"""
サービスのテスト

アプリケーションサービスの単体テスト
"""

import pytest
import numpy as np
from unittest.mock import Mock, patch
from src.domain.entities import (
    RaceInfo, HorseRaceInfo, FeatureData, PredictionResult
)
from src.application.services import (
    FeatureEngineeringServiceImpl, DataSplitServiceImpl, 
    ModelTrainingServiceImpl, EvaluationServiceImpl
)


class TestFeatureEngineeringServiceImpl:
    """FeatureEngineeringServiceImplのテスト"""
    
    def setup_method(self):
        """テスト前の準備"""
        self.service = FeatureEngineeringServiceImpl()
    
    def test_create_feature_data(self):
        """特徴量データ作成のテスト"""
        # テストデータを作成
        race_info = RaceInfo(
            race_id="202401010101",
            keibajo_code="01",
            track_code="01",
            kyori=1600,
            babacd=1,
            tosu=16,
            grade_code=5,
            mu=85.5
        )
        
        horse_info = HorseRaceInfo(
            race_id="202401010101",
            ketto_toroku_bango="1234567890",
            horse_id="テスト馬",
            umaban=1,
            ketto1_bamei="テスト父",
            kisyu_id="テスト騎手",
            odds=3.5,
            ninki=1,
            bataiju=450,
            batai_zogen=2,
            futan=55.0,
            sire_rate=0.15,
            sire_joken_rate=0.12,
            jockey_rate=0.18,
            hensa=65.5,
            rate_diff=5.0,
            race_order=1,
            soha_time=648,
            kohan_3f=341,
            corner1=1,
            corner2=1,
            corner3=1,
            corner4=1
        )
        
        previous_races = {"テスト馬": []}
        
        # 特徴量データを作成
        features = self.service.create_feature_data(race_info, [horse_info], previous_races)
        
        # 結果を検証
        assert isinstance(features, np.ndarray)
        assert features.dtype == np.float32
        assert len(features) > 0
    
    def test_normalize_features(self):
        """特徴量正規化のテスト"""
        # テストデータ
        features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float32)
        
        # 正規化
        normalized = self.service.normalize_features(features)
        
        # 結果を検証
        assert isinstance(normalized, np.ndarray)
        assert normalized.shape == features.shape


class TestDataSplitServiceImpl:
    """DataSplitServiceImplのテスト"""
    
    def setup_method(self):
        """テスト前の準備"""
        self.service = DataSplitServiceImpl()
    
    def test_split_train_validation(self):
        """データ分割のテスト"""
        # テストデータを作成
        feature_data = []
        for i in range(10):
            race_info = RaceInfo(
                race_id=f"20240101010{i}",
                keibajo_code="01",
                track_code="01",
                kyori=1600,
                babacd=1,
                tosu=16,
                grade_code=5,
                mu=85.5
            )
            
            feature_data.append(FeatureData(
                race_id=f"20240101010{i}",
                race_info=race_info,
                horses=[],
                previous_races={}
            ))
        
        # データ分割
        train_data, val_data = self.service.split_train_validation(feature_data, train_ratio=0.8)
        
        # 結果を検証
        assert len(train_data) + len(val_data) == len(feature_data)
        assert len(train_data) > 0
        assert len(val_data) > 0
        
        # 重複がないことを確認
        train_ids = {data.race_id for data in train_data}
        val_ids = {data.race_id for data in val_data}
        assert len(train_ids.intersection(val_ids)) == 0


class TestModelTrainingServiceImpl:
    """ModelTrainingServiceImplのテスト"""
    
    def setup_method(self):
        """テスト前の準備"""
        self.service = ModelTrainingServiceImpl(feature_size=169, max_horses=18)
    
    @patch('tensorflow.keras.models.Model')
    @patch('tensorflow.keras.Model.fit')
    def test_train_model(self, mock_fit, mock_model):
        """モデル学習のテスト"""
        # モックの設定
        mock_model.return_value = Mock()
        mock_fit.return_value = Mock()
        
        # テストデータを作成
        train_data = []
        val_data = []
        
        for i in range(5):
            race_info = RaceInfo(
                race_id=f"20240101010{i}",
                keibajo_code="01",
                track_code="01",
                kyori=1600,
                babacd=1,
                tosu=16,
                grade_code=5,
                mu=85.5
            )
            
            horse_info = HorseRaceInfo(
                race_id=f"20240101010{i}",
                ketto_toroku_bango="1234567890",
                horse_id="テスト馬",
                umaban=1,
                ketto1_bamei="テスト父",
                kisyu_id="テスト騎手",
                odds=3.5,
                ninki=1,
                bataiju=450,
                batai_zogen=2,
                futan=55.0,
                sire_rate=0.15,
                sire_joken_rate=0.12,
                jockey_rate=0.18,
                hensa=65.5,
                rate_diff=5.0,
                race_order=1,
                soha_time=648,
                kohan_3f=341,
                corner1=1,
                corner2=1,
                corner3=1,
                corner4=1
            )
            
            feature_data = FeatureData(
                race_id=f"20240101010{i}",
                race_info=race_info,
                horses=[horse_info],
                previous_races={}
            )
            
            if i < 4:
                train_data.append(feature_data)
            else:
                val_data.append(feature_data)
        
        # モデル学習（モックを使用）
        with patch('src.application.services.ModelTrainingServiceImpl._build_transformer_model') as mock_build:
            mock_build.return_value = Mock()
            model = self.service.train_model(train_data, val_data)
            
            # 結果を検証
            assert model is not None


class TestEvaluationServiceImpl:
    """EvaluationServiceImplのテスト"""
    
    def setup_method(self):
        """テスト前の準備"""
        self.service = EvaluationServiceImpl()
    
    def test_calculate_accuracy(self):
        """予測精度計算のテスト"""
        # テストデータを作成
        predictions = []
        
        # 正解の予測
        predictions.append(PredictionResult(
            race_id="202401010101",
            horse_id="テスト馬1",
            predicted_win_probability=0.8,
            actual_race_order=1,
            odds=3.5,
            predicted_rank=1
        ))
        
        # 不正解の予測
        predictions.append(PredictionResult(
            race_id="202401010101",
            horse_id="テスト馬2",
            predicted_win_probability=0.2,
            actual_race_order=2,
            odds=5.0,
            predicted_rank=2
        ))
        
        # 別レースの正解予測
        predictions.append(PredictionResult(
            race_id="202401010102",
            horse_id="テスト馬3",
            predicted_win_probability=0.9,
            actual_race_order=1,
            odds=2.0,
            predicted_rank=1
        ))
        
        # 精度を計算
        accuracy = self.service.calculate_accuracy(predictions)
        
        # 結果を検証
        assert isinstance(accuracy, float)
        assert 0.0 <= accuracy <= 1.0
    
    def test_calculate_correlation(self):
        """相関計算のテスト"""
        # テストデータ
        predicted_probabilities = [0.8, 0.6, 0.4, 0.2]
        actual_orders = [1, 2, 3, 4]
        
        # 相関を計算
        correlation = self.service.calculate_correlation(predicted_probabilities, actual_orders)
        
        # 結果を検証
        assert isinstance(correlation, float)
        assert -1.0 <= correlation <= 1.0
    
    def test_calculate_rank_correlation(self):
        """順位相関計算のテスト"""
        # テストデータ
        predicted_ranks = [1, 2, 3, 4]
        actual_orders = [1, 2, 3, 4]
        
        # 順位相関を計算
        rank_correlation = self.service.calculate_rank_correlation(predicted_ranks, actual_orders)
        
        # 結果を検証
        assert isinstance(rank_correlation, float)
        assert -1.0 <= rank_correlation <= 1.0 