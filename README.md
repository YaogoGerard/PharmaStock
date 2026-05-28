# PharmaStock
#  Pharmacy Management System

A Python console application for managing pharmacy stock:  
medications, parapharmacy products, sales, expiration alerts, and low stock warnings.

---

##  How to Run the Project

**Prerequisites:** Python 3.10 or higher — no external modules required.

```bash
# 1. Clone the repository
git clone https://github.com/YaogoGerard/PharmaStock.git

# 2. Go to the project folder
cd PharmaStock

# 3. Run the program
python pharmacy.py
```

---

##  Features

- Display the entire stock with visual alerts
- Add a medication (with expiration date and prescription requirement)
- Add a parapharmacy product (with category)
- Sell a product with stock availability check
- Automatic alerts: expired medications and low stock
- Search for a product by name
- Automatic saving and loading of stock in CSV format

---

##  Technologies Used

- **Python 3.10+**
- Standard libraries: `csv`, `os`, `datetime`

---

##  Project Structure

```
YOUR_REPO/
├── pharmacie.py     # Main source code (classes + program)
├── stock.csv        # Stock backup file (auto-generated)
└── README.md        # This file
```

---

##  OOP Structure

| Class                    | Description                                      | Inherits from | Key Methods                     |
|--------------------------|--------------------------------------------------|---------------|---------------------------------|
| `Produit`                | Base generic product                             | —             | `afficher()`, `est_stock_faible()`, `vers_csv()` |
| `Medicament`             | Medication with prescription and expiration      | `Produit`     | `afficher()`, `est_expire()`    |
| `ProduitParapharmacie`   | Hygiene / cosmetic / nutrition product           | `Produit`     | `afficher()`, `get_categorie()` |

**The 4 OOP Principles:**
- **Encapsulation**: Private attributes (`__nom`, `__prix`, etc.) accessible via getters/setters
- **Abstraction**: The `afficher()` method hides internal complexity
- **Inheritance**: `Medicament` and `ProduitParapharmacie` extend `Produit`
- **Polymorphism**: `afficher()` behaves differently depending on the class

---

##  Group Members

| Name           | GitHub                                      |
|----------------|---------------------------------------------|
| YAOGO Gérard W | [@YaogoGerard](https://github.com/YaogoGerard)    |
| Traoré cheick | [@CAR-id13](https://github.com/CAR-id13)    |
| YAMEOGO Odette | [@odetteyameogo2002-sketch](https://github.com/odetteyameogo2002-sketch)    |
| TUINA Marina | [@tuinamarina28-png](https://github.com/tuinamarina28-png)    |
| Yams | [@Yams-tech](https://github.com/Yams-tech)    |
| YARO Leana | [@yaroleana7-maker](https://github.com/yaroleana7-maker)    |

---

##  Acknowledgments

- Official Python Documentation: https://docs.python.org
- BIT Course — Programming I with Python, Mrs. Kweyakie Afi Blebo
