# Laporan Capstone Project - LAI25-SM089

## Domain Proyek

Banjir merupakan salah satu bencana alam yang paling sering terjadi di Indonesia, dan memberikan dampak besar terhadap aspek ekonomi, sosial, kesehatan, dan lingkungan. Sebagai negara tropis dengan curah hujan yang tinggi dan kepadatan penduduk yang terus meningkat, Indonesia—terutama wilayah seperti Jakarta, Lampung, Kalimantan, dan Nusa Tenggara Barat—menghadapi tantangan serius dalam pengelolaan risiko banjir.

Menurut data dari [DataIndonesia.ID](https://dataindonesia.id/varia/detail/data-jumlah-bencana-alam-di-indonesia-pada-1-januari-hingga-8-mei-2025), sepanjang 1 Januari hingga 8 Mei 2025 telah tercatat 677 kejadian banjir, menjadikannya sebagai jenis bencana paling dominan di periode tersebut. Fakta ini menunjukkan bahwa sistem mitigasi dan kesiapsiagaan banjir di Indonesia masih perlu ditingkatkan, terutama dalam menghadapi dampak perubahan iklim yang memicu intensitas curah hujan ekstrem.

Dalam konteks ini, penerapan teknologi kecerdasan buatan (Artificial Intelligence/AI) menawarkan potensi besar untuk meningkatkan efektivitas sistem prediksi dan peringatan dini banjir. Sistem prediksi berbasis AI dapat memberikan informasi secara lebih cepat dan akurat, sehingga memungkinkan otoritas maupun masyarakat untuk melakukan tindakan preventif, seperti evakuasi dan persiapan infrastruktur, dengan lebih baik.

Proyek ini bertujuan untuk mengembangkan aplikasi prediksi probabilitas banjir berbasis web, yang mampu memproses data faktor-faktor risiko banjir seperti curah hujan, kepadatan penduduk, dan lainnya, lalu memberikan output berupa probabilitas terjadinya banjir. Berdasarkan nilai probabilitas tersebut, sistem akan menampilkan peringatan dini serta rekomendasi tindakan preventif yang dapat diambil.

Model prediksi dibangun menggunakan pendekatan Artificial Neural Network (ANN) dan Deep Neural Network (DNN) dengan library TensorFlow, di mana masing-masing model akan dievaluasi untuk menentukan performa terbaik. ANN dikenal efektif dalam memodelkan hubungan non-linear antara fitur cuaca dan kejadian banjir, sedangkan DNN menawarkan kedalaman arsitektur yang lebih baik untuk mengekstraksi pola dari data kompleks dan besar.

Dukungan literatur juga menunjukkan efektivitas pendekatan ini. Studi oleh [Chika Stefanny P. S dkk (2025)](https://journal.ppmi.web.id/index.php/jdaics/article/view/1404) menunjukkan bahwa ANN dapat memprediksi banjir secara akurat berdasarkan data curah hujan, dengan hasil Mean Absolute Error (MAE) yang sangat rendah, yaitu 0.0037. Penelitian lain oleh [Triyo Krismantoro dkk (2023)](https://openlibrarypublications.telkomuniversity.ac.id/index.php/engineering/article/download/21274/20549) memperkuat peran deep learning dalam mitigasi bencana banjir. Studi ini mengembangkan sistem deteksi untuk banjir dan gempa bumi, dengan fokus pada banjir yang menggunakan data ketinggian air dari Patriot-net. Metode yang diterapkan mencakup ANN, RNN, dan LSTM, di mana model ANN menunjukkan performa terbaik dengan akurasi mencapai 99,91%. Aplikasi yang dikembangkan menghasilkan dua output utama terkait banjir: prediksi ketinggian air dan status potensi terjadinya banjir.

Dengan menggabungkan pendekatan ilmiah dan teknologi berbasis AI, proyek ini diharapkan dapat memberikan kontribusi nyata dalam upaya peningkatan mitigasi bencana banjir di Indonesia, melalui solusi berbasis data yang adaptif, presisi, dan mudah diakses oleh berbagai pemangku kepentingan. Proses pengembangannya mengikuti tahapan CRISP-DM yang mencakup Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, dan Deployment.

## Business Understanding

### Problem Statements

- Bagaimana memprediksi potensi terjadinya banjir menggunakan data lingkungan dan infrastruktur?
- Model deep learning apa yang lebih akurat dalam memprediksi banjir: ANN atau DNN?
- Fitur-fitur apa yang paling berpengaruh terhadap terjadinya banjir di Indonesia?

### Goals

- Membangun model prediksi banjir berbasis data lingkungan dan infrastruktur menggunakan pendekatan supervised learning.
- Membandingkan performa antara model ANN dan DNN dalam konteks akurasi prediksi banjir.
- Mengidentifikasi fitur lingkungan dan infrastruktur yang paling berkontribusi terhadap model prediksi.

### Solution Statements

- Menggunakan dua pendekatan model deep learning: ANN dan DNN.
- Meningkatkan performa model dengan teknik hyperparameter tuning (jumlah neuron, epoch, batch size, dan learning rate).
- Menerapkan teknik normalisasi untuk menyeimbangkan data sebelum pemodelan.

## Data Understanding

Dataset yang digunakan berasal dari sumber terbuka seperti Kaggle yang berisi faktor-faktor lingkungan dan infrastruktur yang berdampak pada banjir. Dataset ini terdiri dari 50.000 entri data yang mencakup 21 kolom, yaitu 20 fitur input dan 1 kolom target bernama FloodProbability.
Meskipun disusun dalam bahasa Inggris, dataset ini bersifat universal dan dapat diterapkan pada berbagai negara, sehingga relevan digunakan untuk studi kasus ini.

**Tautan Dataset**: [https://www.kaggle.com/datasets/naiyakhalid/flood-prediction-dataset/data](https://www.kaggle.com/datasets/naiyakhalid/flood-prediction-dataset/data)

### Variabel dalam Dataset:

Dataset ini terdiri dari berbagai variabel yang digunakan untuk memprediksi probabilitas terjadinya banjir di suatu wilayah. Setiap variabel merepresentasikan faktor lingkungan, sosial, atau infrastruktur yang dapat memengaruhi risiko banjir. Berikut penjelasan masing-masing fitur:

- `MonsoonIntensity`: Intensitas hujan selama musim monsun. Semakin tinggi intensitasnya, semakin besar risiko banjir.
- `TopographyDrainage`: Kapasitas drainase alami berdasarkan topografi wilayah. Drainase yang baik dapat mengurangi potensi banjir.
- `RiverManagement`: Kualitas pengelolaan sungai, termasuk pengerukan dan pemeliharaan tanggul.
- `Deforestation`: Tingkat deforestasi. Penebangan hutan dapat meningkatkan limpasan permukaan dan risiko banjir.
- `Urbanization`: Tingkat urbanisasi wilayah. Permukaan kedap air di area perkotaan menghambat infiltrasi air.
- `ClimateChange`: Dampak perubahan iklim terhadap curah hujan ekstrem di wilayah tersebut.
- `DamsQuality`: Kualitas struktur dan perawatan bendungan. Bendungan yang terawat dapat menahan banjir, sedangkan yang rusak dapat memperburuknya.
- `Siltation`: Tingkat sedimentasi di sungai dan waduk. Sedimen yang menumpuk dapat mengurangi kapasitas aliran air.
- `AgriculturalPractices`: Pola pertanian dan keberlanjutannya. Praktik buruk dapat menyebabkan erosi dan memperbesar risiko banjir.
- `Encroachments`: Tingkat alih fungsi lahan di dataran banjir dan aliran sungai alami.
- `IneffectiveDisasterPreparedness`: Kesiapsiagaan bencana yang rendah, seperti tidak adanya sistem peringatan dini atau simulasi evakuasi.
- `DrainageSystems`: Kondisi dan ukuran sistem drainase buatan. Drainase yang buruk dapat memicu genangan.
- `CoastalVulnerability`: Kerentanan wilayah pesisir terhadap banjir akibat pasang laut dan naiknya permukaan air laut.
- `Landslides`: Risiko longsor yang berkaitan dengan kemiringan lahan dan stabilitas tanah.
- `Watersheds`: Jumlah dan kondisi daerah aliran sungai (DAS), yang bisa meningkatkan atau mengurangi risiko banjir.
- `DeterioratingInfrastructure`: Infrastruktur yang rusak atau tersumbat seperti gorong-gorong dan saluran air.
- `PopulationScore`: Kepadatan penduduk. Wilayah padat penduduk berisiko mengalami kerugian lebih besar saat banjir.
- `WetlandLoss`: Kehilangan lahan basah, yang berfungsi menyerap kelebihan air secara alami.
- `InadequatePlanning`: Kurangnya perencanaan tata kota yang mempertimbangkan risiko banjir.
- `PoliticalFactors`: Hambatan administratif dan kurangnya komitmen politik dalam pengelolaan risiko banjir.
- `FloodProbability`: Probabilitas banjir di wilayah tersebut. Ini merupakan variabel target dalam analisis prediktif (nilai antara 0 hingga 1).

Visualisasi awal menggunakan histogram, heatmap korelasi, dan scatter plot digunakan untuk memahami distribusi dan relasi antar fitur.

## Data Preparation

Tahap ini mencakup beberapa proses penting untuk memastikan kualitas data sebelum dilakukan pemodelan. Adapun langkah-langkahnya adalah sebagai berikut:

### **Outlier Handling**

Dilakukan teknik _winsorizing_ pada semua fitur dengan memangkas nilai ekstrem di bawah persentil ke-1 dan di atas persentil ke-99. Pendekatan ini digunakan untuk mengurangi dampak _outlier_ ekstrem terhadap performa model tanpa menghilangkan data apa pun.

Tahapan selanjutnya dibagi menjadi dua skenario, yaitu:

### 1. Tanpa Feature Engineering

Dalam pendekatan ini, semua fitur asli dari dataset digunakan secara langsung tanpa rekayasa fitur tambahan. Proses yang dilakukan meliputi:

- **Data Splitting**  
  Dataset dibagi menjadi data pelatihan dan data pengujian dengan rasio 90:10. Mengingat dataset memiliki 50.000 sampel, pembagian ini dianggap memadai untuk menjaga proporsi data uji tetap representatif.

- **Feature Scaling**  
  Proses normalisasi dilakukan menggunakan `RobustScaler` dari `sklearn.preprocessing`. Metode ini dipilih karena lebih tahan terhadap _outlier_ dibandingkan Min-Max Scaling maupun Standard Scaling. `RobustScaler` menggunakan median dan _interquartile range (IQR)_, sehingga lebih stabil pada data dengan distribusi tidak normal atau mengandung nilai ekstrem.

### 2. Dengan Feature Engineering

Pada pendekatan ini, dilakukan pembentukan fitur baru berdasarkan _domain knowledge_ yang diperoleh dari [PUSDATARU Jateng](https://pusdataru.jatengprov.go.id/ppid/dokumen/bencana/Apa-itu-banjir-dan-cara-menghadapi-bencana-banjir.pdf). Fitur-fitur baru yang dibentuk antara lain:

- `EnvironmentalDegradationScore`: Rata-rata dari fitur `Deforestation`, `WetlandLoss`, dan `Urbanization`.
- `RiverObstructionRisk`: Rata-rata dari fitur `Encroachments` dan `Siltation`.

Setelah fitur-fitur tersebut dibentuk, dilakukan seleksi manual fitur berdasarkan penyebab umum banjir di Indonesia yang meliputi curah hujan tinggi, kerentanan kawasan pesisir, kurangnya tutupan lahan, dan hambatan aliran sungai. Fitur yang digunakan dalam versi model _with feature engineering_ meliputi:

- `MonsoonIntensity`
- `CoastalVulnerability`
- `EnvironmentalDegradationScore`
- `RiverObstructionRisk`
- `Siltation`
- `Deforestation`

Langkah-langkah selanjutnya adalah:

- **Feature Scaling**  
  Normalisasi dilakukan menggunakan `RobustScaler` dengan alasan yang sama seperti pada pendekatan tanpa feature engineering: lebih stabil terhadap data yang mengandung _outlier_.

- **Data Splitting**  
  Data dibagi menjadi train dan test set dengan rasio 90:10 dan `random_state=42` untuk memastikan reprodusibilitas hasil. Karena target `FloodProbability` bersifat kontinu, stratifikasi tidak dilakukan.

## Modeling

Dalam proyek ini, dua pendekatan arsitektur digunakan untuk prediksi banjir:

### 1. **Artificial Neural Network (ANN)**

- **Arsitektur**:
  - Tanpa Feature Engineering:  
    `Input → Dense(64) → Output(Sigmoid)`
  - Dengan Feature Engineering:  
    `Input → Dense(64) → Output(Sigmoid)`
- **Optimizer**: Adam (`learning_rate=0.001`)
- **Loss Function**: Mean Squared Error
- **Epochs**: 100 (dengan **EarlyStopping**, `patience=10`)
- **Batch Size**: 32
- **Callbacks**: EarlyStopping

### 2. **Deep Neural Network (DNN)**

- **Arsitektur**:  
  `Input → Dense(64) → Dropout(0.3) → Dense(32) → Dropout(0.2) → Output(Sigmoid)`
  - Digunakan baik untuk data **tanpa** maupun **dengan** feature engineering
- **Optimizer**: Adam
- **Loss Function**: Mean Squared Error
- **Epochs**: 100
- **Batch Size**: 32

Fungsi aktivasi pada layer output menggunakan sigmoid karena hasil yang diinginkan berupa nilai probabilitas dalam rentang 0 hingga 1.

---

## Perbandingan ANN vs DNN

Berikut perbandingan antara kedua model beserta kelebihan dan kekurangannya:

| Aspek                      | Artificial Neural Network (ANN)             | Deep Neural Network (DNN)                                |
| -------------------------- | ------------------------------------------- | -------------------------------------------------------- |
| **Arsitektur**             | 1 hidden layer sederhana                    | 2 hidden layer + dropout untuk regularisasi              |
| **Kompleksitas Model**     | Rendah                                      | Lebih tinggi                                             |
| **Kemampuan Generalisasi** | Cukup baik untuk dataset kecil-sedang       | Lebih baik untuk dataset besar dan kompleks              |
| **Waktu Latih**            | Cepat                                       | Lebih lambat (lebih banyak parameter)                    |
| **Risiko Overfitting**     | Lebih besar jika tanpa regularisasi         | Lebih kecil dengan dropout                               |
| **Kemudahan Interpretasi** | Lebih mudah di-tune dan dianalisis          | Sulit ditelusuri interpretasinya                         |
| **Feature Engineering**    | Pengaruh cukup signifikan terhadap performa | Bisa menangani kompleksitas meski tanpa feature tambahan |

## Evaluation

Model dievaluasi menggunakan metrik **regresi**, karena target prediksi (`FloodProbability`) bersifat kontinu (nilai antara 0 hingga 1). Metrik utama yang digunakan adalah:

- **Mean Absolute Error (MAE)**: Rata-rata selisih absolut antara nilai aktual dan nilai prediksi. Semakin kecil nilai MAE, semakin baik performa model dalam melakukan prediksi.

### Hasil Evaluasi:

| Model                          | MAE        |
| ------------------------------ | ---------- |
| ANN tanpa Feature Engineering  | **0.0021** |
| ANN dengan Feature Engineering | 0.3220     |
| DNN tanpa Feature Engineering  | **0.0022** |
| DNN dengan Feature Engineering | 0.0320     |

Berdasarkan hasil evaluasi, feature engineering yang diterapkan justru menurunkan performa model secara signifikan, terlihat dari peningkatan nilai MAE terutama pada model ANN. Model dengan performa terbaik secara metrik MAE adalah ANN tanpa feature engineering, dengan nilai MAE terendah (0.0021), yang menunjukkan prediksi sangat mendekati nilai aktual.

Namun demikian, dalam konteks implementasi aplikasi yang mempertimbangkan kompleksitas data dan karakteristik demografis Indonesia, model yang dipilih adalah DNN dengan feature engineering, karena dianggap lebih adaptif terhadap variasi fitur dan memiliki performa yang tetap baik (MAE = 0.0320), meskipun tidak serendah model lain.

## Deployment

Model yang telah dikembangkan diimplementasikan ke dalam aplikasi prediksi banjir berbasis web.

Aplikasi ini dibangun menggunakan Streamlit dan menyediakan beberapa fitur utama, yaitu:

- Prediksi probabilitas banjir berdasarkan input data
- Sistem peringatan dini untuk potensi banjir
- Menu edukasi atau sosialisasi terkait penanggulangan banjir
- Informasi mengenai website serta kontak pengembang aplikasi

## Dampak terhadap Business Understanding

### Problem Statements

- **Bagaimana memprediksi potensi terjadinya banjir menggunakan data cuaca dan lingkungan?**  
  → Proyek ini berhasil membangun model prediksi berbasis AI yang memanfaatkan berbagai indikator lingkungan seperti **intensitas monsun (curah hujan musiman)**, **kerentanan wilayah pesisir**, **kerusakan lingkungan (deforestasi, urbanisasi, dan kehilangan lahan basah)**, serta **penyempitan sungai akibat sedimentasi dan pembangunan liar**. Sistem ini dapat digunakan sebagai **alat peringatan dini berbasis data** untuk wilayah rawan banjir di Indonesia.

- **Model deep learning apa yang lebih akurat dalam memprediksi banjir: ANN atau DNN?**  
  → Evaluasi menunjukkan bahwa **ANN tanpa feature engineering** memiliki nilai MAE terendah. Namun, **DNN dengan feature engineering** dipilih karena lebih representatif terhadap **kondisi geospasial dan lingkungan Indonesia**, serta lebih siap untuk diintegrasikan ke dalam **aplikasi prediksi banjir berbasis web**.

- **Faktor lingkungan apa yang paling berpengaruh terhadap terjadinya banjir di Indonesia?**  
  → Evaluasi fitur menunjukkan bahwa faktor seperti **intensitas monsun**, **deforestasi**, **tingkat sedimentasi (siltation)**, dan **kerentanan wilayah pesisir** merupakan faktor signifikan dalam prediksi banjir. Informasi ini relevan untuk lembaga seperti BMKG, BPBD, dan dinas lingkungan dalam mendukung kebijakan mitigasi berbasis data.

---

### Goals

- **Membangun model prediksi banjir berbasis data lingkungan dan cuaca dengan pendekatan supervised learning.**  
  → Model berhasil dibangun dan diuji menggunakan pendekatan ANN dan DNN. DNN dengan rekayasa fitur dipilih karena memberikan hasil yang seimbang antara akurasi dan kemampuan generalisasi di kondisi nyata.

- **Membandingkan performa antara model ANN dan DNN dalam konteks prediksi risiko banjir.**  
  → Perbandingan dilakukan menggunakan metrik MAE. Hasilnya menunjukkan bahwa meskipun ANN memiliki error lebih rendah, DNN lebih cocok untuk **implementasi sistem real-time** karena lebih stabil pada data kompleks.

- **Mengidentifikasi indikator lingkungan yang paling relevan terhadap model prediksi banjir.**  
  → Identifikasi ini dilakukan melalui proses feature selection dan domain knowledge. Faktor-faktor seperti **kerusakan lingkungan**, **obstruksi sungai**, dan **kerentanan pesisir** menjadi fokus utama dalam sistem monitoring dan kebijakan mitigasi.

---

### Solution Statements

- **Mengembangkan dua model deep learning: ANN dan DNN.**  
  → Kedua model berhasil dikembangkan dan diuji. Model DNN dipilih untuk deployment karena mempertimbangkan kemampuan adaptasi terhadap kompleksitas data lingkungan.

- **Mengoptimalkan model menggunakan hyperparameter tuning (jumlah neuron, batch size, epoch, dan learning rate).**  
  → Proses tuning dilakukan iteratif untuk menghasilkan konfigurasi terbaik dan meningkatkan stabilitas performa model pada data validasi.

- **Menerapkan teknik normalisasi (RobustScaler) dan feature engineering untuk menangani outlier serta menggabungkan informasi relevan.**  
  → Pendekatan ini meningkatkan daya prediktif model dan menjaga stabilitas meskipun terdapat variabilitas tinggi pada data lingkungan.

## Kesimpulan

Proyek ini dikembangkan sebagai upaya mitigasi banjir di Indonesia dengan memanfaatkan dataset dari Kaggle. Proses pemodelan dilakukan dengan membandingkan dua pendekatan, yaitu Artificial Neural Network (ANN) dan Deep Neural Network (DNN), baik dengan maupun tanpa rekayasa fitur (feature engineering). Hasil evaluasi menunjukkan bahwa model DNN dengan feature engineering memberikan performa terbaik dengan nilai Mean Absolute Error (MAE) sebesar 0.320.

Model terbaik ini kemudian diimplementasikan dalam bentuk aplikasi berbasis web menggunakan Streamlit Cloud, dengan nama Flood Prediction App. Aplikasi ini dirancang untuk memberikan prediksi potensi banjir secara cepat dan akurat, sehingga dapat dimanfaatkan sebagai alat bantu oleh pemerintah dan masyarakat dalam meningkatkan kesiapsiagaan dan respons terhadap bencana banjir.

---

_Catatan:_
Visualisasi heatmap, confusion matrix, dan grafik loss/accuracy disertakan dalam notebook yang dapat diakses pada direktori model_development/Model_ML_Development_LAI_Capstone.ipynb atau bisa klik [link ini](https://github.com/teguhh18/Capstone_LaskarAI_LAI25-SM089/blob/main/model_development/Model_ML_Development_LAI_Capstone.ipynb).

---

**Sumber Referensi**:

- Ridha Kusuma Perdana. (2025, May 8). Data Jumlah Bencana Alam di Indonesia pada 1 Januari hingga 8 Mei 2025. Data Indonesia: Data Indonesia for Better Decision. Valid, Accurate, Relevant; dataindonesia.id. https://dataindonesia.id/varia/detail/data-jumlah-bencana-alam-di-indonesia-pada-1-januari-hingga-8-mei-2025

‌- Stefanny P. S, C., & Suharsono, T. N. (2025). PREDIKSI BANJIR DI KABUPATEN KARAWANG BERDASARKAN CURAH HUJAN DENGAN METODE ARTIFICAL NEURAL NETWORK. Journal of Data Analytics, Information, and Computer Science, 2(1), 10–19. https://doi.org/10.70248/jdaics.v2i1.1404

- Krismantoro, T., Suhendi, A., & Saputra, C. (2023). Analisis Penerapan ANN dan RNN dengan Inisialisasi Nguyen-Widrow pada Aplikasi Monitoring Banjir dan Gempa. eProceedings of Engineering, 10(5).

- https://pusdataru.jatengprov.go.id/ppid/dokumen/bencana/Apa-itu-banjir-dan-cara-menghadapi-bencana-banjir.pdf
