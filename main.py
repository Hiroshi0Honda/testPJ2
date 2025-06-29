"""
競馬データ分析メイン実行ファイル

Must-have Conditionの機能を実行するメインファイル
"""

import os
import sys
import logging
from datetime import datetime
from typing import Dict, Any

# プロジェクトルートをパスに追加
sys.path.append(os.path.dirname(__file__))

from src.infrastructure.dependency_injection import container

# ログ設定
def setup_logging():
    """ログ設定を初期化する"""
    # logsディレクトリが存在しない場合は作成
    os.makedirs("logs", exist_ok=True)
    
    # ログファイル名に日時を含める
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/horse_racing_analysis_{timestamp}.log"
    
    # ログ設定
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def main():
    """メイン実行関数"""
    try:
        # ログ設定
        setup_logging()
        logger = logging.getLogger(__name__)
        
        logger.info("=" * 60)
        logger.info("競馬データ分析システムを開始します")
        logger.info("=" * 60)
        
        # 必要なディレクトリを作成
        os.makedirs("data", exist_ok=True)
        os.makedirs("models", exist_ok=True)
        
        # ユースケースを取得
        usecase = container.get_service('horse_racing_analysis_usecase')
        
        # 特徴量サイズを設定（簡略化のため固定値）
        feature_size = 7 + (18 * 9)  # レース情報7 + 馬の情報18頭分×9項目
        container.set_model_training_service(feature_size)
        
        # 競馬分析を実行
        logger.info("競馬分析の実行を開始します")
        results = usecase.execute_analysis()
        
        # 結果を表示
        logger.info("=" * 60)
        logger.info("分析結果")
        logger.info("=" * 60)
        logger.info(f"予測精度: {results['accuracy']:.4f}")
        logger.info(f"予測勝率と実際の着順の相関: {results['correlation']:.4f}")
        logger.info(f"予測順位と実際の着順の順位相関: {results['rank_correlation']:.4f}")
        logger.info(f"総予測数: {results['total_predictions']}")
        logger.info(f"結果CSVファイル: {results['csv_path']}")
        logger.info("=" * 60)
        
        logger.info("競馬データ分析システムが正常に完了しました")
        
    except Exception as e:
        logger.error(f"競馬データ分析システムの実行に失敗しました: {e}")
        raise
    
    finally:
        # リソースのクリーンアップ
        container.cleanup()


if __name__ == "__main__":
    main() 