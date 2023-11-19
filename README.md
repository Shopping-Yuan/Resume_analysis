更新日期:2023/11/12
本專案預計呈現一個基於Django、pytorchu以及mysql建立的專案，
可在網頁接收使用者上傳的食物圖片，並利用pytorch以semi-supervised方式訓練的cnn模型得到分類結果，
並在網頁中展示結果，將良好的結果存入資料庫，以更新模型。

本專案分為三個主要部分:
Data_preparing 資料夾將包含資料處理和儲存的功能
Analysis_and_Model將包含模型和訓練、儲存模型的功能
Website_building 資料夾將包含呈現網頁的所有功能

本次更新的功能集中在Analysis_and_Model的model資料夾中
1.pytorch_setting中，設定訓練模型時的各種隨機變數，以及裝置(cpu、gpu，未來可能新增mac的imp )

2.data_info 設定了訓練用、驗證用資料集的路徑以及處理資料集的函數(函數並非實作在這裡)。

3.hyper_parameters 設定訓練用的超參數，亦即會透過手動調整以優化模型訓練結果的參數。

4.cnn_model 中實作了訓練用的cnn模型

5.dataset_construction 中實作了資料處理的函數，未來會和Data_preparing連結，包含2個檔案:

5-1.dataset_preparing 中實作資料處理的函數，(11/19新增)包含半監督學習中處理資料的類別和函數。

5-2.get_data_set 執行後，按data_info的設定，在dataset_preparing中尋找對應的函數進行處理，
進行格式處理後，輸出可迭代訓練用、驗證用資料的Dataloader

6.training_process中，將get_data_set得到的資料集，以及hyper_parameters中的設定輸入cnn_model，
訓練並儲存模型，目前包含6個檔案:

6-1.train中實作利用訓練集，訓練模型的步驟

6-2.val中實作驗證模型的過程，當所有資料跑過一輪後，會進行驗證，輸出目前模型的準確度

(11/19新增) 6-3.semi_supervised_learning 中實作了半監督學習的過程，在訓練模型時，
會把對預測結果較有把握的未標註資料，新增至初始訓練集。
每一次的新增資料都是個別獨立，根據現有模型，重新由未標註資料中選定，
再讀入初始訓練集，以初始訓練集和新增資料組成新訓練集。

6-3.train_val_process整合train和val檔案，決定是否輸出結果或暫停訓練，未來將在train和val之間，
新增semi-supervised learining的功能，亦即多準備一個未被標註的資料集，利用目前訓練的模型進行標註，
將具有良好結果(分成某一類的機率極高)的未標註資料加進訓練集。將輸出並儲存模型參數，損失函數和準確率的變化。

6-4.get_model執行後，將執行train_val_process輸出模型、損失函數和準確率的變化，並存入指定的路徑。

6-5.plot_outcome執行後，讀取get_model存入的訓練集、驗證集的損失函數和準確率的變化，利用matplotlib進行視覺化。

另外，本專案含有:
Dataflow.docx 呈現專案的資料流程圖
environment.yaml 是目前conda環境中安裝的package，但尚未經過完整測試，目前有許多功能尚無法運行，
未來預計利用docker進行整合。
README.md 本檔案，將會隨日期更新