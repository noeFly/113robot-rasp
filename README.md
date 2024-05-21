# rasp

* [介紹](#介紹)
* [依賴](#依賴)
* [開發](#開發)

## 介紹

此專案是本人參加 [113 年度中小學資通訊應用大賽-智組型機器人](https://lurl.cc/hq2QXV)
，編寫在 [樹莓派（Raspberry Pi）](https://lurl.cc/Es4hit)上運行的程式，所以幾乎沒什麼技術可言。
> [!IMPORTANT]
> 此專案於競賽結束後公開，並轉為唯獨專案。  
> 不接受一切的 Issue 和 Pull Request。

## 依賴

> [!TIP]
> 詳細依賴套件請參考 [requirements.txt](./requirements.txt)

* [Python](https://lurl.cc/holoIm)
    * [paho-mqtt](https://lurl.cc/tJ2ycC)
    * [python-dotenv](https://lurl.cc/gRldhY)
    * [pygsheets](https://lurl.cc/UX1CKb)
    * [requests](https://lurl.cc/HkqzVE)

## 開發

1. 複製此儲存庫到本機。
    ```shell
    git clone https://github.com/noeFly/rasp.git
    ```
2. 安裝必要套件。
    ```shell
    python3 -m install -r ./requirements.txt
    ``` 
3. 啟動各程式。
    ```shell
    bash ./start.sh
    ```