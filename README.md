# Mini Learning Platform Demo (FastAPI)

## Overview
This project is a small **demo backend application** developed as part of a **technical pre-evaluation task**.

The goal of the project is **not to build a production-ready system**, but to demonstrate:
- Backend architectural thinking
- API design
- Payment flow simulation
- Basic matching logic similar to Udemy & Uber concepts

The application is built using **FastAPI** and uses **mock JSON data** instead of a real database.

---

## Technologies Used
- **Python 3**
- **FastAPI** – lightweight and modern backend framework
- **Uvicorn** – ASGI server
- **JSON files** – mock data storage
- **Swagger UI** – API testing and documentation

---

## User Roles
The system conceptually supports three basic roles:
- **User**
- **Instructor**
- **Admin**

Authentication is simulated using mock data.

---

## Mini Udemy Flow – Course Purchase
- Courses are listed with:
  - Title
  - Description
  - Instructor
  - Price
- Payment is **simulated**
- Payment can be **successful or failed**
- If payment is successful:
  - The course is assigned to the user
  - User can view purchased courses

---

## Mini Uber Logic – Live Lesson Matching
- User can create a **live lesson request**
- System assigns the **first available instructor**
- Instructor notification is simulated using logs (`print`)
- This structure is designed to be easily extendable

---

## Project Structure
```
Udemy-Uber_Demo/
 ├── app/
 │   ├── auth.py
 │   ├── courses.py
 │   ├── main.py
 │   └── matching.py
 └── data/
     ├── users.json
     ├── purchases.json
     ├── live_requests.json
     └── courses.json
 ├── requirements.txt
 └── README.md
```

---

## How to Run
```bash
pip install fastapi uvicorn
uvicorn app.main:app --reload
```

Then open:
```
http://127.0.0.1:8000/docs
```

---

## Scalability Notes
If this project were extended:
- Real database (PostgreSQL, MongoDB)
- JWT-based authentication
- Real payment providers (Stripe, iyzico)
- Queue-based notification system
- Instructor availability & rating-based matching

---

---

# Mini Eğitim Platformu Demo (FastAPI)

## Genel Bakış
Bu proje, **ön eleme mini proje görevi** kapsamında geliştirilmiş **küçük ölçekli bir backend demo uygulamasıdır**.

Amaç:
- Mimari düşünme becerisini göstermek
- API tasarım yaklaşımını sergilemek
- Ödeme ve eşleştirme mantığını simüle etmek

Gerçek veritabanı yerine **JSON dosyaları** kullanılmıştır.

---

## Kullanılan Teknolojiler
- **Python**
- **FastAPI**
- **Uvicorn**
- **JSON (mock data)**
- **Swagger UI**

---

## Roller
- Kullanıcı (User)
- Eğitmen (Instructor)
- Admin

Giriş işlemleri mock veri ile simüle edilmiştir.

---

## Eğitim Satın Alma (Mini Udemy)
- Eğitim listesi görüntülenebilir
- Ödeme işlemi simüle edilmiştir
- Ödeme:
  - Başarılı olabilir
  - Başarısız olabilir
- Başarılı ödeme sonrası eğitim kullanıcıya tanımlanır

---

## Canlı Ders Eşleştirme (Mini Uber Mantığı)
- Kullanıcı canlı ders talebi oluşturur
- Sistem uygun eğitmeni otomatik atar
- Eğitmene bildirim simüle edilir (log)

---

## Çalıştırma
```bash
uvicorn app.main:app --reload
```

Swagger:
```
http://127.0.0.1:8000/docs
```

---

## Not
Bu proje **demo amaçlıdır** ve geliştirilmeye açık bir mimari ile hazırlanmıştır.
