# VividHues :rainbow: :package:

[![VividHues](https://github.com/KennyOliver/VividHues/actions/workflows/python-publish.yml/badge.svg)](https://github.com/KennyOliver/VividHues/actions/workflows/python-publish.yml)

![CodeFactor](https://www.codefactor.io/repository/github/KennyOliver/vividHues/badge?style=for-the-badge)
![Latest SemVer](https://img.shields.io/github/v/tag/KennyOliver/vividHues?label=version&sort=semver&style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/KennyOliver/vividHues?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/KennyOliver/vividHues?style=for-the-badge)

<!-- [![repl](https://repl.it/badge/github/KennyOliver/vividHues)](https://repl.it/@KennyOliver/vividHues) -->

**VividHues: super lite package for colored strings in Python!**

<a href="https://pypi.org/project/VividHues/"><img src="https://img.shields.io/badge/PyPi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" /></a>
<a href="https://test.pypi.org/project/VividHues/"><img src="https://img.shields.io/badge/Test%20PyPi-white?style=for-the-badge&logo=pypi&logoColor=3775A9" /></a>

<img src="repo-imgs/vividhues-console-example.png" width="30%" align="none" />

---

## :hammer_and_wrench: Official Installation
##### Pop this command in your terminal to install VividHues.
```bash
pip install VividHues
```

### :bricks: Dependency
#### _requirements.txt_ (Highly Recommended!)
###### Append one of these versions to your Python packages requirements.txt.
```python
VividHues  # simple, but may be better to specify versions
```
```python
VividHues==3.0.0  # only has Clr codes
VividHues>=4.1.0  # adds: abbreviations & Magic Functions
VividHues>=5.2.0  # adds: Clr.pattern()
```

#### _Dependabot.yml_ (optional, but needs requirements.txt)
###### Create this file, to add your GitHub repo as a dependent.
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
```

#### _Dockerfile_ (optional)
###### If you have a Docker container. :whale2:
```dockerfile
# recommended
COPY requirements.txt .
RUN pip install -r requirements.txt
```
```dockerfile
# alternatively...
RUN pip install VividHues
```

---

## :snake: Python Example

<img src="repo-imgs/vividhues-console-example.png" width="30%" align="right" />

```python
print(Clr.BO + Clr.UL + Clr.rainbow('I love VividHues!') + Clr.RS)
print(f"{Clr.RED}It's got my fave color!{Clr.RS}")
print(f"Soooo {Clr.jazzy('jazzy') + Clr.RS}")
#                          ^^^
# you'll get an error using "" in f-string interpolations
print(Clr.pattern("Kenny Oliver", Clr.PURPLE, Clr.CYAN, Clr.LIME) + Clr.RS)
```

## :rainbow: Available Clr codes:
#### Just put a code in the gap ```Clr.___```

###### Clr: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; RED, ORANGE, YELLOW, LIME, GREEN, BLUE, CYAN, PURPLE, PINK, BLACK, WHITE
###### Formatter: &nbsp;&nbsp; UNDERLINE, UL, BOLD, BO, RESET, RS


### :magic_wand: Magic Functions

#### :game_die: Clr.random()
```python
print(Clr.random(string))
```
###### Paints your string in a random Clr code.

#### :saxophone: Clr.jazzy()
```python
print(Clr.jazzy(string))
```
###### Paints each letter in jazzy random colors! It's a total gamble, that's guaranteed to be ugly! :)

#### :rainbow: Clr.rainbow()
```python
print(Clr.rainbow(string))
```
###### Paints your string in a rainbow pattern.

#### :test_tube: Clr.pattern()
```python
print(Clr.pattern(string, *color))
```
###### Paint your letters in a repeating pattern, by specifying an unlimited amount of Clr codes!

---

## :muscle: How VividHues stacks up...
| Feature | [VividHues](https://pypi.org/project/VividHues/) | [Colorama](https://pypi.org/project/colorama/) | [termcolor](https://pypi.org/project/termcolor/) |
| :-----: | :-------: | :------: | :-------: |
| Simplicity/Abstraction | :star: | :star: | :star: |
| Font Colors | :star: | :star: | :star: |
| Background/Highlight | :soon: | :star: | :star: |
| Bold/Underline | :star: |  | :star: |
| Lightweight | :star: |  |  |
| Auto-Reset | :soon: | :star: |  |
| Cursor-Positioning |  | :star: |  |
| Special Features | :star: |  | :star: |
| <b>Total</b> | <b>5/8 + 2/8 = 7/8</b> | <b>5/8</b> | <b>5/8</b> |

This is why you should choose VividHues. Soon, it'll have more features than the leading competitors - in a smaller form factor.


---
Kenny Oliver ©2021
