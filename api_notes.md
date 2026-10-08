# API Notes

| Адрес | Метод | Код ответа |
|---|---|---:|
| `/api/tours/` | GET | 200 |
| `/api/tours/` | POST | 201 |
| `/api/tours/1/` | GET | 200 |
| `/api/tours/1/` | PATCH | 200 |
| `/api/tours/1/` | PUT | 200 |
| `/api/tours/1/` | DELETE | 204 |
| `/api/tours/999/` | GET | 404 |
| `/api/tours/999/` | DELETE | 404 |
| `/api/categories/` | GET | 200 |
| `/api/categories/` | POST | 201 |
| `/api/categories/1/` | GET | 200 |
| `/api/categories/1/tours/` | GET | 200 |
| `/api/tours/` | POST с некорректной ценой | 400 |
| `/api/tours/` | POST с коротким названием | 400 |