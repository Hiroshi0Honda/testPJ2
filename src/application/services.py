"""
アプリケーションサービス

ビジネスロジックの実装
"""

import logging
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict, Any
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from src.domain.entities import (
    RaceInfo, HorseRaceInfo, PreviousRaceInfo, 
    FeatureData, PredictionResult
)
from src.domain.services import (
    FeatureEngineeringService, DataSplitService, 
    ModelTrainingService, EvaluationService
)

logger = logging.getLogger(__name__)


class FeatureEngineeringServiceImpl(FeatureEngineeringService):
    """特徴量エンジニアリングサービス実装"""
    
    def __init__(self):
        """初期化"""
        self.scaler = StandardScaler()
        self.max_horses = 18
        self.max_previous_races = 5
        
    def create_feature_data(
        self, 
        race_info: RaceInfo, 
        horses: List[HorseRaceInfo], 
        previous_races: Dict[str, List[Dict[str, Any]]]
    ) -> np.ndarray:
        """
        特徴量データを作成する
        
        Args:
            race_info: レース情報
            horses: 馬ごとレース情報のリスト
            previous_races: 前走情報の辞書
            
        Returns:
            特徴量データの配列
        """
        try:
            # レース情報の特徴量
            race_features = [
                int(race_info.keibajo_code),
                int(race_info.track_code),
                race_info.kyori,
                race_info.babacd,
                race_info.tosu,
                race_info.grade_code,
                race_info.mu
            ]
            
            # 馬の特徴量を固定長に調整
            horse_features_list = []
            for i in range(self.max_horses):
                if i < len(horses):
                    horse = horses[i]
                    horse_features = self._create_horse_features(horse, previous_races.get(horse.horse_id, []))
                else:
                    # 欠損データの補完
                    horse_features = [0] * self._get_horse_feature_size()
                
                horse_features_list.extend(horse_features)
            
            # 全特徴量を結合
            all_features = race_features + horse_features_list
            
            return np.array(all_features, dtype=np.float32)
            
        except Exception as e:
            logger.error(f"特徴量データの作成に失敗しました: {e}")
            raise
    
    def _create_horse_features(self, horse: HorseRaceInfo, previous_races: List[Dict[str, Any]]) -> List[float]:
        """
        馬の特徴量を作成する
        
        Args:
            horse: 馬のレース情報
            previous_races: 前走情報のリスト
            
        Returns:
            馬の特徴量リスト
        """
        # 基本特徴量
        basic_features = [
            horse.umaban,
            horse.odds,
            horse.ninki,
            horse.bataiju,
            horse.batai_zogen,
            horse.futan,
            horse.sire_rate,
            horse.sire_joken_rate,
            horse.jockey_rate,
            horse.hensa,
            horse.rate_diff,
            horse.race_order,
            horse.soha_time,
            horse.kohan_3f,
            horse.corner1,
            horse.corner2,
            horse.corner3,
            horse.corner4
        ]
        
        # 前走特徴量を固定長に調整
        previous_features = []
        for i in range(self.max_previous_races):
            if i < len(previous_races):
                prev_race = previous_races[i]
                prev_features = self._create_previous_race_features(prev_race)
            else:
                # 欠損データの補完
                prev_features = [0] * self._get_previous_race_feature_size()
            
            previous_features.extend(prev_features)
        
        return basic_features + previous_features
    
    def _create_previous_race_features(self, previous_race: Dict[str, Any]) -> List[float]:
        """
        前走の特徴量を作成する
        
        Args:
            previous_race: 前走情報
            
        Returns:
            前走の特徴量リスト
        """
        # 前走のレース情報と馬の情報を結合
        features = []
        
        # レース情報
        if 'race_info' in previous_race:
            race_info = previous_race['race_info']
            features.extend([
                int(race_info.keibajo_code),
                int(race_info.track_code),
                race_info.kyori,
                race_info.babacd,
                race_info.tosu,
                race_info.grade_code,
                race_info.mu
            ])
        else:
            features.extend([0] * 7)
        
        # 馬の情報
        if 'horse_info' in previous_race:
            horse_info = previous_race['horse_info']
            features.extend([
                horse_info.umaban,
                horse_info.odds,
                horse_info.ninki,
                horse_info.bataiju,
                horse_info.batai_zogen,
                horse_info.futan,
                horse_info.sire_rate,
                horse_info.sire_joken_rate,
                horse_info.jockey_rate,
                horse_info.hensa,
                horse_info.rate_diff,
                horse_info.race_order,
                horse_info.soha_time,
                horse_info.kohan_3f,
                horse_info.corner1,
                horse_info.corner2,
                horse_info.corner3,
                horse_info.corner4
            ])
        else:
            features.extend([0] * 18)
        
        return features
    
    def _get_horse_feature_size(self) -> int:
        """馬の特徴量サイズを取得"""
        return 18 + (self.max_previous_races * self._get_previous_race_feature_size())
    
    def _get_previous_race_feature_size(self) -> int:
        """前走の特徴量サイズを取得"""
        return 7 + 18  # レース情報7 + 馬の情報18
    
    def normalize_features(self, features: np.ndarray) -> np.ndarray:
        """
        特徴量を正規化する
        
        Args:
            features: 特徴量配列
            
        Returns:
            正規化された特徴量配列
        """
        try:
            return self.scaler.fit_transform(features)
        except Exception as e:
            logger.error(f"特徴量の正規化に失敗しました: {e}")
            raise


class DataSplitServiceImpl(DataSplitService):
    """データ分割サービス実装"""
    
    def split_train_validation(
        self, 
        feature_data: List[FeatureData], 
        train_ratio: float = 0.8
    ) -> Tuple[List[FeatureData], List[FeatureData]]:
        """
        学習データと検証データに分割する
        
        Args:
            feature_data: 特徴量データのリスト
            train_ratio: 学習データの割合
            
        Returns:
            学習データと検証データのタプル
        """
        try:
            # race_idで分割
            race_ids = [data.race_id for data in feature_data]
            train_ids, val_ids = train_test_split(
                race_ids, 
                train_size=train_ratio, 
                random_state=42
            )
            
            # データを分割
            train_data = [data for data in feature_data if data.race_id in train_ids]
            val_data = [data for data in feature_data if data.race_id in val_ids]
            
            logger.info(f"学習データ: {len(train_data)}件, 検証データ: {len(val_data)}件に分割しました")
            
            return train_data, val_data
            
        except Exception as e:
            logger.error(f"データ分割に失敗しました: {e}")
            raise


class ModelTrainingServiceImpl(ModelTrainingService):
    """モデル学習サービス実装"""
    
    def __init__(self, feature_size: int, max_horses: int = 18):
        """
        初期化
        
        Args:
            feature_size: 特徴量のサイズ
            max_horses: 最大馬数
        """
        self.feature_size = 15  # レース情報7 + 馬の情報8
        self.max_horses = max_horses
    
    def train_model(
        self, 
        train_data: List[FeatureData], 
        validation_data: List[FeatureData]
    ) -> Any:
        """
        Transformerモデルを学習する
        
        Args:
            train_data: 学習データ
            validation_data: 検証データ
            
        Returns:
            学習済みモデル
        """
        try:
            # データを準備
            X_train, y_train = self._prepare_data(train_data)
            X_val, y_val = self._prepare_data(validation_data)
            
            # モデルを構築
            model = self._build_transformer_model()
            
            # モデルを学習
            history = model.fit(
                X_train, y_train,
                validation_data=(X_val, y_val),
                epochs=50,
                batch_size=32,
                callbacks=[
                    keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True),
                    keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=5)
                ]
            )
            
            logger.info("モデルの学習が完了しました")
            return model
            
        except Exception as e:
            logger.error(f"モデルの学習に失敗しました: {e}")
            raise
    
    def _prepare_data(self, data: List[FeatureData]) -> Tuple[np.ndarray, np.ndarray]:
        """
        データを準備する
        
        Args:
            data: 特徴量データのリスト
            
        Returns:
            入力データとラベルのタプル
        """
        X = []
        y = []
        
        for feature_data in data:
            # 各馬の特徴量を個別に作成
            for horse in feature_data.horses:
                # 特徴量を取得
                features = self._extract_horse_features(feature_data, horse)
                X.append(features)
                
                # ラベルを作成（1着の馬を1、それ以外を0）
                label = 1 if horse.race_order == 1 else 0
                y.append(label)
        
        return np.array(X), np.array(y)
    
    def _extract_horse_features(self, feature_data: FeatureData, target_horse: HorseRaceInfo) -> np.ndarray:
        """
        特定の馬の特徴量を抽出する
        
        Args:
            feature_data: 特徴量データ
            target_horse: 対象の馬
            
        Returns:
            特徴量配列
        """
        features = []
        
        # レース情報
        race = feature_data.race_info
        features.extend([
            int(race.keibajo_code),
            int(race.track_code),
            race.kyori,
            race.babacd,
            race.tosu,
            race.grade_code,
            race.mu
        ])
        
        # 対象馬の情報
        features.extend([
            target_horse.umaban,
            target_horse.odds,
            target_horse.ninki,
            target_horse.bataiju,
            target_horse.futan,
            target_horse.sire_rate,
            target_horse.jockey_rate,
            target_horse.hensa
        ])
        
        return np.array(features, dtype=np.float32)
    
    def _extract_basic_features(self, feature_data: FeatureData) -> np.ndarray:
        """
        基本的な特徴量を抽出する（予測用）
        
        Args:
            feature_data: 特徴量データ
            
        Returns:
            特徴量配列
        """
        # 最初の馬の特徴量を返す（簡略化）
        if feature_data.horses:
            return self._extract_horse_features(feature_data, feature_data.horses[0])
        else:
            return np.zeros(15, dtype=np.float32)  # レース情報7 + 馬の情報8
    
    def _build_transformer_model(self) -> keras.Model:
        """
        Transformerモデルを構築する
        
        Returns:
            構築されたモデル
        """
        # 入力層
        inputs = keras.Input(shape=(self.feature_size,))
        
        # 入力次元を埋め込み次元に変換
        x = layers.Dense(512, activation='relu')(inputs)
        x = layers.Dropout(0.1)(x)
        
        # シーケンスとして扱うために次元を追加
        x = layers.Reshape((1, 512))(x)
        
        # Positional Encoding
        pos_encoding = self._positional_encoding(1, 512)
        x = x + pos_encoding
        
        # Multi-Head Attention
        attention_output = layers.MultiHeadAttention(
            num_heads=8, key_dim=64
        )(x, x)
        x = layers.Add()([x, attention_output])
        x = layers.LayerNormalization(epsilon=1e-6)(x)
        
        # Feed Forward
        ffn_output = layers.Dense(2048, activation='relu')(x)
        ffn_output = layers.Dense(512)(ffn_output)
        ffn_output = layers.Dropout(0.1)(ffn_output)
        x = layers.Add()([x, ffn_output])
        x = layers.LayerNormalization(epsilon=1e-6)(x)
        
        # 出力層
        x = layers.GlobalAveragePooling1D()(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.Dropout(0.1)(x)
        outputs = layers.Dense(1, activation='sigmoid')(x)  # 2クラス分類（勝つ/負ける）
        
        model = keras.Model(inputs=inputs, outputs=outputs)
        
        # コンパイル
        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.001),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def _positional_encoding(self, length: int, depth: int) -> np.ndarray:
        """
        Positional Encodingを作成する
        
        Args:
            length: シーケンス長
            depth: 埋め込み次元
            
        Returns:
            Positional Encoding配列
        """
        positions = np.arange(length)[:, np.newaxis]
        depths = np.arange(depth // 2)[np.newaxis, :] / (depth // 2)
        
        angle_rates = 1 / (10000**depths)
        angle_rads = positions * angle_rates
        
        pos_encoding = np.concatenate(
            [np.sin(angle_rads), np.cos(angle_rads)],
            axis=-1
        )
        
        return pos_encoding.astype(np.float32)
    
    def predict_win_probabilities(self, model: Any, data: List[FeatureData]) -> List[float]:
        """
        勝率を予測する
        
        Args:
            model: 学習済みモデル
            data: 予測データ
            
        Returns:
            予測勝率のリスト（1レース内で合計1に標準化）
        """
        try:
            probabilities = []
            
            for feature_data in data:
                race_probabilities = []
                
                # 各馬の勝率を予測
                for horse in feature_data.horses:
                    features = self._extract_horse_features(feature_data, horse)
                    features = np.expand_dims(features, axis=0)
                    
                    # 予測
                    pred = model.predict(features, verbose=0)
                    race_probabilities.append(pred[0][0])  # sigmoid出力の値
                
                # 1レース内でsoftmax正規化（合計1に標準化）
                if race_probabilities:
                    # 数値の安定性のため、最大値を引く
                    max_prob = max(race_probabilities)
                    exp_probs = [np.exp(prob - max_prob) for prob in race_probabilities]
                    sum_exp_probs = sum(exp_probs)
                    
                    # softmax正規化
                    normalized_probs = [exp_prob / sum_exp_probs for exp_prob in exp_probs]
                    probabilities.extend(normalized_probs)
            
            return probabilities
            
        except Exception as e:
            logger.error(f"勝率の予測に失敗しました: {e}")
            raise


class EvaluationServiceImpl(EvaluationService):
    """評価サービス実装"""
    
    def calculate_accuracy(self, predictions: List[PredictionResult]) -> float:
        """
        予測精度を計算する
        
        Args:
            predictions: 予測結果のリスト
            
        Returns:
            予測精度
        """
        try:
            # 1着予測の精度を計算
            correct_predictions = 0
            total_races = len(set(p.race_id for p in predictions))
            
            for race_id in set(p.race_id for p in predictions):
                race_predictions = [p for p in predictions if p.race_id == race_id]
                # 最も確率の高い馬を1着予測とする
                best_prediction = max(race_predictions, key=lambda x: x.predicted_win_probability)
                if best_prediction.actual_race_order == 1:
                    correct_predictions += 1
            
            accuracy = correct_predictions / total_races if total_races > 0 else 0.0
            logger.info(f"予測精度: {accuracy:.4f}")
            return accuracy
            
        except Exception as e:
            logger.error(f"予測精度の計算に失敗しました: {e}")
            raise
    
    def calculate_correlation(
        self, 
        predicted_probabilities: List[float], 
        actual_orders: List[int]
    ) -> float:
        """
        予測勝率と実際の着順の相関を計算する
        
        Args:
            predicted_probabilities: 予測勝率のリスト
            actual_orders: 実際の着順のリスト
            
        Returns:
            相関係数
        """
        try:
            # 着順を数値に変換（1着=1, 2着=2, ...）
            corr = np.corrcoef(predicted_probabilities, actual_orders)[0, 1]
            if np.isnan(corr):
                corr = 0.0
            
            logger.info(f"予測勝率と実際の着順の相関: {corr:.4f}")
            return corr
            
        except Exception as e:
            logger.error(f"相関の計算に失敗しました: {e}")
            raise
    
    def calculate_rank_correlation(
        self, 
        predicted_ranks: List[int], 
        actual_orders: List[int]
    ) -> float:
        """
        予測順位と実際の着順の相関を計算する
        
        Args:
            predicted_ranks: 予測順位のリスト
            actual_orders: 実際の着順のリスト
            
        Returns:
            順位相関係数
        """
        try:
            # スピアマンの順位相関を計算
            from scipy.stats import spearmanr
            corr, _ = spearmanr(predicted_ranks, actual_orders)
            if np.isnan(corr):
                corr = 0.0
            
            logger.info(f"予測順位と実際の着順の順位相関: {corr:.4f}")
            return corr
            
        except Exception as e:
            logger.error(f"順位相関の計算に失敗しました: {e}")
            raise 