# sayısal tuş takımı Modunu Taklit Et #

*	Geliştirici: İbrahim Hamadeh
*	[Geliştirme sürümü 0.6'yı indirin][1]
*	NVDA uyumluluğu: 2019.3 ve sonrası.

## giriş:

Bu eklenti, klavyesinde sayısal tuş takımı olmayan bir kullanıcının isteği üzerine yapılmıştır.  
Böylece sayısal tuş takımının gezinme özelliğinden faydalanmayı sağlar.  
Bu yüzden bu eklentinin daha çok bilgisayarında sayısal tuş takımı olmayan kullanıcıların ilgisini çekeceğini düşünüyoruz.  
İnceleme, nesne gezinme ile ilgili olarak sayısal tuş takımı tuşlarını ve ilgili komutlarını taklit etmelerini sağlamak için ana klavyedeki mevcut formlardan veya tuş setlerinden birini seçebiliriz.  

## kullanım:

Eklenti yüklendikten sonra, üç mod bulunur:  
Bunlar: Normal, Sayısal ve Gezinme modlarıdır.  
Ancak, Sayısal Mod varsayılan olarak atlanmıştır.  
NVDA+F4 kısayolu ile bu modlar arasında geçiş yapılabilir.  
Bu atanmmış hareket, her zamanki gibi NVDA>Tercihler>Girdi hareketleri iletişim kutusunda "Sayısal Tuş takımını taklit et" dalı altından değiştirilebilir.  

Eklentide, aşağıdaki üç Form bulunur:

*	form 1:  
e r t  
d f g  
c v b  
*	form 2:  
y u ı  
h j k  
n m ö  
*	form 3:  
7 8 9  
u ı o  
j k l

Bu formların her biri, aşağıdaki tuşları taklit eder:

sayısal tuş takımı7 sayısal tuş takımı8 sayısal tuş takımı9  
sayısal tuş takımı4 sayısal tuş takımı5 sayısal tuş takımı6  
sayısal tuş takımı1 sayısal tuş takımı2 sayısal tuş takımı3  

Yukarıdaki tuşlar tek başına, Shift ve NVDA tuşları ile birlikte kullanılarak numara pedi taklit edilebilir.  

## Eklenti Ayarları: ##

Eklenti ayarlarına gitmek için: NVDA>Tercihler>Ayarlar iletişim kutusuna gidiyor ve "Sayısal tuş takımını taklit et" dalını seçiyoruz.  

*	Sayısal tuş takımı modunda taklit  edilecek formu seçin Seçim kutusu: Buradan sayısal tuş takımı modunda taklit etmek istediğimiz formu seçebiliriz. Form1 varsayılan olarak seçilmiştir.
*	Daha sonra çoklu düzenleme metin kutusuna erişiriz: seçtiğimiz form için atanmış tuşları görüntülememize yardımcı olur. Gezinmek için yukarı ve aşağı okları kullanabiliriz.
*	Sayısal modu atla onay kutusu: varsayılan olarak işaretli gelir. Sayısal mod, eklentiyi isteyen kullanıcı tarafından istendi ve ikincil görünse ve çoğu kullanıcı tarafından kullanılmasa bile, kalmasını istedik.
*	Escape tuşuyla Sayısal tuş modunu kapat onay kutusu: varsayılan olarak işaretlidir, böylece eklentinin geçiş hareketiyle (varsayılan olarak NVDA+F4) veya Escape tuşuyla normal moda dönebiliriz.

Son not:
Bazen kimi eklentiler, formun hareketlerinden bir veya daha fazlasını alabilir. Umarım bunu başka bir form kullanarak veya theif eklentisinden hareketi kaldırarak yönetebilirsiniz, çünkü şimdiye kadar başka çözüm bulamadık.  

### 0.6 için değişiklikler ###
Eklenti, birçok yeni özellik sunularak güncellendi:

*	Eklenti için bir ayar paneli oluşturuldu.
*	Artık sayısal tuş takımı modunu taklit etmek için üç form mevcut. Kullanıcı dilediğini seçebilir.
*	Sayısal mod artık varsayılan olarak atlanmıştır. Bu durum eklenti ayarlarından değiştirilebilir.
*	Artık sayısal tuş takımı modu Escape tuşuyla kapatılabilir. Bu seçeneğe, eklenti ayarlarından erişilebilir ve değiştirilebilir.

### 0,5 için değişiklikler: ###

*	NVDA 2022.1 API'sı ile uyumlu olması için en son test edilen sürümü güncellendi.

### 0.4 için değişiklikler: ###

*	Türkçe çeviri eklendi.

### Katkıda bulunanlar: ###

*	umut korkmaz eklentinin türkçe çevirisine destek verdiğiniz için teşekkürler.

[1]: https://github.com/ibrahim-h/emulateNumpadMode/releases/download/0.5/emulateNumpadMode-0.5.nvda-addon
