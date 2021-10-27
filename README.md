# Password quality evaluation

The aim of this project is to develop a password strength evaluator using isolation forest as a tool for detecting anomalies.

## Datasets
In order to accurately tell if a password is strong or not, we need a datasets of human used passwords to train our model.
We use these datasets:

### RockYou
- leak in 2009
- aprox. 14 mil. passwords

Dataset downloaded from [here](https://ulozto.sk/file/RZuEmmy7cKtP/rockyou-txt#!ZJD0ZGR2ZmtkLmR4ATEzL2DkZzAzMyO0F2Z2JaMFAUyBYJWyAD==).

### MySpace
- captured via phishing in 2006
- aprox. 37 000 passwords

Dataset downloaded from [here](https://wiki.skullsecurity.org/index.php/Passwords).

### CrackStation
- combination of multiple leaked databases available on the web
- aprox. 64 mil. passwords

Dataset downloaded from [here](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm).
