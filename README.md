# قاعدة بيانات التعريفة الجمركية المصرية (Egyptian Customs Tariff Dataset) 🇪🇬

قاعدة بيانات متكاملة ومفتوحة المصدر لكافة بنود وأصناف التعريفة الجمركية المصرية وفقاً لمنظومة «نافذة» ومصلحة الجمارك المصرية.

---

## 📦 الصيغ المتوفرة في هذا المستودع (Available Formats)

1. **`egypt_customs_tariff.csv`**:
   * ملف إكسل CSV مشفر بـ `UTF-8 BOM` ليعمل في Microsoft Excel مباشرة وبدون أي تشويه للغة العربية.
2. **`egypt_customs_tariff.json`**:
   * هيكل بيانات JSON قياسي يضم الفصول والبنود وتفاصيل الرسوم الجمركية والقواعد الرقابية.
3. **`egypt_customs_tariff.sqlite`**:
   * قاعدة بيانات SQLite خفيفة ومدمجة ومجهزة بمحرك البحث الفوري **FTS5** (Full Text Search).
4. **`egypt_customs_tariff.sql`**:
   * ملف SQL DDL & DML متوافق مع MySQL و MariaDB جاهز للاستيراد المباشر بضغطة زر.

---

## 📊 محتويات البيانات (Dataset Schema)

| الحقل (Field) | النوع (Type) | الوصف (Description) |
|---|---|---|
| `item_code` | VARCHAR(10) | كود الصنف بالكامل (10 أرقام وفقاً للنظام المنسق المصري) |
| `item_name` | TEXT | المسمى التجاري والوصف العربي الدقيق للصنف |
| `chapter_code` | VARCHAR(2) | رقم الفصل الجمركي (من 01 إلى 99) |
| `chapter_name` | VARCHAR(255) | عنوان الفصل الجمركي |
| `heading_code` | VARCHAR(4) | كود البند الرئيسي المكون من 4 أرقام |
| `heading_name` | VARCHAR(500) | اسم البند الرئيسي |
| `import_duty` | VARCHAR(50) | نسبة ضريبة الوارد (الجمارك العامة) |
| `vat_rate` | VARCHAR(50) | نسبة ضريبة القيمة المضافة |
| `other_taxes` | TEXT | الرسوم الإضافية (رسم تنمية، ضريبة جدول، رسم موازنة إن وجد) |
| `rules_json` | JSON / TEXT | قائمة الشروط الرقابية، جهات الفحص (حجر بيطري، زراعي، رقابة) والاتفاقيات الدولية والتخفيضات |

---

## 🔍 أمثلة للاستخدام السريع (Quick Usage Examples)

### Python (باستخدام SQLite أو JSON)
```python
import sqlite3

conn = sqlite3.connect('egypt_customs_tariff.sqlite')
cursor = conn.cursor()

# بحث سريع عن سيارات الإسعاف
query = "إسعاف"
cursor.execute("SELECT item_code, item_name, import_duty, vat_rate FROM tariff_fts JOIN tariff_items ON tariff_fts.rowid = tariff_items.id WHERE tariff_fts MATCH ? LIMIT 10", (query,))

for row in cursor.fetchall():
    print(row)
```

---

## ⚖️ المصدر والترخيص
* **الاستعلام والبحث المباشر أونلاين:** يمكنك تجربة البحث السريع والفوري في كافة البنود عبر بوابة: [الاستعلام عن البنود والتعريفة الجمركية - موقع عاشور](https://ashorcc.com/tariff.php).
* **المصدر:** المنظومة القومية للنافذة الواحدة للتجارة الخارجية (نافذة - MTS) ومصلحة الجمارك المصرية وفقاً لقرار رئيس الجمهورية رقم 218 لسنة 2022 وتعديلاته.
* **إعداد ونشر:** أحمد عاشور للتخليص الجمركي ([ashorcc.com](https://ashorcc.com/)).
* **الترخيص:** مفتوح للاستخدام العام والتجاري مع الحفاظ على نسب المصدر (Open Data under CC-BY 4.0 / MIT).
