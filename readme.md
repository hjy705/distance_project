# **Distance Project**

## **專案說明**
<br>分別抓取*雨量站*、*淹水感知器*、*下水道圖層*之資料，透過索取座標值計算出測站相對位置的距離。

 </br>

## **環境說明**
<br>Windows 10 家用版；
<br>Python version 3.6.8

</br>

## **檔案說明**
<br>distance.py 為撰寫之主要程式
<br>distance.json 專案完成的數據結果
<br>rain_station.json / flooding_sensor_layer.json / sewer_layer.json 為基本資料檔案
<br>requirements.txt存放虛擬環境下所設的套件

</br>

## **成果說明**
<br>透過資料索取、計算後的結果，彙整成字典的形式分別呈現:淹水感知器對應雨量站和下水道的測站名與距離；下水道對應雨量站與淹水感知器的測站名與距離。
