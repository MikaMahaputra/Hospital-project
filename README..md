# CAPSTONE PROJECT MODULE 1

## Project Planning

### Participant Identity

| Field       | Information                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------- |
| Full Name   | Mikhael Mika Mahaputra                                                                                           |
| Case Study  | Data Pasien Rumah Sakit                                                                                          |
| Date        | 17 / 05 / 2026                                                                                                   |
| GitHub Repo | [https://github.com/MikaMahaputra/Hospital-Patient-Data](https://github.com/MikaMahaputra/Hospital-Patient-Data) |

---

# Project Goal

Before writing any code, this document answers the core planning questions for the application.
This planning document becomes the foundation for the application that will be developed during the project period.

---

# Ask Stage (6 Guiding Questions)

## 1. Who has the problem?

Staff rumah sakit, resepsionis, admin rumah sakit.

## 2. What is the problem?

Masalah bisnis yang dihadapi adalah pengelolaan data pasien masih dilakukan secara manual sehingga kurang efisien dan lebih rentan terhadap kesalahan.

## 3. How can your app solve the problem?

Aplikasi CRUD dapat membantu staff untuk menambah, melihat, mengupdate, dan menghapus data-data pasien.

## 4. How will users use your app?

User membuka menu aplikasi yaitu memilih fitur berdasarkan nomor yang diinput seperti melihat data pasien, membuat data, atau mengubah data.

## 5. Where is the data located?

Data disimpan di dalam memory program.

## 6. How is the data organized?

Data disusun menggunakan list yang berisi dictionary seperti di bagian data dummy. Tujuannya adalah untuk menyimpan data lebih mudah dengan field yang berbeda.

---

# Data Structure Design

## Main Collection / Variable

```python
patient_data = []
```

## Data Fields

| No | Field Name | Data Type | Example Value | Description                     |
| -- | ---------- | --------- | ------------- | ------------------------------- |
| 1  | patient_id | string    | "id001"       | Unique ID, cannot be duplicated |
| 2  | name       | string    | "Agus Putra"  | Patient name                    |
| 3  | age        | integer   | 22            | Patient age                     |
| 4  | gender     | string    | "Male"        | Patient gender                  |
| 5  | diagnosis  | string    | "Cold"        | Patient diagnosis               |

---

# Dummy Data Example

```python
patient_data = [
    {
        'patient_id': 'id001',
        'name': 'Agus Putra',
        'age': 22,
        'gender': 'Male',
        'diagnosis': 'Cold'
    },

    {
        'patient_id': 'id002',
        'name': 'Bob Builderman',
        'age': 35,
        'gender': 'Male',
        'diagnosis': 'Asthma'
    },

    {
        'patient_id': 'id003',
        'name': 'Tiara Citra',
        'age': 20,
        'gender': 'Female',
        'diagnosis': 'Flu'
    }
]
```

---

# Business Task Statement

Aplikasi ini dirancang untuk membantu staf administrasi rumah sakit yang mengalami kesulitan mengelola data pasien secara manual.

Project ini akan membantu proses pencatatan data pasien dengan sistem CRUD. Dengan CRUD, staff dapat menambah, membaca, mengupdate, dan menghapus data pasien dengan rapi dan mudah.

Batasan project saat ini yaitu data hanya disimpan sementara di dalam memory program.

---

#
