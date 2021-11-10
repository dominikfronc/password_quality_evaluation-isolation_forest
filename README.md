# Password quality evaluation

The aim of this project is to develop a password strength evaluator using isolation forest as a tool for detecting anomalies.

## Datasets
In order to accurately tell if a password is strong or not, we need a datasets of human used passwords to train our model.
We use these datasets:

### RockYou
- leak in 2009
- aprox. 14 mil. passwords

Dataset downloaded from [here](https://ulozto.sk/file/RZuEmmy7cKtP/rockyou-txt#!ZJD0ZGR2ZmtkLmR4ATEzL2DkZzAzMyO0F2Z2JaMFAUyBYJWyAD==).

### CrackStation
- combination of multiple leaked databases available on the web
- aprox. 64 mil. passwords

Dataset downloaded from [here](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm).

### SkullSecurity datasets
- multiple freely available datasets from different leaks
- elitehacker, facebook-pastebay, faithwriters, hak5, hotmail, myspace, phpbb,...

Datasets downloaded from [here](https://wiki.skullsecurity.org/index.php/Passwords).

### Dataset scripts
#### only_acsi.py
Script for cleaning dataset. Removes any lines that contain non-ASCII codes or lines longer than 40 characters.
To run:
```bash
python only_ascii.py input.txt > output.txt
```
After that manual conversion to UTF-8 encoding is needed.

#### metrics.py
Script for transfering dataset of passwords into .csv file containing metrics representation of passwords.

Metrics are following:
- password length
- number of lowercase characters
- number of uppercase characters
- number of digits
- number of special symbols
- number of continuous groups of characters

To run:
```bash
python metrics.py input.txt > output.csv
```