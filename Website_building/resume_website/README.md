
作為練習用的資料是來自genius_invokation卡牌遊戲的卡片相關資訊，
使用mysql系統，將資料儲存在genius_invokation資料庫裡的all_card表中，
每一筆資料代表一張(種)卡片，存入編號、名稱、類型共三項屬性。

目前網站的功能有:
1.在後台檢視、新增、刪除mysql資料庫中的資料
當網址為 http://127.0.0.1:8000/admin/ 時，透過my_web中的urls.py，
將請求轉發給catalog/admin.py，而admin.py將會import資料夾下的models.py，
用all_card物件的屬性，呈現資料庫中的資料(可能有用到Django的預設的後台網頁模板)

2.在網站首頁檢視目前mysql資料庫中的所有資料
當進入首頁(http://127.0.0.1:8000/catalog/index)時，透過mysite以及catalog資料夾中的urls.py，將請求轉到views.py中，
views.py由mysql資料庫抓取資料，並藉由template.py中的index.html模板生成網頁。

3.在網頁上輸入資料並存入mysql資料庫中。(進入http://127.0.0.1:8000/catalog/add_data/)
另外views/urls中的search函數，對應post.html模板，是網路上參考資料的內容(可以將輸入的文字即時顯示在網頁上)。

4.目前新增搜尋和更新資料功能(/catalog/renew_data/)

目前安裝的python libraries為:
Django==4.2.3
PyMySQL==1.1.0(尚未使用)
