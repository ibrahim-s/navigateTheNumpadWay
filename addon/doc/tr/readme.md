# Sayısal Tuş Takımı İle Dolaşma #

*	Yazar: Ibrahim Hamadeh
*	[Sürüm 1.1'i indirin][1]
*	NVDA uyumluluğu: 2019.3 ve sonrası

## giriş:

Bu eklenti, klavyesinde sayısal tuş takımı veya sayısal tuş takımı tuşları olmayan bir kullanıcının isteğine yanıt olarak yapılmıştır.  
Böylece sayısal tuşların dolaşma özelliğinden faydalanmasına olanak tanıyor.  

Dolayısıyla bu eklentinin daha çok bilgisayarında sayısal tuş takımı bulunmayan kullanıcıların ilgisini çekeceğini düşünüyorum.  
Gözden geçirme veya nesne dolaşımı ile ilgili sayısal tuş takımı tuşlarına ve ilgili komutlarına taklit  edilmesini sağlamak için ana klavyedeki kullanılabilir formlardan veya tuş kümelerinden birini seçebilirsiniz.

## Kullanım:

Eklentiyi yükledikten sonra üç modunuz olacak.  

Normal, Sayısal tuş takımı ve sayılar modu, sayılar modu varsayılan olarak atlanır, dolayısıyla esas olarak normal ve sayısal tuş takımı olmak üzere iki modumuz vardır.  

Shift+NVDA+f4 kısayolunu kullanarak bu modlar arasında geçiş yapabilir ve her zaman olduğu gibi kısayolu NVDA menüsü/tercihler/girdi hareketleri/Sayısal Tuş Takımı İle Dolaşma dalına giderek değiştirebilirsiniz.  

Sayısal tuş takımı moduna benzetebileceğiniz mevcut formlar şunlardır:

*	form1:  
q w e  
a s d  
z x c  

*	form2:  
e r t  
d f g  
c v b  
*	form3:  
y u i  
h j k  
n m ö  

*	form4:  
7 8 9  
u i o  
j k l

Bu formların her biri:  

numpad7 numpad8 numpad9  
numpad4 numpad5 numpad6  
numpad1 numpad2 numpad3  

Taklit eder.  

Tek başına, shift ya da NVDA tuşlarıyla birlikte kullanılarak inceleme veya nesne dolaşımını taklit eder.

## Eklenti Ayarları ##

Eklenti ayarlarına erişmek için:  
NVDA Menüsü>Tercihler>Ayarlar yolunu takip ederek iletişim kutusunu açıyor,  
S harfi ile Sayısal Tuş Takımı İle Dolaşma seçeneğini buluyoruz.

*	Sayısal tuş takımında taklit edilecek formu seçin açılır kutusu: Buradan sayısal tuş takımı modunda taklit edilmesini istediğiniz formu seçebilirsiniz. Form1 varsayılan olarak seçilidir.
*	Ardından, salt okunur metin kutusunda seçili form düzeninin görüntülendiği alan: seçtiğiniz formu görüntülemenize yardımcı olacak ve dolaşmak için yukarı ve aşağı okları kullanabilirsiniz.
*	Atlama Seçenekleri açılır kutusu: Sayısal modu Atla, Dolaşma modunu atla veya her iki modu da etkin tutmanızı sağlar.
*	Escape tuşuyla Sayısal Tuş Takımı modunu kapat onay kutusu: varsayılan olarak işaretlidir, böylece eklentinin geçiş hareketi (varsayılan olarak Shift+NVDA+F4) veya Escape tuşuyla normal moda dönebilirsiniz.

Son not:  
Bazen bazı eklentiler formun bir veya daha fazla hareketini yakalayabilir. Umarım bunu başka bir form kullanarak veya theif eklentisinden hareketi kaldırarak halledebilirsiniz, çünkü şu ana kadar başka çözümüm yok.

### 1.1 için değişiklikler: ###

*	Günlükteki uyarı mesajlarından kurtulmak için gui.settingsDialogs import SettingsPanel'i kullanıldı.

### 1.0 için değişiklikler: ###

*	Benzer adlara sahip birçok eklenti olduğu için bu eklentinin adı: Sayısal Tuş Takımı İle Dolaşma olarak değiştirildi. Böylece, karışıklıklar önlenmiş oldu.
*	En son test edilen sürüm güncellendi. Böylece eklenti NVDA 2024.1 ile uyumlu hale getirildi.

### 0.9 için değişiklikler: ###

*	Sayı modunda 0 sayısının üçüncü ve dördüncü formlardaki konumuyla ilgili bir hata düzeltildi.
*	En son test edilen sürüm güncellendi. Böylece eklenti NVDA 2023.1 ile uyumlu hale getirildi.

### 0.8 için değişiklikler: ###

*	Sayısal mod, dolaşma modu veya her ikisi seçeneklerinden birini seçebileceğiniz bir seçim kutusu eklendi.
*	Yeni bir form eklendi(q w e, a s d, z x c) ve form1 olarak adlandırıldı.

### 0.7 için değişiklikler: ###

*	Eklenti için Portekizce çeviri eklendi.
*	Eklentinin varsayılan hareketi veya kısayolu değiştirildi; artık Shift+NVDA+F4 şeklindedir.

### 0.6 için değişiklikler: ###
Eklenti birçok yeni özellik eklenerek güncellendi:

*	Eklenti için bir ayar paneli eklendi.
*	Artık sayısal tuş takımı moduna benzetilecek üç form mevcuttur ve bunlardan birini seçebilirsiniz.
*	Sayı modu artık varsayılan olarak atlanmıştır ve bunu eklenti ayarlarından değiştirebilirsiniz.
*	Artık sayısal tuş takımı modunu Escape tuşuyla kapatabilirsiniz. Buna eklenti ayarlarından da erişilebilir ve değiştirilebilir.

### 0.5 için değişiklikler: ###

*	NVDA 2022.1 API'sıne uyum sağlamak için en son test edilen sürüm güncellendi.

### 0.4 için değişiklikler: ###

*	Türkçe dili eklendi.

### Katkıda Bulunanlar: ###

*	umut korkmaz, eklentinin Türkçe çevirisini desteklediğiniz için teşekkür ederiz.
*	Ângelo Abrantes, eklentinin Portekizce çevirisini desteklediğiniz için teşekkür ederiz.

[1]: https://github.com/ibrahim-s/navigateTheNumpadWay/releases/download/1.1/navigateTheNumpadWay-1.1.nvda-addon
