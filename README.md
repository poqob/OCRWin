# OCRWin
3. Kullanım Kılavuzu
3.0. Kurulum Talimatları:
3.1. Python Kurulumu: Proje, Python programlama dili kullanılarak geliştirildiği için ilk adım olarak Python'un bilgisayarınıza yüklü olması gerekmektedir. Python'un en son sürümünü resmi Python web sitesinden indirip kurabilirsiniz.
3.2. Gerekli Kütüphanelerin Kurulumu: Proje, PIL (Python Imaging Library) ve pytesseract gibi kütüphaneleri kullanmaktadır. Bu kütüphaneleri yüklemek için aşağıdaki adımları takip edebilirsiniz:
   - PIL Kütüphanesi: Komut istemini açın ve aşağıdaki komutu girin:
     Terminal: pip install pillow
   - pytesseract Kütüphanesi: Komut istemini açın ve aşağıdaki komutu girin:
    Terminal: pip install pytesseract
3.3. Projenin İndirilmesi: Proje dosyalarını indirmek için projenin bulunduğu depoya gidin ve "Clone" veya "Download" seçeneğini kullanarak dosyaları bilgisayarınıza indirin.
Github Link: https://github.com/poqob/OCRWin
3.4. Projenin Çalıştırılması: İndirdiğiniz proje dosyalarını bir dizine çıkartın. Ardından, komut istemini açın ve proje dizinine gidin. Aşağıdaki komutu girerek projeyi çalıştırabilirsiniz:
   Terminal: python new2.py


3.5. Uygulama Kullanımı ve Özellikleri:
Bu uygulama, görüntülerden metin çıkarmak için kullanılan bir araçtır. Kullanıcı, arayüz üzerinden iki farklı yöntemle metin çıkarımı yapabilir:
3.5.1. Görüntü Seçme: "Select Picture" düğmesine tıklayarak bir görüntü seçebilirsiniz. Seçtiğiniz görüntü açılacak ve metin çıkarımı işlemi gerçekleştirilecektir. Elde edilen metin, uygulama arayüzünde görüntülenecektir.
3.5.2. Ekran Görüntüsü Yapıştırma: Uygulama arayüzünde "Press Ctrl+V to paste a screenshot" yazan bir bölüm bulunmaktadır. Bu bölüme, ekran görüntüsü yapıştırabilirsiniz. Yapıştırdığınız ekran görüntüsü üzerinde metin çıkarımı işlemi gerçekleştirilecek ve elde edilen metin, uygulama arayüzünde görüntülenecektir.
Program kullanım videosu: https://youtu.be/hIAdSMpznc0
3.6. İlerleme Planı:
Uygulama açık kaynak kodlu olarak geliştirilecek olup, ilerleyen süreçte çevrim içi hizmet sunabilme yeteneğine sahip hale getirilmesi planlanmaktadır. Şu an itibarıyla, 06-2023 tarihi itibarıyla sadece Windows platformunda kullanılabilir durumdadır. Projenin tek geliştiricisi ben olduğum için güncellemeler sık ve düzenli bir şekilde gerçekleştirilemeyebilir. Ancak, ilerleyen güncellemelerde öncelikli olarak uygulamanın sunucu tarafında hizmet verebilme yeteneği yeniden kodlanacak ve mikro hizmetlerle yeni özellikler kazandırılacaktır. Ayrıca, yeni bir kullanıcı arayüzü Flutter kullanılarak tüm platformlar için oluşturulacaktır. Bu sayede uygulamanın kullanılabilirliği artacak ve kullanıcılar farklı platformlarda sorunsuz bir deneyim yaşayabilecektir.
