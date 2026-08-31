-- Yaqith Live Inventory Database Schema
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT UNIQUE,       -- عنوان الجهاز
    mac_address TEXT,             -- المعرف الفعلي
    vendor TEXT,                  -- الشركة المصنعة
    os_details TEXT,              -- نظام التشغيل
    first_seen TIMESTAMP,         -- وقت أول اكتشاف
    last_seen TIMESTAMP,          -- وقت آخر اتصال
    status TEXT                   -- الحالة (Online/Offline)
);
