# 台灣機車環島路線規劃 (使用基因演算法)

## 專案簡介

本專案運用基因演算法(GA)來最佳化台灣機車環島旅遊路線。我們的目標是在考慮景點評分、行駛距離等因素的情況下，為旅行者提供一個平衡且高效的環島路線。

## 功能特點

- 利用Google Maps API獲取景點資訊和距離數據
- 基於評分和評論數篩選高質量景點
- 使用基因演算法優化路線選擇
- 生成詳細的行程規劃，包括每日路線和推薦景點
- 與現有熱門路線進行比較分析

## 技術stack

- Python: 主要編程語言
- Google Maps API: 地理數據獲取
- 基因演算法庫 (例如: DEAP)
- 數據處理: Pandas, NumPy
- 數據視覺化: Matplotlib, Folium

## 安裝和使用

1. 克隆儲存庫:
   ```
   git clone https://github.com/your-username/ga-motorcycle-tour.git
   ```
2. 安裝依賴:
   ```
   pip install -r requirements.txt
   ```
3. 設置Google Maps API金鑰 (在 `config.py` 文件中)
4. 運行主程序:
   ```
   python main.py
   ```

## 專案結構

```
ga-motorcycle-tour/
│
├── data/                 # 景點數據和距離矩陣
├── src/                  # 源代碼
│   ├── ga/               # 基因演算法實現
│   ├── data_collection/  # 數據收集和處理
│   └── visualization/    # 結果視覺化
├── results/              # 輸出結果和圖表
├── tests/                # 單元測試
├── main.py               # 主程序
├── requirements.txt      # 項目依賴
└── README.md             # 本文件
```

## 結果展示

[在這裡添加一些生成路線的截圖或動態地圖]

## 未來改進

- 整合即時交通數據以優化路線
- 開發用戶友好的前端界面
- 加入更多自定義選項，如預算限制、時間偏好等
- 擴展到其他旅遊方式，如自駕車、公共交通等

## 貢獻

歡迎貢獻！請閱讀 `CONTRIBUTING.md` 了解如何開始。

## 許可證

本專案採用 MIT 許可證 - 查看 [LICENSE.md](LICENSE.md) 文件了解詳情。

## 聯繫我們

如有任何問題或建議，請開啟一個issue或直接聯繫項目維護者。

---

**注意**: 本專案僅供學習和研究使用。在進行實際的機車環島旅行時，請務必考慮安全因素，並遵守交通規則。
