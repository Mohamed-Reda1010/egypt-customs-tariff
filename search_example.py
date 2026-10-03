"""
مثال سريع للبحث في قاعدة بيانات التعريفة الجمركية المصرية (SQLite + FTS5)
Quick example to search the Egyptian Customs Tariff SQLite database with Full-Text Search.
"""

import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

def search_tariff(db_path, query, limit=10):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print(f"\n🔍 نتائج البحث عن: '{query}'")
    print("=" * 70)

    # Check if query is numeric (Code search)
    if query.replace('.', '').replace('-', '').isdigit():
        sql = """
        SELECT item_code, item_name, chapter_name, import_duty, vat_rate 
        FROM tariff_items 
        WHERE item_code LIKE ? OR heading_code = ?
        LIMIT ?
        """
        cur.execute(sql, (f"{query}%", query, limit))
    else:
        # Full-Text Search using FTS5
        sql = """
        SELECT t.item_code, t.item_name, t.chapter_name, t.import_duty, t.vat_rate 
        FROM tariff_fts f
        JOIN tariff_items t ON f.rowid = t.id
        WHERE tariff_fts MATCH ?
        LIMIT ?
        """
        cur.execute(sql, (query, limit))

    rows = cur.fetchall()
    if not rows:
        print("❌ لم يتم العثور على نتائج.")
    else:
        for r in rows:
            print(f"📦 كود: {r[0]} | ضريبة الوارد: {r[3] or 'حسب النظام'} | قيمة مضافة: {r[4] or '0%'}")
            print(f"   الوصف: {r[1]}")
            print(f"   الفصل: {r[2]}")
            print("-" * 70)

    conn.close()

if __name__ == '__main__':
    db_file = 'egypt_customs_tariff.sqlite'
    # Test searches
    search_tariff(db_file, 'سيارات')
    search_tariff(db_file, '8703')
