# Wearlog（ウェアログ）

[![WearLog](wearlog/app/assets/images/WearLog_thmb.jpg)](https://www.youtube.com/watch?v=E5Hs6CRP7Mo&feature=youtu.be)

## 製品概要
### 衣服 X Tech

### 背景（製品開発のきっかけ、課題等）
 友達と遊ぶ日，バイトの日，飲み会の日など，何かイベントがあるとき，前回と同じ服を着て行きたくない．

### 製品説明（具体的な製品の説明）
#### ターゲット
 - 服選びに困っている人
#### 課題
 - 前回のイベントに何を着て行ったのか覚えていられない．
 - 毎日服の写真を撮影して保存するのは面倒 → 撮影の自動化

### 特長

#### 1. 自動ログ記録
 - 毎日の服装を自動で撮影してログを取ってくれる．

#### 2. イベントと服装の紐づけ機能
 - カレンダーのイベントと服装を紐づけて，前回のイベントと比較ができる．

#### 3. 服装の管理
 - お気に入りの服をフォルダ分けして管理したり，評価を付けてソートできる．  

#### 4. LINE連携
 - イベントのある日に前回のイベントで着ていた服をLINEで通知できる.

### 解決出来ること
 - 友達と遊ぶ日，バイトの日等に前回と同じ服装で行かなくて済む．

### 今後の展望
 * 過去に着た服の色の割合を出す
 * 収集した服装のログをもとに利用者の服装の傾向を分析し，利用者にあった服を提案
 * SNS化し，自分の服や他人の服を相互に評価することができる機能
 * 初期設定で属性（10代学生，20代女性，40代主婦など）を設定すると，属性ごとのトレンドがわかる


## 開発内容・開発技術
### 活用した技術
#### API・データ

* Google Calender API
* Open Weather API
* LINE API

#### フレームワーク・ライブラリ・モジュール
* Ruby on Rails
* OpenCV
* chainercv 
* scikit-learn
* annoy(近似最近傍探索ライブラリ)

#### デバイス
* Raspberry Pi 3 model B
* mouse USB顔認証カメラ Windows Hello 機能対応 CM01
* iPhone 7 Plus

### 研究内容・事前開発プロダクト（任意）
* カレンダー連携
* 深層学習モデルの事前学習

### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* 人物の自動検出
* 人物の自動撮影
* 人物画像のクロップ
* 服のトップスとボトムスの検出
* 服装のラベリング
* メインカラーの抽出

####
```
docker-compose build
docker-compose run --rm spring rails db:create
docker-compose run --rm spring rails db:migrate
docker-compose up -d

```
