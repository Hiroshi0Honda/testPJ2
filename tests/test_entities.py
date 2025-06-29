"""
エンティティのテスト

ドメインエンティティの単体テスト
"""

import pytest
from src.domain.entities import (
    RaceInfo, HorseRaceInfo, PreviousRaceInfo, 
    FeatureData, PredictionResult
)


class TestRaceInfo:
    """RaceInfoエンティティのテスト"""
    
    def test_race_info_creation(self):
        """RaceInfoの作成テスト"""
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
        
        assert race_info.race_id == "202401010101"
        assert race_info.keibajo_code == "01"
        assert race_info.track_code == "01"
        assert race_info.kyori == 1600
        assert race_info.babacd == 1
        assert race_info.tosu == 16
        assert race_info.grade_code == 5
        assert race_info.mu == 85.5


class TestHorseRaceInfo:
    """HorseRaceInfoエンティティのテスト"""
    
    def test_horse_race_info_creation(self):
        """HorseRaceInfoの作成テスト"""
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
        
        assert horse_info.race_id == "202401010101"
        assert horse_info.ketto_toroku_bango == "1234567890"
        assert horse_info.horse_id == "テスト馬"
        assert horse_info.umaban == 1
        assert horse_info.odds == 3.5
        assert horse_info.race_order == 1


class TestPreviousRaceInfo:
    """PreviousRaceInfoエンティティのテスト"""
    
    def test_previous_race_info_creation(self):
        """PreviousRaceInfoの作成テスト"""
        prev_info = PreviousRaceInfo(
            ketto_toroku_bango="1234567890",
            race_id="202401010101",
            pre1_race_id="202312010101",
            pre2_race_id="202311010101",
            pre3_race_id="202310010101",
            pre4_race_id="202309010101",
            pre5_race_id="202308010101"
        )
        
        assert prev_info.ketto_toroku_bango == "1234567890"
        assert prev_info.race_id == "202401010101"
        assert prev_info.pre1_race_id == "202312010101"
        assert prev_info.pre5_race_id == "202308010101"
    
    def test_previous_race_info_with_none(self):
        """None値を含むPreviousRaceInfoの作成テスト"""
        prev_info = PreviousRaceInfo(
            ketto_toroku_bango="1234567890",
            race_id="202401010101",
            pre1_race_id=None,
            pre2_race_id="202311010101",
            pre3_race_id=None,
            pre4_race_id="202309010101",
            pre5_race_id=None
        )
        
        assert prev_info.pre1_race_id is None
        assert prev_info.pre2_race_id == "202311010101"
        assert prev_info.pre3_race_id is None


class TestFeatureData:
    """FeatureDataエンティティのテスト"""
    
    def test_feature_data_creation(self):
        """FeatureDataの作成テスト"""
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
        
        feature_data = FeatureData(
            race_id="202401010101",
            race_info=race_info,
            horses=[horse_info],
            previous_races={"テスト馬": []}
        )
        
        assert feature_data.race_id == "202401010101"
        assert feature_data.race_info == race_info
        assert len(feature_data.horses) == 1
        assert feature_data.horses[0] == horse_info
        assert "テスト馬" in feature_data.previous_races


class TestPredictionResult:
    """PredictionResultエンティティのテスト"""
    
    def test_prediction_result_creation(self):
        """PredictionResultの作成テスト"""
        prediction = PredictionResult(
            race_id="202401010101",
            horse_id="テスト馬",
            predicted_win_probability=0.25,
            actual_race_order=1,
            odds=3.5,
            predicted_rank=1
        )
        
        assert prediction.race_id == "202401010101"
        assert prediction.horse_id == "テスト馬"
        assert prediction.predicted_win_probability == 0.25
        assert prediction.actual_race_order == 1
        assert prediction.odds == 3.5
        assert prediction.predicted_rank == 1 