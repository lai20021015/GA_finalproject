# 台灣機車環島路線規劃 (使用基因演算法) :motorcycle:

## 專案簡介

本專案運用基因演算法(GA)來最佳化台灣機車環島旅遊路線。我們的目標是在考慮景點評分、行駛距離等因素的情況下，為旅行者提供一個平衡且高效的環島路線。
試圖最小化距離並最大化旅遊景點評分數。
<br>
### Formula : score = distance * (-0.1) + rating

## 功能特點

- 利用Google Maps API獲取景點資訊和距離數據
- 基於評分和評論數篩選高質量景點
- 使用基因演算法優化路線選擇
- 生成詳細的行程規劃，包括每日路線和推薦景點
- 與現有熱門路線進行比較分析

## 技術stack :dna:

- Python: 主要編程語言
- Google Maps API: 地理數據獲取
- 基因演算法:TSP旅行家問題解決方法
- 數據處理: Pandas, NumPy
- 數據視覺化: Matplotlib

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

## 結果展示 :bar_chart:

![image](https://github.com/user-attachments/assets/945205e9-c4dc-433d-81f7-1a050611092b)
![image](https://github.com/user-attachments/assets/471d6558-e1a1-4828-8513-9a2cda945a65)


## 未來改進

- 整合即時交通數據以優化路線
- 開發用戶友好的前端界面
- 加入更多自定義選項，如預算限制、時間偏好等
- 擴展到其他旅遊方式，如自駕車、公共交通等
