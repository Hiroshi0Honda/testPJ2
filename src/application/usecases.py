"""
ユースケース

アプリケーションの主要なビジネスロジックを実装
"""

import logging
from typing import List, Dict, Any
import os

from src.domain.entities import (
    RaceInfo, HorseRaceInfo, PreviousRaceInfo, 
    FeatureData, PredictionResult
)
from src.domain.repositories import RaceRepository, ModelRepository, DataRepository
from src.domain.services import (
    FeatureEngineeringService, DataSplitService, 
    ModelTrainingService, EvaluationService
)
from src.application.services import ModelTrainingServiceImpl

logger = logging.getLogger(__name__)


class HorseRacingAnalysisUseCase:
    """競馬分析ユースケース"""
    
    def __init__(
        self,
        race_repository: RaceRepository,
        model_repository: ModelRepository,
        data_repository: DataRepository,
        feature_engineering_service: FeatureEngineeringService,
        data_split_service: DataSplitService,
        model_training_service: ModelTrainingService,
        evaluation_service: EvaluationService
    ):
        """
        初期化
        
        Args:
            race_repository: レース情報リポジトリ
            model_repository: モデルリポジトリ
            data_repository: データリポジトリ
            feature_engineering_service: 特徴量エンジニアリングサービス
            data_split_service: データ分割サービス
            model_training_service: モデル学習サービス
            evaluation_service: 評価サービス
        """
        self.race_repository = race_repository
        self.model_repository = model_repository
        self.data_repository = data_repository
        self.feature_engineering_service = feature_engineering_service
        self.data_split_service = data_split_service
        self.model_training_service = model_training_service
        self.evaluation_service = evaluation_service
    
    def execute_analysis(self) -> Dict[str, Any]:
        """
        競馬分析を実行する
        
        Returns:
            分析結果の辞書
        """
        try:
            logger.info("競馬分析を開始します")
            
            # 1. データ取得
            logger.info("データ取得を開始します")
            race_data = self._fetch_race_data()
            horse_race_data = self._fetch_horse_race_data(race_data)
            previous_race_data = self._fetch_previous_race_data(horse_race_data)
            
            # 2. 特徴量データ作成
            logger.info("特徴量データ作成を開始します")
            feature_data = self._create_feature_data(race_data, horse_race_data, previous_race_data)
            
            # 3. データ分割
            logger.info("データ分割を開始します")
            train_data, validation_data = self.data_split_service.split_train_validation(feature_data)
            
            # 4. モデル学習
            logger.info("モデル学習を開始します")
            model = self._train_model(train_data, validation_data)
            
            # 5. モデル保存
            logger.info("モデル保存を開始します")
            model_path = os.path.join("models", "horse_racing_model.keras")
            self.model_repository.save_model(model, model_path)
            
            # 6. 検証と結果出力
            logger.info("検証と結果出力を開始します")
            results = self._evaluate_and_output_results(model, validation_data)
            
            logger.info("競馬分析が完了しました")
            return results
            
        except Exception as e:
            logger.error(f"競馬分析の実行に失敗しました: {e}")
            raise
    
    def _fetch_race_data(self) -> List[RaceInfo]:
        """レース情報を取得する"""
        return self.race_repository.get_race_data(start_year=2019, end_year=2024)
    
    def _fetch_horse_race_data(self, race_data: List[RaceInfo]) -> List[HorseRaceInfo]:
        """馬ごとレース情報を取得する"""
        race_ids = [race.race_id for race in race_data]
        return self.race_repository.get_horse_race_data(race_ids)
    
    def _fetch_previous_race_data(self, horse_race_data: List[HorseRaceInfo]) -> List[PreviousRaceInfo]:
        """前走ID情報を取得する"""
        ketto_toroku_bangos = list(set([horse.ketto_toroku_bango for horse in horse_race_data]))
        return self.race_repository.get_previous_race_data(ketto_toroku_bangos)
    
    def _create_feature_data(
        self, 
        race_data: List[RaceInfo], 
        horse_race_data: List[HorseRaceInfo], 
        previous_race_data: List[PreviousRaceInfo]
    ) -> List[FeatureData]:
        """特徴量データを作成する"""
        feature_data_list = []
        
        # レースIDでグループ化
        race_dict = {race.race_id: race for race in race_data}
        horse_dict = {}
        for horse in horse_race_data:
            if horse.race_id not in horse_dict:
                horse_dict[horse.race_id] = []
            horse_dict[horse.race_id].append(horse)
        
        # 前走情報を辞書化
        previous_dict = {}
        for prev in previous_race_data:
            if prev.race_id not in previous_dict:
                previous_dict[prev.race_id] = {}
            previous_dict[prev.race_id][prev.ketto_toroku_bango] = prev
        
        # 各レースの特徴量データを作成
        for race_id, race_info in race_dict.items():
            if race_id in horse_dict:
                horses = horse_dict[race_id]
                
                # 前走情報を取得
                previous_races = {}
                for horse in horses:
                    if race_id in previous_dict and horse.ketto_toroku_bango in previous_dict[race_id]:
                        prev_info = previous_dict[race_id][horse.ketto_toroku_bango]
                        # 前走情報を取得（簡略化のため空のリストを設定）
                        previous_races[horse.horse_id] = []
                
                feature_data = FeatureData(
                    race_id=race_id,
                    race_info=race_info,
                    horses=horses,
                    previous_races=previous_races
                )
                feature_data_list.append(feature_data)
        
        logger.info(f"特徴量データを{len(feature_data_list)}件作成しました")
        return feature_data_list
    
    def _train_model(
        self, 
        train_data: List[FeatureData], 
        validation_data: List[FeatureData]
    ) -> Any:
        """モデルを学習する"""
        # 特徴量サイズを計算（簡略化のため固定値を使用）
        feature_size = 7 + (18 * 9)  # レース情報7 + 馬の情報18頭分×9項目
        
        # モデル学習サービスを初期化
        training_service = ModelTrainingServiceImpl(feature_size)
        
        return training_service.train_model(train_data, validation_data)
    
    def _evaluate_and_output_results(
        self, 
        model: Any, 
        validation_data: List[FeatureData]
    ) -> Dict[str, Any]:
        """検証と結果出力を実行する"""
        # 予測実行
        predictions = self._predict_validation_data(model, validation_data)
        
        # 評価指標を計算
        accuracy = self.evaluation_service.calculate_accuracy(predictions)
        
        # 相関を計算
        predicted_probabilities = [p.predicted_win_probability for p in predictions]
        actual_orders = [p.actual_race_order for p in predictions]
        correlation_coef = self.evaluation_service.calculate_correlation(
            predicted_probabilities, actual_orders
        )
        
        # 順位相関を計算
        predicted_ranks = [p.predicted_rank for p in predictions]
        rank_correlation = self.evaluation_service.calculate_rank_correlation(
            predicted_ranks, actual_orders
        )
        
        # 結果をCSVに出力
        results_data = [
            {
                'race_id': p.race_id,
                'horse_id': p.horse_id,
                'predicted_win_probability': p.predicted_win_probability,
                'actual_race_order': p.actual_race_order,
                'odds': p.odds,
                'predicted_rank': p.predicted_rank
            }
            for p in predictions
        ]
        
        csv_path = os.path.join("data", "prediction_results.csv")
        self.data_repository.save_prediction_results(results_data, csv_path)
        
        # 結果を返す
        return {
            'accuracy': accuracy,
            'correlation': correlation_coef,
            'rank_correlation': rank_correlation,
            'total_predictions': len(predictions),
            'csv_path': csv_path
        }
    
    def _predict_validation_data(
        self, 
        model: Any, 
        validation_data: List[FeatureData]
    ) -> List[PredictionResult]:
        """検証データで予測を実行する"""
        
        # モデルを使って予測確率を取得（正規化済み）
        predicted_probabilities = self.model_training_service.predict_win_probabilities(
            model, validation_data
        )
        
        predictions = []
        prob_index = 0
        for feature_data in validation_data:
            horse_predictions = []
            
            for horse in feature_data.horses:
                if prob_index < len(predicted_probabilities):
                    prediction = PredictionResult(
                        race_id=feature_data.race_id,
                        horse_id=horse.horse_id,
                        predicted_win_probability=predicted_probabilities[prob_index],
                        actual_race_order=horse.race_order,
                        odds=horse.odds,
                        predicted_rank=0  # 後で設定
                    )
                    horse_predictions.append(prediction)
                    prob_index += 1
            
            # 予測順位を設定
            horse_predictions.sort(key=lambda x: x.predicted_win_probability, reverse=True)
            for i, pred in enumerate(horse_predictions):
                pred.predicted_rank = i + 1
            
            predictions.extend(horse_predictions)
        
        return predictions 