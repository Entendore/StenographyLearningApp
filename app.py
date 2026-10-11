        #!/usr/bin/env python3
"""
Stenography Learning Application
A comprehensive tool for learning machine shorthand (stenography)
Built with PySide6
"""

import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QPushButton, QTextEdit, QLineEdit,
    QStackedWidget, QListWidget, QGroupBox, QProgressBar,
    QFrame, QScrollArea, QSizePolicy, QMessageBox,
    QRadioButton, QButtonGroup, QSplitter, QTabWidget, QSpacerItem
)
from PySide6.QtCore import Qt, QSize, Signal, QTimer, QRectF
from PySide6.QtGui import (
    QFont, QColor, QPainter, QPen, QBrush, QLinearGradient,
    QPalette, QAction, QIcon, QRadialGradient
)

# ==================== STENO DATA ====================

LEFT_KEYS = ['S', 'T', 'K', 'P', 'W', 'H', 'R']
VOWEL_KEYS = ['A', 'O', 'E', 'U']
RIGHT_KEYS = ['F', 'R', 'P', 'B', 'L', 'G', 'T', 'S', 'D', 'Z']

STENO_DICT = {
    'the': '-T', 'a': 'AEU', 'an': 'A', 'I': 'EU', 'you': 'U',
    'he': 'HE', 'she': 'SHE', 'it': 'T', 'we': 'WE', 'they': 'THE',
    'me': 'PHAOE', 'him': 'HEUPL', 'her': 'HER', 'us': 'US',
    'them': 'THEPL', 'my': 'PHAOEU', 'your': 'KWROUR', 'his': 'H-S',
    'our': 'OUR', 'this': 'TH', 'that': 'THAT', 'these': 'THAOES',
    'those': 'THOS', 'is': 'S', 'are': 'R', 'was': 'WAS', 'were': 'WR',
    'be': '-B', 'been': 'PW-B', 'have': 'SR', 'has': 'H-S', 'had': 'H',
    'do': 'TKO', 'did': 'TK', 'does': 'TKOS', 'will': 'HR',
    'would': 'WOULD', 'can': 'K', 'could': 'KO', 'should': 'SHO',
    'may': 'PHAE', 'must': 'PHUFT', 'say': 'SAEU', 'said': 'SAED',
    'tell': 'TEL', 'told': 'TOLD', 'know': 'TPHO', 'think': 'THEUPBG',
    'feel': 'TPAOEL', 'find': 'TPAEUPBD', 'give': 'TKPW', 'take': 'TAEUBG',
    'come': 'KPH', 'go': 'TKPW', 'make': 'PHAEUBG', 'keep': 'KAOEP',
    'get': 'TKPWET', 'put': 'PUT', 'see': 'SAOE', 'want': 'WAPBT',
    'need': 'TPHAOED', 'like': 'HRAOEUBG', 'love': 'HROF', 'help': 'HEP',
    'use': 'AOUS', 'work': 'WORBG', 'play': 'PHRAEU', 'run': 'RUPB',
    'walk': 'WAUBG', 'live': 'HREUFT', 'write': 'WRAOEUT', 'read': 'RAOED',
    'learn': 'HRERPBL', 'teach': 'TAEFP', 'try': 'TREU', 'start': 'START',
    'stop': 'STOP', 'move': 'PHOF', 'call': 'KAUL', 'ask': 'SK',
    'show': 'SHOE', 'hear': 'HAOER', 'watch': 'WAFP', 'and': 'SKP',
    'but': 'PWUT', 'or': 'OR', 'so': 'SO', 'if': 'TP', 'to': 'TO',
    'from': 'TPR', 'with': 'W', 'for': 'TPOR', 'of': '-F', 'in': 'TPH',
    'on': 'OPB', 'at': 'AT', 'by': 'PWREU', 'about': 'PW-BT',
    'into': 'TPHAO', 'through': 'THRU', 'over': 'OEFR', 'after': 'AF',
    'before': 'PW-F', 'between': 'TWAOEPB', 'under': 'UPBD', 'up': 'UP',
    'down': 'TKOUPB', 'out': 'OUT', 'off': 'OF', 'good': 'TKPWAOED',
    'great': 'TKPWRAET', 'right': 'RAOEUT', 'big': 'PWIG',
    'small': 'SPHAUL', 'long': 'HROPG', 'high': 'HAEU', 'hot': 'HOT',
    'cold': 'KOLD', 'fast': 'TAPFT', 'slow': 'SHROE', 'hard': 'HARD',
    'easy': 'ES', 'full': 'TPAUL', 'new': 'TPHU', 'old': 'OLD',
    'first': 'TPEURS', 'last': 'HRAFT', 'next': 'TPHEGT', 'own': 'OEPB',
    'all': 'AUL', 'each': 'AOEFP', 'every': 'EFR', 'some': 'SPL',
    'any': 'TPHEU', 'many': 'PHAEPB', 'much': 'PHUFP', 'more': 'PHOR',
    'most': 'PHOFT', 'less': 'HRES', 'other': 'OER', 'same': 'SAEPL',
    'different': 'TKEFTPBT', 'just': 'SKWRUFT', 'also': 'HR-S',
    'very': 'SRE', 'still': 'STEUL', 'always': 'AULZ', 'never': 'TPHEF',
    'only': 'OEPBL', 'again': 'TKPWEPB', 'well': 'WEL', 'now': 'TPHOU',
    'then': 'THEPB', 'there': 'THR', 'here': 'HAOER', 'not': 'TPHOT',
    'no': 'TPHO', 'yes': 'KWRE', 'what': 'WHA', 'when': 'WHEPB',
    'where': 'WHR', 'why': 'KWREU', 'how': 'HOU', 'who': 'WHO',
    'house': 'HOUS', 'home': 'HOEPL', 'world': 'WORLD', 'life': 'HRAOEUF',
    'time': 'TAEUPL', 'year': 'KWRAOER', 'day': 'TKAEU',
    'night': 'TPHAEUT', 'week': 'WAOEBG', 'man': 'PHAPB', 'woman': 'WOPL',
    'child': 'KHAOEULD', 'people': 'PAOEPL', 'water': 'WAUR',
    'food': 'TAOPD', 'hand': 'HAPBD', 'head': 'HED', 'eye': 'AOEU',
    'door': 'TKOR', 'room': 'RAOPL', 'book': 'PWAOBG', 'word': 'WORD',
    'place': 'PHRAEUS', 'name': 'TPHAEUPL', 'part': 'PART', 'end': 'EPBD',
    'side': 'SAOEUD', 'thing': 'THEUPBG', 'way': 'WAEU',
    'school': 'SKOOL', 'family': 'TPAEPL', 'friend': 'TPREPBD',
    'country': 'KREU', 'group': 'TKPWRAOUP', 'number': 'TPHURPB',
    'problem': 'PROBL', 'fact': 'TPABGT', 'power': 'POUR',
    'money': 'PHOPB', 'story': 'STOER', 'car': 'KAR', 'phone': 'TPOPB',
    'game': 'TKPWAEUPL', 'street': 'STRAOET', 'morning': 'PHORPBG',
    'evening': 'AOEPG', 'paper': 'PAEUR', 'question': 'KW-BGS',
    'answer': 'APBS', 'example': 'KP-PL', 'idea': 'EU', 'back': 'PWABG',
    'point': 'POEUPBT',
}

LESSONS = [
    {
        'title': '📖 Introduction to Stenography',
        'desc': 'What is stenography and how does it work?',
        'content': """<h2>What is Stenography?</h2>
<p>Stenography (machine shorthand) is a method of rapid writing using a stenotype machine.
Court reporters, live captioners, and others use stenography to type at <b>200+ words per minute</b>.</p>

<h3>How is it Different from Regular Typing?</h3>
<p>On a standard keyboard, you type one letter at a time. On a steno keyboard, you press
multiple keys <b>simultaneously</b> (called a "chord") to produce whole words or syllables.</p>

<h3>The Steno Keyboard</h3>
<p>A steno keyboard has only <b>22 keys</b> arranged in a specific layout:</p>
<ul>
<li><b style="color:#64b5f6">Left hand</b> (7 keys): S T K P W H R — Initial consonants</li>
<li><b style="color:#ffd54f">Thumbs</b> (4 keys): A O E U — Vowels</li>
<li><b style="color:#81c784">Right hand</b> (10 keys): F R P B L G T S D Z — Final consonants</li>
</ul>

<h3>Steno Order</h3>
<p>Keys are always pressed in a specific order:
<b>S-T-K-P-W-H-R-A-O-E-U-F-R-P-B-L-G-T-S-D-Z</b></p>
<p>No matter which keys you press simultaneously, they will always be read in this order.</p>

<h3>Chords = Words</h3>
<p>A "stroke" or "chord" is the result of pressing one or more keys simultaneously.
For example, pressing T + P + H + O produces "no" — because T+P+H makes the "n" sound,
and O makes the "o" sound.</p>

<p>➡️ Move to the next lesson to learn about the keyboard layout in detail!</p>"""
    },
    {
        'title': '⌨️ Left Hand Keys',
        'desc': 'Learn the left hand consonant keys: S, T, K, P, W, H, R',
        'content': """<h2>Left Hand Keys</h2>
<p>The left hand controls 7 keys that produce <b>initial consonant</b> sounds:</p>

<table border="1" cellpadding="6" style="border-collapse:collapse;">
<tr style="background:#37474f"><th>Key</th><th>Sound</th><th>Example</th></tr>
<tr><td><b>S</b></td><td>s</td><td>sun, see</td></tr>
<tr><td><b>T</b></td><td>t</td><td>top, ten</td></tr>
<tr><td><b>K</b></td><td>k</td><td>cat, key</td></tr>
<tr><td><b>P</b></td><td>p</td><td>put, pen</td></tr>
<tr><td><b>W</b></td><td>w</td><td>we, will</td></tr>
<tr><td><b>H</b></td><td>h</td><td>he, how</td></tr>
<tr><td><b>R</b></td><td>r</td><td>run, red</td></tr>
</table>

<h3>Key Combinations Produce New Sounds!</h3>
<table border="1" cellpadding="6" style="border-collapse:collapse;">
<tr style="background:#37474f"><th>Keys</th><th>Sound</th><th>Example</th></tr>
<tr><td><b>T + P</b></td><td>f</td><td>for, find</td></tr>
<tr><td><b>T + K</b></td><td>d</td><td>do, day</td></tr>
<tr><td><b>P + W</b></td><td>b</td><td>but, big</td></tr>
<tr><td><b>T + P + W</b></td><td>v</td><td>very, have</td></tr>
<tr><td><b>T + P + H</b></td><td>n</td><td>not, no</td></tr>
<tr><td><b>K + P + W</b></td><td>g (hard)</td><td>go, get</td></tr>
<tr><td><b>S + T + P + H</b></td><td>m</td><td>me, my</td></tr>
<tr><td><b>H + R</b></td><td>l</td><td>like, long</td></tr>
<tr><td><b>S + H</b></td><td>sh</td><td>she, show</td></tr>
<tr><td><b>T + H</b></td><td>th</td><td>the, that</td></tr>
<tr><td><b>S + T + K + P + W</b></td><td>j</td><td>just, job</td></tr>
<tr><td><b>S + T + K + W + R</b></td><td>y</td><td>you, yes</td></tr>
</table>

<p>💡 Try clicking these keys on the <b>Keyboard</b> tab to see the strokes!</p>""",
        'exercises': [
            {'word': 'sun', 'stroke': 'S', 'hint': 'Just the S key'},
            {'word': 'top', 'stroke': 'T', 'hint': 'Just the T key'},
            {'word': 'cat', 'stroke': 'K', 'hint': 'K key for k sound'},
            {'word': 'no', 'stroke': 'TPH', 'hint': 'T+P+H = n sound'},
            {'word': 'for', 'stroke': 'TP', 'hint': 'T+P = f sound'},
            {'word': 'big', 'stroke': 'PW', 'hint': 'P+W = b sound'},
            {'word': 'do', 'stroke': 'TK', 'hint': 'T+K = d sound'},
        ]
    },
    {
        'title': '🔤 Vowel Keys',
        'desc': 'Learn the vowel keys: A, O, E, U and their combinations',
        'content': """<h2>Vowel Keys</h2>
<p>The thumbs control 4 vowel keys. Combinations create different vowel sounds:</p>

<table border="1" cellpadding="6" style="border-collapse:collapse;">
<tr style="background:#37474f"><th>Key(s)</th><th>Sound</th><th>Example</th></tr>
<tr><td><b>A</b></td><td>short a</td><td>cat, hat</td></tr>
<tr><td><b>O</b></td><td>short o</td><td>hot, not</td></tr>
<tr><td><b>E</b></td><td>short e</td><td>pet, let</td></tr>
<tr><td><b>U</b></td><td>short u</td><td>cup, up</td></tr>
<tr><td><b>A + O</b></td><td>aw/ah</td><td>all, call</td></tr>
<tr><td><b>A + E</b></td><td>long a</td><td>day, make</td></tr>
<tr><td><b>A + U</b></td><td>ow</td><td>out, how</td></tr>
<tr><td><b>O + E</b></td><td>long o</td><td>go, know</td></tr>
<tr><td><b>O + U</b></td><td>oo</td><td>food, you</td></tr>
<tr><td><b>E + U</b></td><td>long e</td><td>me, I</td></tr>
<tr><td><b>A + E + U</b></td><td>long i</td><td>high, my</td></tr>
</table>

<h3>Important Vowel Patterns</h3>
<ul>
<li><b>AEU</b> = long "a" as in "day"</li>
<li><b>AOE</b> = long "e" as in "see"</li>
<li><b>OE</b> = long "o" as in "go"</li>
<li><b>OU</b> = "oo" as in "food"</li>
<li><b>EU</b> = long "e" as in "me" / also used for "I"</li>
</ul>""",
        'exercises': [
            {'word': 'a', 'stroke': 'AEU', 'hint': 'A+E+U = long a'},
            {'word': 'I', 'stroke': 'EU', 'hint': 'E+U = long e / I'},
            {'word': 'out', 'stroke': 'OUT', 'hint': 'A+U = ow + T'},
            {'word': 'up', 'stroke': 'UP', 'hint': 'U + P'},
            {'word': 'all', 'stroke': 'AUL', 'hint': 'A+O = aw + L'},
            {'word': 'you', 'stroke': 'U', 'hint': 'O+U = oo → brief form U'},
        ]
    },
    {
        'title': '👉 Right Hand Keys',
        'desc': 'Learn the right hand consonant keys: F, R, P, B, L, G, T, S, D, Z',
        'content': """<h2>Right Hand Keys</h2>
<p>The right hand controls 10 keys that produce <b>final consonant</b> sounds:</p>

<table border="1" cellpadding="6" style="border-collapse:collapse;">
<tr style="background:#37474f"><th>Key</th><th>Sound</th><th>Example</th></tr>
<tr><td><b>-F</b></td><td>f</td><td>off, if</td></tr>
<tr><td><b>-R</b></td><td>r</td><td>or, her</td></tr>
<tr><td><b>-P</b></td><td>p</td><td>up, top</td></tr>
<tr><td><b>-B</b></td><td>b</td><td>about, lab</td></tr>
<tr><td><b>-L</b></td><td>l</td><td>will, all</td></tr>
<tr><td><b>-G</b></td><td>ng</td><td>long, thing</td></tr>
<tr><td><b>-T</b></td><td>t</td><td>it, not</td></tr>
<tr><td><b>-S</b></td><td>s</td><td>is, this</td></tr>
<tr><td><b>-D</b></td><td>d</td><td>had, did</td></tr>
<tr><td><b>-Z</b></td><td>z</td><td>was, is</td></tr>
</table>

<h3>Right Hand Combinations</h3>
<table border="1" cellpadding="6" style="border-collapse:collapse;">
<tr style="background:#37474f"><th>Keys</th><th>Sound</th><th>Example</th></tr>
<tr><td><b>-P + -B</b></td><td>sh</td><td>she, which</td></tr>
<tr><td><b>-F + -P</b></td><td>ch</td><td>each, much</td></tr>
<tr><td><b>-F + -R</b></td><td>v</td><td>have, very</td></tr>
<tr><td><b>-B + -L</b></td><td>bl</td><td>able, table</td></tr>
<tr><td><b>-P + -L</b></td><td>pl</td><td>people, simple</td></tr>
<tr><td><b>-F + -L</b></td><td>fl</td><td>beautiful</td></tr>
<tr><td><b>-L + -G</b></td><td>lg</td><td>village</td></tr>
<tr><td><b>-T + -S</b></td><td>ts</td><td>its, that's</td></tr>
<tr><td><b>-G + -S</b></td><td>ngs</td><td>things</td></tr>
<tr><td><b>-B + -G</b></td><td>bk</td><td>bank</td></tr>
</table>

<p>💡 In steno notation, right-hand keys are sometimes written with a dash prefix
(e.g., <b>-F</b>, <b>-R</b>) to distinguish them from left-hand keys with the same letter.</p>""",
        'exercises': [
            {'word': 'it', 'stroke': 'T', 'hint': 'Just T (brief form)'},
            {'word': 'is', 'stroke': 'S', 'hint': 'Just S (brief form)'},
            {'word': 'not', 'stroke': 'TPHOT', 'hint': 'TPH(n) + O + T'},
            {'word': 'all', 'stroke': 'AUL', 'hint': 'A+O(aw) + L'},
            {'word': 'will', 'stroke': 'HR', 'hint': 'HR(l) + L (brief form)'},
        ]
    },
    {
        'title': '🔗 Complete Strokes',
        'desc': 'Combine left hand + vowels + right hand to make words',
        'content': """<h2>Building Complete Strokes</h2>
<p>A complete steno stroke combines:</p>
<ol>
<li><b style="color:#64b5f6">Initial consonants</b> (left hand)</li>
<li><b style="color:#ffd54f">Vowels</b> (thumbs)</li>
<li><b style="color:#81c784">Final consonants</b> (right hand)</li>
</ol>

<h3>Examples</h3>
<table border="1" cellpadding="6" style="border-collapse:collapse;">
<tr style="background:#37474f"><th>Word</th><th>Stroke</th><th>Breakdown</th></tr>
<tr><td>the</td><td>-T</td><td>(none) + (none) + T</td></tr>
<tr><td>that</td><td>THAT</td><td>TH + A + T</td></tr>
<tr><td>for</td><td>TPOR</td><td>TP(f) + O + R</td></tr>
<tr><td>not</td><td>TPHOT</td><td>TPH(n) + O + T</td></tr>
<tr><td>but</td><td>PWUT</td><td>PW(b) + U + T</td></tr>
<tr><td>she</td><td>SHE</td><td>SH + E</td></tr>
<tr><td>they</td><td>THE</td><td>TH + E</td></tr>
<tr><td>and</td><td>SKP</td><td>S+K+P (brief form)</td></tr>
<tr><td>have</td><td>SR</td><td>S+R (brief form)</td></tr>
<tr><td>with</td><td>W</td><td>W (brief form)</td></tr>
</table>

<h3>Stroke Notation</h3>
<ul>
<li>A dash prefix means right-hand only: <b>-T</b> = just right T</li>
<li>A dash suffix means left-hand only: <b>W-</b> or just <b>W</b> = just left W</li>
<li>Full stroke: <b>TPHOT</b> = left TPH + vowel O + right T</li>
</ul>""",
        'exercises': [
            {'word': 'the', 'stroke': '-T', 'hint': 'Right T only'},
            {'word': 'that', 'stroke': 'THAT', 'hint': 'TH + A + T'},
            {'word': 'for', 'stroke': 'TPOR', 'hint': 'TP(f) + O + R'},
            {'word': 'not', 'stroke': 'TPHOT', 'hint': 'TPH(n) + O + T'},
            {'word': 'but', 'stroke': 'PWUT', 'hint': 'PW(b) + U + T'},
            {'word': 'she', 'stroke': 'SHE', 'hint': 'SH + E'},
            {'word': 'have', 'stroke': 'SR', 'hint': 'Brief form: S+R'},
        ]
    },
    {
        'title': '⚡ Brief Forms',
        'desc': 'Learn common brief forms for maximum speed',
        'content': """<h2>Brief Forms</h2>
<p>Brief forms are shortened strokes for common words. They are essential for speed!</p>

<table border="1" cellpadding="6" style="border-collapse:collapse;">
<tr style="background:#37474f"><th>Word</th><th>Brief Form</th><th>Explanation</th></tr>
<tr><td>the</td><td>-T</td><td>Just right T</td></tr>
<tr><td>and</td><td>SKP</td><td>S+K+P</td></tr>
<tr><td>is</td><td>S</td><td>Just S</td></tr>
<tr><td>are</td><td>R</td><td>Just R</td></tr>
<tr><td>have</td><td>SR</td><td>S+R</td></tr>
<tr><td>with</td><td>W</td><td>Just W</td></tr>
<tr><td>can</td><td>K</td><td>Just K</td></tr>
<tr><td>will</td><td>HR</td><td>H+R</td></tr>
<tr><td>of</td><td>-F</td><td>Just right F</td></tr>
<tr><td>it</td><td>T</td><td>Just T</td></tr>
<tr><td>in</td><td>TPH</td><td>T+P+H</td></tr>
<tr><td>to</td><td>TO</td><td>T+O</td></tr>
<tr><td>had</td><td>H</td><td>Just H</td></tr>
<tr><td>do</td><td>TKO</td><td>T+K+O</td></tr>
<tr><td>not</td><td>TPHOT</td><td>T+P+H+O+T</td></tr>
<tr><td>be</td><td>-B</td><td>Just right B</td></tr>
<tr><td>he</td><td>HE</td><td>H+E</td></tr>
<tr><td>we</td><td>WE</td><td>W+E</td></tr>
<tr><td>go</td><td>TKPW</td><td>T+K+P+W = g</td></tr>
<tr><td>give</td><td>TKPW</td><td>Same as "go" — context determines</td></tr>
</table>

<h3>Why Brief Forms Matter</h3>
<ul>
<li>⏩ Faster writing speed — fewer keys per word</li>
<li>👌 Less finger movement — reduced fatigue</li>
<li>📈 Common words make up ~50% of everyday text</li>
</ul>

<p>💡 Practice these until they become automatic!</p>""",
        'exercises': [
            {'word': 'the', 'stroke': '-T', 'hint': 'Brief: right T'},
            {'word': 'and', 'stroke': 'SKP', 'hint': 'Brief: S+K+P'},
            {'word': 'have', 'stroke': 'SR', 'hint': 'Brief: S+R'},
            {'word': 'with', 'stroke': 'W', 'hint': 'Brief: just W'},
            {'word': 'will', 'stroke': 'HR', 'hint': 'Brief: H+R'},
            {'word': 'of', 'stroke': '-F', 'hint': 'Brief: right F'},
            {'word': 'can', 'stroke': 'K', 'hint': 'Brief: just K'},
            {'word': 'it', 'stroke': 'T', 'hint': 'Brief: just T'},
            {'word': 'be', 'stroke': '-B', 'hint': 'Brief: right B'},
            {'word': 'had', 'stroke': 'H', 'hint': 'Brief: just H'},
        ]
    },
]

# ==================== STYLESHEET ====================

DARK_STYLESHEET = """
QMainWindow {
    background-color: #1a1a2e;
}
QWidget {
    background-color: #1a1a2e;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QListWidget {
    background-color: #16213e;
    border: none;
    border-radius: 8px;
    padding: 5px;
    font-size: 14px;
}
QListWidget::item {
    padding: 12px 16px;
    border-radius: 6px;
    margin: 2px 4px;
    color: #b0bec5;
}
QListWidget::item:selected {
    background-color: #0f3460;
    color: #64b5f6;
    font-weight: bold;
}
QListWidget::item:hover {
    background-color: #1a2744;
    color: #e0e0e0;
}
QPushButton {
    background-color: #0f3460;
    color: #e0e0e0;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #1a4a8a;
}
QPushButton:pressed {
    background-color: #0a2540;
}
QPushButton:disabled {
    background-color: #2a2a3e;
    color: #555;
}
QPushButton#accentBtn {
    background-color: #e94560;
    color: white;
    font-size: 15px;
}
QPushButton#accentBtn:hover {
    background-color: #ff6b81;
}
QPushButton#keyBtn {
    background-color: #16213e;
    color: #e0e0e0;
    border: 2px solid #2a3a5e;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
    min-width: 52px;
    min-height: 52px;
    max-width: 52px;
    max-height: 52px;
}
QPushButton#keyBtn:hover {
    background-color: #1a2744;
    border-color: #64b5f6;
}
QPushButton#keyBtn[active="true"] {
    background-color: #e94560;
    color: white;
    border-color: #ff6b81;
}
QPushButton#leftKeyBtn {
    background-color: #1a2744;
    color: #64b5f6;
    border: 2px solid #2a4a7e;
}
QPushButton#leftKeyBtn[active="true"] {
    background-color: #1565c0;
    color: white;
    border-color: #64b5f6;
}
QPushButton#vowelKeyBtn {
    background-color: #2a2a1e;
    color: #ffd54f;
    border: 2px solid #5a4a1e;
}
QPushButton#vowelKeyBtn[active="true"] {
    background-color: #f9a825;
    color: #1a1a2e;
    border-color: #ffd54f;
}
QPushButton#rightKeyBtn {
    background-color: #1a2e1a;
    color: #81c784;
    border: 2px solid #2e5e2e;
}
QPushButton#rightKeyBtn[active="true"] {
    background-color: #2e7d32;
    color: white;
    border-color: #81c784;
}
QTextEdit {
    background-color: #16213e;
    color: #e0e0e0;
    border: 1px solid #2a3a5e;
    border-radius: 8px;
    padding: 16px;
    font-size: 14px;
    selection-background-color: #0f3460;
}
QLineEdit {
    background-color: #16213e;
    color: #e0e0e0;
    border: 2px solid #2a3a5e;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 16px;
    font-weight: bold;
}
QLineEdit:focus {
    border-color: #e94560;
}
QProgressBar {
    background-color: #16213e;
    border: none;
    border-radius: 8px;
    text-align: center;
    color: #e0e0e0;
    font-weight: bold;
    min-height: 24px;
}
QProgressBar::chunk {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #e94560, stop:1 #ff6b81);
    border-radius: 8px;
}
QGroupBox {
    background-color: #16213e;
    border: 1px solid #2a3a5e;
    border-radius: 10px;
    margin-top: 16px;
    padding: 20px;
    padding-top: 30px;
    font-size: 14px;
    font-weight: bold;
    color: #64b5f6;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 16px;
    padding: 0 8px;
}
QLabel#titleLabel {
    font-size: 28px;
    font-weight: bold;
    color: #e94560;
}
QLabel#subtitleLabel {
    font-size: 16px;
    color: #b0bec5;
}
QLabel#strokeLabel {
    font-size: 32px;
    font-weight: bold;
    color: #ffd54f;
    font-family: 'Consolas', 'Courier New', monospace;
}
QLabel#wordLabel {
    font-size: 36px;
    font-weight: bold;
    color: #64b5f6;
}
QLabel#correctLabel {
    font-size: 20px;
    font-weight: bold;
    color: #81c784;
}
QLabel#wrongLabel {
    font-size: 20px;
    font-weight: bold;
    color: #e94560;
}
QScrollArea {
    border: none;
    background-color: transparent;
}
QRadioButton {
    font-size: 14px;
    color: #e0e0e0;
    spacing: 8px;
}
QRadioButton::indicator {
    width: 18px;
    height: 18px;
}
QFrame#separator {
    background-color: #2a3a5e;
    max-height: 1px;
}
"""


# ==================== STENO KEYBOARD WIDGET ====================

class StenoKeyboardWidget(QWidget):
    """Interactive steno keyboard visualization widget."""
    stroke_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.active_keys = set()
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        # Title
        title = QLabel("🎹 Steno Keyboard")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #64b5f6; padding: 4px;")
        layout.addWidget(title)

        # Stroke display
        self.stroke_label = QLabel("—")
        self.stroke_label.setObjectName("strokeLabel")
        self.stroke_label.setAlignment(Qt.AlignCenter)
        self.stroke_label.setStyleSheet(
            "font-size: 28px; font-weight: bold; color: #ffd54f; "
            "font-family: 'Consolas', monospace; padding: 8px; "
            "background-color: #16213e; border-radius: 10px; border: 2px solid #2a3a5e;"
        )
        layout.addWidget(self.stroke_label)

        # Keyboard grid
        kb_layout = QGridLayout()
        kb_layout.setSpacing(4)

        # Left hand keys - Row 1
        self.key_buttons = {}
        left_row1 = ['S', 'T', 'K', 'P']
        left_row2 = ['S', 'W', 'H', 'R']

        # Row 1: Left hand top
        for i, key in enumerate(['S', 'T', 'K', 'P']):
            btn = QPushButton(key)
            btn.setObjectName("leftKeyBtn")
            btn.setProperty("key_group", "left")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedSize(56, 56)
            btn.clicked.connect(lambda checked, k=key: self._toggle_key(k))
            kb_layout.addWidget(btn, 0, i)
            self.key_buttons[('left', key)] = btn

        # Spacer
        spacer = QSpacerItem(8, 56)
        kb_layout.addItem(spacer, 0, 4)

        # Row 1: Right hand top
        right_keys_layout = [
            (0, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
        ]
        right_row = ['F', 'R', 'P', 'B', 'L', 'G', 'T', 'S', 'D', 'Z']
        for i, key in enumerate(right_row):
            btn = QPushButton(key)
            btn.setObjectName("rightKeyBtn")
            btn.setProperty("key_group", "right")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedSize(48, 56)
            btn.clicked.connect(lambda checked, k=key: self._toggle_key(k))
            kb_layout.addWidget(btn, 0, i + 5)
            self.key_buttons[('right', key)] = btn

        # Row 2: Left hand bottom
        btn_w = QPushButton("W")
        btn_w.setObjectName("leftKeyBtn")
        btn_w.setProperty("key_group", "left")
        btn_w.setCursor(Qt.PointingHandCursor)
        btn_w.setFixedSize(56, 56)
        btn_w.clicked.connect(lambda: self._toggle_key('W'))
        kb_layout.addWidget(btn_w, 1, 1)
        self.key_buttons[('left', 'W')] = btn_w

        btn_h = QPushButton("H")
        btn_h.setObjectName("leftKeyBtn")
        btn_h.setProperty("key_group", "left")
        btn_h.setCursor(Qt.PointingHandCursor)
        btn_h.setFixedSize(56, 56)
        btn_h.clicked.connect(lambda: self._toggle_key('H'))
        kb_layout.addWidget(btn_h, 1, 2)
        self.key_buttons[('left', 'H')] = btn_h

        btn_r = QPushButton("R")
        btn_r.setObjectName("leftKeyBtn")
        btn_r.setProperty("key_group", "left")
        btn_r.setCursor(Qt.PointingHandCursor)
        btn_r.setFixedSize(56, 56)
        btn_r.clicked.connect(lambda: self._toggle_key('R'))
        kb_layout.addWidget(btn_r, 1, 3)
        self.key_buttons[('left', 'R')] = btn_r

        # Row 3: Vowels (centered)
        vowel_row = ['A', 'O', 'E', 'U']
        for i, key in enumerate(vowel_row):
            btn = QPushButton(key)
            btn.setObjectName("vowelKeyBtn")
            btn.setProperty("key_group", "vowel")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedSize(80, 56)
            btn.clicked.connect(lambda checked, k=key: self._toggle_key(k))
            kb_layout.addWidget(btn, 2, i + 4)
            self.key_buttons[('vowel', key)] = btn

        # Star key
        btn_star = QPushButton("★")
        btn_star.setObjectName("keyBtn")
        btn_star.setProperty("key_group", "star")
        btn_star.setCursor(Qt.PointingHandCursor)
        btn_star.setFixedSize(56, 56)
        btn_star.clicked.connect(lambda: self._toggle_key('*'))
        kb_layout.addWidget(btn_star, 2, 8)
        self.key_buttons[('star', '*')] = btn_star

        layout.addLayout(kb_layout)

        # Controls
        ctrl_layout = QHBoxLayout()

        self.clear_btn = QPushButton("🗑️ Clear")
        self.clear_btn.clicked.connect(self.clear_keys)
        ctrl_layout.addWidget(self.clear_btn)

        ctrl_layout.addStretch()

        # Key info
        self.info_label = QLabel("Click keys to build a stroke")
        self.info_label.setStyleSheet("color: #78909c; font-style: italic; padding: 4px;")
        ctrl_layout.addWidget(self.info_label)

        layout.addLayout(ctrl_layout)

        # Legend
        legend_layout = QHBoxLayout()
        for label_text, color in [
            ("■ Left Hand", "#64b5f6"),
            ("■ Vowels", "#ffd54f"),
            ("■ Right Hand", "#81c784"),
            ("■ Star/Correction", "#e0e0e0")
        ]:
            lbl = QLabel(label_text)
            lbl.setStyleSheet(f"color: {color}; font-size: 12px; font-weight: bold; padding: 2px 8px;")
            legend_layout.addWidget(lbl)
        legend_layout.addStretch()
        layout.addLayout(legend_layout)

    def _toggle_key(self, key):
        if key in self.active_keys:
            self.active_keys.discard(key)
        else:
            self.active_keys.add(key)
        self._update_display()

    def _update_display(self):
        # Update button states
        for (group, key), btn in self.key_buttons.items():
            is_active = key in self.active_keys
            btn.setProperty("active", "true" if is_active else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)
            btn.repaint()

        # Build stroke string in steno order
        stroke = self._build_stroke_string()
        self.stroke_label.setText(stroke if stroke else "—")
        self.stroke_changed.emit(stroke)

        # Check if stroke matches a word
        if stroke:
            matches = [w for w, s in STENO_DICT.items() if s == stroke]
            if matches:
                self.info_label.setText(f"→ {', '.join(matches)}")
                self.info_label.setStyleSheet("color: #81c784; font-weight: bold; padding: 4px;")
            else:
                self.info_label.setText(f"Stroke: {stroke}")
                self.info_label.setStyleSheet("color: #ffd54f; font-style: italic; padding: 4px;")
        else:
            self.info_label.setText("Click keys to build a stroke")
            self.info_label.setStyleSheet("color: #78909c; font-style: italic; padding: 4px;")

    def _build_stroke_string(self):
        left_part = ""
        vowel_part = ""
        right_part = ""

        for key in LEFT_KEYS:
            if key in self.active_keys:
                left_part += key

        for key in VOWEL_KEYS:
            if key in self.active_keys:
                vowel_part += key

        for key in RIGHT_KEYS:
            if key in self.active_keys:
                right_part += key

        # Handle star
        star = "*" if "*" in self.active_keys else ""

        # Build stroke with proper dashes
        has_left = bool(left_part)
        has_vowel = bool(vowel_part)
        has_right = bool(right_part)
        has_star = bool(star)

        result = ""
        if has_left:
            result += left_part
        if has_vowel or has_star:
            if not has_left:
                pass  # no dash needed before vowels if no left
            result += vowel_part
            if has_star:
                result += star
        if has_right:
            if not has_left and not has_vowel:
                result += "-" + right_part
            else:
                result += right_part
        elif has_star and not has_vowel:
            if not has_left:
                result += "-" + star
            else:
                result += star

        return result

    def clear_keys(self):
        self.active_keys.clear()
        self._update_display()

    def set_keys_for_stroke(self, stroke):
        """Set the keyboard to display a specific stroke."""
        self.active_keys.clear()
        # Parse stroke into keys
        remaining = stroke.replace("-", "")

        for key in LEFT_KEYS:
            if remaining.startswith(key):
                self.active_keys.add(key)
                remaining = remaining[len(key):]

        for key in VOWEL_KEYS:
            if remaining.startswith(key):
                self.active_keys.add(key)
                remaining = remaining[len(key):]

        if remaining.startswith("*"):
            self.active_keys.add("*")
            remaining = remaining[1:]

        for key in RIGHT_KEYS:
            if remaining.startswith(key):
                self.active_keys.add(key)
                remaining = remaining[len(key):]

        self._update_display()


# ==================== HOME PAGE ====================

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 40, 40, 40)

        # Hero section
        hero = QFrame()
        hero.setStyleSheet(
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, "
            "stop:0 #1a1a2e, stop:0.5 #16213e, stop:1 #0f3460); "
            "border-radius: 20px; padding: 40px;"
        )
        hero_layout = QVBoxLayout(hero)

        title = QLabel("🎓 Stenography Learning App")
        title.setObjectName("titleLabel")
        title.setStyleSheet("font-size: 36px; font-weight: bold; color: #e94560;")
        hero_layout.addWidget(title)

        subtitle = QLabel(
            "Master machine shorthand with interactive lessons, practice, and quizzes"
        )
        subtitle.setObjectName("subtitleLabel")
        subtitle.setStyleSheet("font-size: 18px; color: #b0bec5; padding: 8px 0;")
        hero_layout.addWidget(subtitle)

        hero_layout.addSpacing(10)

        stats_text = QLabel(
            "💻 22 keys → 200+ WPM\n"
            "📚 7 structured lessons\n"
            "🔍 150+ word dictionary\n"
            "🎯 Practice & Quiz modes"
        )
        stats_text.setStyleSheet(
            "font-size: 16px; color: #78909c; line-height: 1.8; padding: 8px;"
        )
        hero_layout.addWidget(stats_text)

        layout.addWidget(hero)

        # Quick guide cards
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(16)

        cards_data = [
            ("⌨️", "Keyboard", "Interactive steno\nkeyboard visualizer", "#64b5f6"),
            ("📚", "Lessons", "Progressive lessons\nfrom basics to pro", "#81c784"),
            ("🎯", "Practice", "Type strokes for\nwords & get feedback", "#ffd54f"),
            ("❓", "Quiz", "Test your knowledge\nwith quizzes", "#e94560"),
        ]

        for icon, title, desc, color in cards_data:
            card = QFrame()
            card.setStyleSheet(
                f"background-color: #16213e; border-radius: 16px; "
                f"border: 2px solid {color}33; padding: 20px;"
            )
            card_layout = QVBoxLayout(card)

            icon_lbl = QLabel(icon)
            icon_lbl.setStyleSheet("font-size: 36px;")
            icon_lbl.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(icon_lbl)

            card_title = QLabel(title)
            card_title.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {color};")
            card_title.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(card_title)

            card_desc = QLabel(desc)
            card_desc.setStyleSheet("font-size: 12px; color: #78909c;")
            card_desc.setAlignment(Qt.AlignCenter)
            card_layout.addWidget(card_desc)

            cards_layout.addWidget(card)

        layout.addLayout(cards_layout)

        # Getting started
        start_frame = QFrame()
        start_frame.setStyleSheet(
            "background-color: #16213e; border-radius: 16px; padding: 24px;"
        )
        start_layout = QVBoxLayout(start_frame)

        start_title = QLabel("🚀 Getting Started")
        start_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #ffd54f;")
        start_layout.addWidget(start_title)

        steps = [
            "1️⃣  Start with <b>Lesson 1</b> to learn the basics of stenography",
            "2️⃣  Use the <b>Keyboard</b> tab to explore the steno keyboard interactively",
            "3️⃣  Move through lessons in order — each builds on the previous",
            "4️⃣  Use <b>Practice</b> mode to reinforce what you've learned",
            "5️⃣  Take <b>Quizzes</b> to test your knowledge",
            "6️⃣  Look up words in the <b>Dictionary</b> when you need a reference",
        ]
        for step in steps:
            step_lbl = QLabel(step)
            step_lbl.setStyleSheet("font-size: 14px; color: #b0bec5; padding: 4px 0;")
            start_layout.addWidget(step_lbl)

        layout.addWidget(start_frame)
        layout.addStretch()


# ==================== KEYBOARD PAGE ====================

class KeyboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(24, 24, 24, 24)

        # Title
        title = QLabel("🎹 Interactive Steno Keyboard")
        title.setObjectName("titleLabel")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #e94560;")
        layout.addWidget(title)

        desc = QLabel(
            "Click keys to build strokes. The stroke notation and matching words appear automatically."
        )
        desc.setStyleSheet("font-size: 14px; color: #b0bec5; padding-bottom: 8px;")
        layout.addWidget(desc)

        # Keyboard widget
        self.keyboard = StenoKeyboardWidget()
        layout.addWidget(self.keyboard)

        # Lookup section
        lookup_group = QGroupBox("🔍 Stroke Lookup")
        lookup_layout = QHBoxLayout(lookup_group)

        lookup_label = QLabel("Enter stroke:")
        lookup_label.setStyleSheet("color: #b0bec5; font-size: 14px;")
        lookup_layout.addWidget(lookup_label)

        self.lookup_input = QLineEdit()
        self.lookup_input.setPlaceholderText("e.g., TPHOT")
        self.lookup_input.textChanged.connect(self._on_lookup)
        lookup_layout.addWidget(self.lookup_input)

        self.lookup_result = QLabel("")
        self.lookup_result.setStyleSheet("color: #81c784; font-size: 16px; font-weight: bold;")
        lookup_layout.addWidget(self.lookup_result)

        layout.addWidget(lookup_group)

        # Steno order reference
        ref_group = QGroupBox("📖 Steno Order Reference")
        ref_layout = QVBoxLayout(ref_group)

        order_label = QLabel(
            "Keys are always read in this order: "
            "<b style='color:#64b5f6'>S T K P W H R</b> "
            "<b style='color:#ffd54f'>A O E U</b> "
            "<b style='color:#81c784'>F R P B L G T S D Z</b>"
        )
        order_label.setStyleSheet("font-size: 14px; padding: 8px;")
        order_label.setWordWrap(True)
        ref_layout.addWidget(order_label)

        tips = QLabel(
            "💡 <b>Tips:</b><br>"
            "• A dash before letters means right-hand only (e.g., <b>-T</b> = right T)<br>"
            "• The <b>★</b> key is used for corrections and disambiguation<br>"
            "• Some words are 'brief forms' — shortened strokes for speed<br>"
            "• Press multiple keys at once (chording) to type whole syllables/words"
        )
        tips.setStyleSheet("font-size: 13px; color: #90a4ae; padding: 8px;")
        tips.setWordWrap(True)
        ref_layout.addWidget(tips)

        layout.addWidget(ref_group)
        layout.addStretch()

    def _on_lookup(self, text):
        stroke = text.strip().upper()
        if not stroke:
            self.lookup_result.setText("")
            return

        matches = [w for w, s in STENO_DICT.items() if s == stroke]
        if matches:
            self.lookup_result.setText(f"→ {', '.join(matches)}")
            self.lookup_result.setStyleSheet("color: #81c784; font-size: 16px; font-weight: bold;")
        else:
            self.lookup_result.setText("No match found")
            self.lookup_result.setStyleSheet("color: #e94560; font-size: 14px;")


# ==================== LESSON PAGE ====================

class LessonPage(QWidget):
    lesson_completed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_lesson = 0
        self._build_ui()

    def _build_ui(self):
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Left panel: lesson list
        left_panel = QWidget()
        left_panel.setFixedWidth(280)
        left_panel.setStyleSheet("background-color: #0e1a30; border-right: 1px solid #1a2744;")
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(12, 16, 12, 16)

        list_title = QLabel("📚 Lessons")
        list_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #e94560; padding: 8px;")
        left_layout.addWidget(list_title)

        self.lesson_list = QListWidget()
        self.lesson_list.currentRowChanged.connect(self._on_lesson_selected)
        for i, lesson in enumerate(LESSONS):
            self.lesson_list.addItem(lesson['title'])
        left_layout.addWidget(self.lesson_list)

        # Progress
        self.progress_label = QLabel("Progress: 0 / {}".format(len(LESSONS)))
        self.progress_label.setStyleSheet("color: #78909c; font-size: 12px; padding: 8px;")
        left_layout.addWidget(self.progress_label)

        self.main_layout.addWidget(left_panel)

        # Right panel: lesson content
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(16)
        right_layout.setContentsMargins(32, 24, 32, 24)

        # Content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        self.content_layout.setSpacing(16)

        self.content_display = QTextEdit()
        self.content_display.setReadOnly(True)
        self.content_display.setStyleSheet(
            "background-color: #16213e; color: #e0e0e0; border: none; "
            "font-size: 14px; line-height: 1.6; padding: 8px;"
        )
        self.content_layout.addWidget(self.content_display)

        # Exercise section
        self.exercise_group = QGroupBox("✏️ Lesson Exercises")
        self.exercise_layout = QVBoxLayout(self.exercise_group)

        self.exercise_word = QLabel("")
        self.exercise_word.setObjectName("wordLabel")
        self.exercise_word.setStyleSheet("font-size: 36px; font-weight: bold; color: #64b5f6;")
        self.exercise_word.setAlignment(Qt.AlignCenter)
        self.exercise_layout.addWidget(self.exercise_word)

        self.exercise_hint = QLabel("")
        self.exercise_hint.setStyleSheet("color: #ffd54f; font-size: 14px; font-style: italic;")
        self.exercise_hint.setAlignment(Qt.AlignCenter)
        self.exercise_layout.addWidget(self.exercise_hint)

        input_row = QHBoxLayout()
        self.exercise_input = QLineEdit()
        self.exercise_input.setPlaceholderText("Type the steno stroke...")
        self.exercise_input.returnPressed.connect(self._check_exercise)
        input_row.addWidget(self.exercise_input)

        check_btn = QPushButton("Check ✓")
        check_btn.setObjectName("accentBtn")
        check_btn.clicked.connect(self._check_exercise)
        input_row.addWidget(check_btn)
        self.exercise_layout.addLayout(input_row)

        self.exercise_feedback = QLabel("")
        self.exercise_feedback.setAlignment(Qt.AlignCenter)
        self.exercise_layout.addWidget(self.exercise_feedback)

        self.exercise_progress = QProgressBar()
        self.exercise_progress.setRange(0, 100)
        self.exercise_layout.addWidget(self.exercise_progress)

        self.exercise_nav = QHBoxLayout()
        self.prev_ex_btn = QPushButton("← Previous")
        self.prev_ex_btn.clicked.connect(self._prev_exercise)
        self.exercise_nav.addWidget(self.prev_ex_btn)

        self.exercise_counter = QLabel("")
        self.exercise_counter.setStyleSheet("color: #78909c; font-size: 12px;")
        self.exercise_counter.setAlignment(Qt.AlignCenter)
        self.exercise_nav.addWidget(self.exercise_counter)

        self.next_ex_btn = QPushButton("Next →")
        self.next_ex_btn.clicked.connect(self._next_exercise)
        self.exercise_nav.addWidget(self.next_ex_btn)

        self.exercise_layout.addLayout(self.exercise_nav)
        self.content_layout.addWidget(self.exercise_group)

        # Navigation
        nav_layout = QHBoxLayout()
        self.prev_btn = QPushButton("← Previous Lesson")
        self.prev_btn.clicked.connect(self._prev_lesson)
        nav_layout.addWidget(self.prev_btn)

        nav_layout.addStretch()

        self.complete_btn = QPushButton("✓ Mark Complete")
        self.complete_btn.setObjectName("accentBtn")
        self.complete_btn.clicked.connect(self._mark_complete)
        nav_layout.addWidget(self.complete_btn)

        nav_layout.addStretch()

        self.next_btn = QPushButton("Next Lesson →")
        self.next_btn.clicked.connect(self._next_lesson)
        nav_layout.addWidget(self.next_btn)

        self.content_layout.addLayout(nav_layout)
        self.content_layout.addStretch()

        scroll.setWidget(content_widget)
        right_layout.addWidget(scroll)

        self.main_layout.addWidget(right_panel)

        # State
        self.current_exercise = 0
        self.completed_lessons = set()
        self.exercise_correct = 0

        # Load first lesson
        if LESSONS:
            self.lesson_list.setCurrentRow(0)
            self._load_lesson(0)

    def _on_lesson_selected(self, row):
        if row >= 0:
            self._load_lesson(row)

    def _load_lesson(self, index):
        self.current_lesson = index
        lesson = LESSONS[index]

        self.content_display.setHtml(lesson['content'])

        # Setup exercises
        exercises = lesson.get('exercises', [])
        if exercises:
            self.exercise_group.setVisible(True)
            self.current_exercise = 0
            self.exercise_correct = 0
            self._load_exercise()
        else:
            self.exercise_group.setVisible(False)

        # Update nav buttons
        self.prev_btn.setEnabled(index > 0)
        self.next_btn.setEnabled(index < len(LESSONS) - 1)

        # Update complete button
        if index in self.completed_lessons:
            self.complete_btn.setText("✓ Completed")
            self.complete_btn.setEnabled(False)
        else:
            self.complete_btn.setText("✓ Mark Complete")
            self.complete_btn.setEnabled(True)

    def _load_exercise(self):
        lesson = LESSONS[self.current_lesson]
        exercises = lesson.get('exercises', [])
        if not exercises:
            return

        ex = exercises[self.current_exercise]
        self.exercise_word.setText(f'"{ex["word"]}"')
        self.exercise_hint.setText(f'Hint: {ex["hint"]}')
        self.exercise_input.clear()
        self.exercise_feedback.setText("")
        self.exercise_input.setFocus()

        self.exercise_counter.setText(
            f"Exercise {self.current_exercise + 1} / {len(exercises)}"
        )
        total = len(exercises)
        if total > 0:
            self.exercise_progress.setValue(int((self.current_exercise / total) * 100))

        self.prev_ex_btn.setEnabled(self.current_exercise > 0)
        self.next_ex_btn.setEnabled(self.current_exercise < total - 1)

    def _check_exercise(self):
        lesson = LESSONS[self.current_lesson]
        exercises = lesson.get('exercises', [])
        if not exercises:
            return

        ex = exercises[self.current_exercise]
        user_input = self.exercise_input.text().strip().upper()
        correct = ex['stroke'].upper()

        if user_input == correct:
            self.exercise_feedback.setText("✅ Correct! Great job!")
            self.exercise_feedback.setObjectName("correctLabel")
            self.exercise_feedback.setStyleSheet("color: #81c784; font-size: 18px; font-weight: bold;")
            self.exercise_correct += 1
            # Auto advance after delay
            QTimer.singleShot(1200, self._next_exercise)
        else:
            self.exercise_feedback.setText(
                f"❌ Not quite. The correct stroke is: <b style='color:#ffd54f'>{correct}</b>"
            )
            self.exercise_feedback.setObjectName("wrongLabel")
            self.exercise_feedback.setStyleSheet("color: #e94560; font-size: 16px;")

    def _prev_exercise(self):
        if self.current_exercise > 0:
            self.current_exercise -= 1
            self._load_exercise()

    def _next_exercise(self):
        lesson = LESSONS[self.current_lesson]
        exercises = lesson.get('exercises', [])
        if self.current_exercise < len(exercises) - 1:
            self.current_exercise += 1
            self._load_exercise()
        else:
            total = len(exercises)
            self.exercise_progress.setValue(100)
            self.exercise_feedback.setText(
                f"🎉 Exercise complete! {self.exercise_correct}/{total} correct."
            )
            self.exercise_feedback.setStyleSheet("color: #ffd54f; font-size: 18px; font-weight: bold;")

    def _prev_lesson(self):
        if self.current_lesson > 0:
            self.lesson_list.setCurrentRow(self.current_lesson - 1)

    def _next_lesson(self):
        if self.current_lesson < len(LESSONS) - 1:
            self.lesson_list.setCurrentRow(self.current_lesson + 1)

    def _mark_complete(self):
        self.completed_lessons.add(self.current_lesson)
        self.complete_btn.setText("✓ Completed")
        self.complete_btn.setEnabled(False)
        self.progress_label.setText(
            f"Progress: {len(self.completed_lessons)} / {len(LESSONS)}"
        )
        self.lesson_completed.emit(self.current_lesson)


# ==================== PRACTICE PAGE ====================

class PracticePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_word = None
        self.current_stroke = None
        self.score = 0
        self.total = 0
        self.streak = 0
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 32, 40, 32)

        # Title row
        title_row = QHBoxLayout()
        title = QLabel("🎯 Practice Mode")
        title.setObjectName("titleLabel")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #e94560;")
        title_row.addWidget(title)
        title_row.addStretch()

        self.score_label = QLabel("Score: 0 / 0")
        self.score_label.setStyleSheet("font-size: 16px; color: #78909c; font-weight: bold;")
        title_row.addWidget(self.score_label)

        self.streak_label = QLabel("🔥 Streak: 0")
        self.streak_label.setStyleSheet("font-size: 16px; color: #ff9800; font-weight: bold;")
        title_row.addWidget(self.streak_label)

        layout.addLayout(title_row)

        # Difficulty selection
        diff_row = QHBoxLayout()
        diff_label = QLabel("Difficulty:")
        diff_label.setStyleSheet("color: #b0bec5; font-size: 14px; font-weight: bold;")
        diff_row.addWidget(diff_label)

        self.diff_buttons = QButtonGroup(self)
        for i, (text, count) in enumerate([
            ("🟢 Easy (brief forms)", 15),
            ("🟡 Medium (common)", 30),
            ("🔴 Hard (all words)", None),
        ]):
            btn = QRadioButton(text)
            btn.setStyleSheet("color: #e0e0e0; font-size: 13px; padding: 4px 12px;")
            if i == 0:
                btn.setChecked(True)
            self.diff_buttons.addButton(btn, i)
            diff_row.addWidget(btn)

        diff_row.addStretch()
        layout.addLayout(diff_row)

        # Main practice area
        practice_frame = QFrame()
        practice_frame.setStyleSheet(
            "background-color: #16213e; border-radius: 20px; padding: 32px;"
        )
        practice_layout = QVBoxLayout(practice_frame)
        practice_layout.setSpacing(16)

        # Word display
        word_container = QVBoxLayout()
        prompt = QLabel("Type the steno stroke for:")
        prompt.setStyleSheet("color: #78909c; font-size: 14px;")
        prompt.setAlignment(Qt.AlignCenter)
        word_container.addWidget(prompt)

        self.word_label = QLabel("")
        self.word_label.setObjectName("wordLabel")
        self.word_label.setStyleSheet("font-size: 48px; font-weight: bold; color: #64b5f6;")
        self.word_label.setAlignment(Qt.AlignCenter)
        word_container.addWidget(self.word_label)

        practice_layout.addLayout(word_container)

        # Input
        input_row = QHBoxLayout()
        self.stroke_input = QLineEdit()
        self.stroke_input.setPlaceholderText("Type steno stroke here (e.g., TPHOT)...")
        self.stroke_input.setStyleSheet(
            "font-size: 20px; font-weight: bold; padding: 16px; letter-spacing: 2px;"
        )
        self.stroke_input.returnPressed.connect(self._check_answer)
        input_row.addWidget(self.stroke_input)

        check_btn = QPushButton("Check ✓")
        check_btn.setObjectName("accentBtn")
        check_btn.setFixedSize(120, 48)
        check_btn.clicked.connect(self._check_answer)
        input_row.addWidget(check_btn)

        practice_layout.addLayout(input_row)

        # Feedback
        self.feedback_label = QLabel("")
        self.feedback_label.setAlignment(Qt.AlignCenter)
        self.feedback_label.setStyleSheet("font-size: 18px; font-weight: bold; min-height: 30px;")
        practice_layout.addWidget(self.feedback_label)

        # Show answer button
        self.show_btn = QPushButton("👁️ Show Answer")
        self.show_btn.clicked.connect(self._show_answer)
        practice_layout.addWidget(self.show_btn, alignment=Qt.AlignCenter)

        layout.addWidget(practice_frame)

        # Keyboard reference
        self.keyboard = StenoKeyboardWidget()
        layout.addWidget(self.keyboard)

        # Start button
        start_row = QHBoxLayout()
        start_row.addStretch()

        self.start_btn = QPushButton("🎲 New Practice Session")
        self.start_btn.setObjectName("accentBtn")
        self.start_btn.setStyleSheet("font-size: 16px; padding: 14px 32px;")
        self.start_btn.clicked.connect(self._new_session)
        start_row.addWidget(self.start_btn)

        start_row.addStretch()
        layout.addLayout(start_row)

        # Auto-start
        QTimer.singleShot(500, self._new_session)

    def _get_word_list(self):
        idx = self.diff_buttons.checkedId()
        if idx == 0:
            brief_forms = {'the', 'and', 'is', 'are', 'have', 'with', 'can',
                          'will', 'of', 'it', 'in', 'to', 'had', 'do', 'be',
                          'he', 'we', 'go', 'not', 'but', 'for', 'on', 'at',
                          'so', 'if', 'up', 'out', 'off', 'or', 'her'}
            return {w: s for w, s in STENO_DICT.items() if w in brief_forms}
        elif idx == 1:
            words = list(STENO_DICT.keys())[:70]
            return {w: STENO_DICT[w] for w in words}
        else:
            return dict(STENO_DICT)

    def _new_session(self):
        self.score = 0
        self.total = 0
        self.streak = 0
        self._update_score()
        self._next_word()

    def _next_word(self):
        word_list = self._get_word_list()
        if not word_list:
            return
        self.current_word = random.choice(list(word_list.keys()))
        self.current_stroke = word_list[self.current_word]
        self.word_label.setText(f'"{self.current_word}"')
        self.stroke_input.clear()
        self.feedback_label.setText("")
        self.show_btn.setVisible(True)
        self.stroke_input.setFocus()
        self.keyboard.clear_keys()

    def _check_answer(self):
        if not self.current_stroke:
            return

        user_input = self.stroke_input.text().strip().upper()
        correct = self.current_stroke.upper()

        self.total += 1

        if user_input == correct:
            self.score += 1
            self.streak += 1
            self.feedback_label.setText("✅ Correct! Well done!")
            self.feedback_label.setStyleSheet("color: #81c784; font-size: 20px; font-weight: bold;")
            self.keyboard.set_keys_for_stroke(correct)
            QTimer.singleShot(1000, self._next_word)
        else:
            self.streak = 0
            self.feedback_label.setText(
                f"❌ Incorrect. The answer is: <b style='color:#ffd54f'>{self.current_stroke}</b>"
            )
            self.feedback_label.setStyleSheet("color: #e94560; font-size: 18px; font-weight: bold;")
            self.keyboard.set_keys_for_stroke(correct)

        self._update_score()

    def _show_answer(self):
        if self.current_stroke:
            self.feedback_label.setText(
                f"The stroke for <b>'{self.current_word}'</b> is: "
                f"<b style='color:#ffd54f'>{self.current_stroke}</b>"
            )
            self.feedback_label.setStyleSheet("color: #ffd54f; font-size: 18px; font-weight: bold;")
            self.keyboard.set_keys_for_stroke(self.current_stroke)
            self.show_btn.setVisible(False)

    def _update_score(self):
        self.score_label.setText(f"Score: {self.score} / {self.total}")
        pct = (self.score / self.total * 100) if self.total > 0 else 0
        self.streak_label.setText(f"🔥 Streak: {self.streak}  ({pct:.0f}%)")


# ==================== QUIZ PAGE ====================

class QuizPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.quiz_data = []
        self.current_q = 0
        self.quiz_score = 0
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(40, 32, 40, 32)

        # Title
        title_row = QHBoxLayout()
        title = QLabel("❓ Quiz Mode")
        title.setObjectName("titleLabel")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #e94560;")
        title_row.addWidget(title)
        title_row.addStretch()

        self.quiz_score_label = QLabel("")
        self.quiz_score_label.setStyleSheet("font-size: 16px; color: #78909c; font-weight: bold;")
        title_row.addWidget(self.quiz_score_label)

        layout.addLayout(title_row)

        # Quiz type selection
        type_row = QHBoxLayout()
        type_label = QLabel("Quiz Type:")
        type_label.setStyleSheet("color: #b0bec5; font-size: 14px; font-weight: bold;")
        type_row.addWidget(type_label)

        self.type_buttons = QButtonGroup(self)
        for i, text in enumerate([
            "🔤 Word → Stroke",
            "🎹 Stroke → Word",
            "🔀 Mixed",
        ]):
            btn = QRadioButton(text)
            btn.setStyleSheet("color: #e0e0e0; font-size: 13px; padding: 4px 12px;")
            if i == 0:
                btn.setChecked(True)
            self.type_buttons.addButton(btn, i)
            type_row.addWidget(btn)

        type_row.addStretch()

        # Question count
        count_label = QLabel("Questions:")
        count_label.setStyleSheet("color: #b0bec5; font-size: 14px; font-weight: bold;")
        type_row.addWidget(count_label)

        self.count_buttons = QButtonGroup(self)
        for i, text in enumerate(["5", "10", "20"]):
            btn = QRadioButton(text)
            btn.setStyleSheet("color: #e0e0e0; font-size: 13px; padding: 4px 12px;")
            if i == 1:
                btn.setChecked(True)
            self.count_buttons.addButton(btn, i)
            type_row.addWidget(btn)

        type_row.addStretch()

        self.start_quiz_btn = QPushButton("🚀 Start Quiz")
        self.start_quiz_btn.setObjectName("accentBtn")
        self.start_quiz_btn.clicked.connect(self._start_quiz)
        type_row.addWidget(self.start_quiz_btn)

        layout.addLayout(type_row)

        # Quiz area (stacked: question / results)
        self.quiz_stack = QStackedWidget()

        # -- Question page
        q_page = QWidget()
        q_layout = QVBoxLayout(q_page)
        q_layout.setSpacing(20)

        self.quiz_progress = QProgressBar()
        self.quiz_progress.setRange(0, 100)
        q_layout.addWidget(self.quiz_progress)

        self.quiz_question_label = QLabel("")
        self.quiz_question_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: #e0e0e0; padding: 16px;"
        )
        self.quiz_question_label.setAlignment(Qt.AlignCenter)
        self.quiz_question_label.setWordWrap(True)
        q_layout.addWidget(self.quiz_question_label)

        # Answer options
        self.option_buttons = []
        self.option_group = QButtonGroup(self)
        for i in range(4):
            btn = QPushButton("")
            btn.setStyleSheet(
                "QPushButton { background-color: #1a2744; color: #e0e0e0; "
                "border: 2px solid #2a3a5e; border-radius: 12px; "
                "padding: 16px; font-size: 16px; font-weight: bold; text-align: left; }"
                "QPushButton:hover { background-color: #1a3a5e; border-color: #64b5f6; }"
            )
            btn.setCursor(Qt.PointingHandCursor)
            btn.setVisible(False)
            self.option_group.addButton(btn, i)
            self.option_buttons.append(btn)
            q_layout.addWidget(btn)

        self.option_group.buttonClicked.connect(self._on_option_selected)

        # Free-form input (for word→stroke mode)
        self.quiz_input_frame = QFrame()
        quiz_input_layout = QHBoxLayout(self.quiz_input_frame)
        self.quiz_input = QLineEdit()
        self.quiz_input.setPlaceholderText("Type the steno stroke...")
        self.quiz_input.setStyleSheet(
            "font-size: 18px; font-weight: bold; padding: 14px; letter-spacing: 2px;"
        )
        self.quiz_input.returnPressed.connect(self._on_input_submitted)
        quiz_input_layout.addWidget(self.quiz_input)

        submit_btn = QPushButton("Submit ✓")
        submit_btn.setObjectName("accentBtn")
        submit_btn.clicked.connect(self._on_input_submitted)
        quiz_input_layout.addWidget(submit_btn)

        self.quiz_input_frame.setVisible(False)
        q_layout.addWidget(self.quiz_input_frame)

        self.quiz_feedback = QLabel("")
        self.quiz_feedback.setAlignment(Qt.AlignCenter)
        self.quiz_feedback.setStyleSheet("font-size: 18px; font-weight: bold; min-height: 30px;")
        q_layout.addWidget(self.quiz_feedback)

        self.quiz_nav_row = QHBoxLayout()
        self.quiz_next_btn = QPushButton("Next Question →")
        self.quiz_next_btn.setObjectName("accentBtn")
        self.quiz_next_btn.clicked.connect(self._next_question)
        self.quiz_nav_row.addStretch()
        self.quiz_nav_row.addWidget(self.quiz_next_btn)
        self.quiz_nav_row.addStretch()
        q_layout.addLayout(self.quiz_nav_row)

        self.quiz_stack.addWidget(q_page)

        # -- Results page
        r_page = QWidget()
        r_layout = QVBoxLayout(r_page)
        r_layout.setSpacing(20)
        r_layout.setAlignment(Qt.AlignCenter)

        results_frame = QFrame()
        results_frame.setStyleSheet(
            "background-color: #16213e; border-radius: 20px; padding: 40px;"
        )
        results_inner = QVBoxLayout(results_frame)
        results_inner.setSpacing(16)
        results_inner.setAlignment(Qt.AlignCenter)

        trophy = QLabel("🏆")
        trophy.setStyleSheet("font-size: 64px;")
        trophy.setAlignment(Qt.AlignCenter)
        results_inner.addWidget(trophy)

        self.results_title = QLabel("Quiz Complete!")
        self.results_title.setStyleSheet("font-size: 32px; font-weight: bold; color: #ffd54f;")
        self.results_title.setAlignment(Qt.AlignCenter)
        results_inner.addWidget(self.results_title)

        self.results_score = QLabel("")
        self.results_score.setStyleSheet("font-size: 24px; font-weight: bold; color: #64b5f6;")
        self.results_score.setAlignment(Qt.AlignCenter)
        results_inner.addWidget(self.results_score)

        self.results_grade = QLabel("")
        self.results_grade.setStyleSheet("font-size: 48px; font-weight: bold;")
        self.results_grade.setAlignment(Qt.AlignCenter)
        results_inner.addWidget(self.results_grade)

        self.results_detail = QLabel("")
        self.results_detail.setStyleSheet("font-size: 14px; color: #90a4ae;")
        self.results_detail.setAlignment(Qt.AlignCenter)
        self.results_detail.setWordWrap(True)
        results_inner.addWidget(self.results_detail)

        retry_btn = QPushButton("🔄 Try Another Quiz")
        retry_btn.setObjectName("accentBtn")
        retry_btn.setStyleSheet("font-size: 16px; padding: 14px 32px;")
        retry_btn.clicked.connect(self._retry_quiz)
        results_inner.addWidget(retry_btn, alignment=Qt.AlignCenter)

        r_layout.addWidget(results_frame)
        self.quiz_stack.addWidget(r_page)

        layout.addWidget(self.quiz_stack)

        # Show start state
        self._show_start_state()

    def _show_start_state(self):
        self.quiz_question_label.setText(
            "Select your quiz options above and click <b>Start Quiz</b>!"
        )
        self.quiz_progress.setValue(0)
        self.quiz_feedback.setText("")
        for btn in self.option_buttons:
            btn.setVisible(False)
        self.quiz_input_frame.setVisible(False)
        self.quiz_next_btn.setVisible(False)
        self.quiz_score_label.setText("")

    def _start_quiz(self):
        quiz_type = self.type_buttons.checkedId()
        count_map = {0: 5, 1: 10, 2: 20}
        count = count_map[self.count_buttons.checkedId()]

        # Build quiz data
        words = list(STENO_DICT.keys())
        sample = random.sample(words, min(count, len(words)))

        self.quiz_data = []
        for word in sample:
            stroke = STENO_DICT[word]
            if quiz_type == 0:  # Word → Stroke (free input)
                q_type = 'input'
            elif quiz_type == 1:  # Stroke → Word (multiple choice)
                q_type = 'choice'
            else:  # Mixed
                q_type = random.choice(['input', 'choice'])

            if q_type == 'choice':
                # Build choices
                wrong_words = [w for w in words if w != word]
                choices = random.sample(wrong_words, min(3, len(wrong_words)))
                choices.append(word)
                random.shuffle(choices)
                self.quiz_data.append({
                    'type': 'choice',
                    'question': f"What word does the stroke <b style='color:#ffd54f'>{stroke}</b> represent?",
                    'answer': word,
                    'choices': choices,
                })
            else:
                self.quiz_data.append({
                    'type': 'input',
                    'question': f"What is the steno stroke for <b style='color:#64b5f6'>{word}</b>?",
                    'answer': stroke,
                    'word': word,
                })

        self.current_q = 0
        self.quiz_score = 0
        self.quiz_stack.setCurrentIndex(0)
        self._show_question()

    def _show_question(self):
        if self.current_q >= len(self.quiz_data):
            self._show_results()
            return

        q = self.quiz_data[self.current_q]
        self.quiz_progress.setValue(
            int((self.current_q / len(self.quiz_data)) * 100)
        )
        self.quiz_question_label.setText(q['question'])
        self.quiz_feedback.setText("")
        self.quiz_next_btn.setVisible(False)
        self.quiz_score_label.setText(
            f"Question {self.current_q + 1}/{len(self.quiz_data)}  |  "
            f"Score: {self.quiz_score}"
        )

        if q['type'] == 'choice':
            self.quiz_input_frame.setVisible(False)
            for i, btn in enumerate(self.option_buttons):
                btn.setText(f"  {q['choices'][i]}")
                btn.setVisible(True)
                btn.setEnabled(True)
                btn.setStyleSheet(
                    "QPushButton { background-color: #1a2744; color: #e0e0e0; "
                    "border: 2px solid #2a3a5e; border-radius: 12px; "
                    "padding: 16px; font-size: 16px; font-weight: bold; text-align: left; }"
                    "QPushButton:hover { background-color: #1a3a5e; border-color: #64b5f6; }"
                )
        else:
            for btn in self.option_buttons:
                btn.setVisible(False)
            self.quiz_input_frame.setVisible(True)
            self.quiz_input.clear()
            self.quiz_input.setFocus()

    def _on_option_selected(self, btn):
        q = self.quiz_data[self.current_q]
        selected = btn.text().strip()
        correct = q['answer']

        # Disable all buttons
        for b in self.option_buttons:
            b.setEnabled(False)
            if b.text().strip() == correct:
                b.setStyleSheet(
                    "QPushButton { background-color: #1b5e20; color: #81c784; "
                    "border: 2px solid #4caf50; border-radius: 12px; "
                    "padding: 16px; font-size: 16px; font-weight: bold; text-align: left; }"
                )

        if selected == correct:
            self.quiz_score += 1
            btn.setStyleSheet(
                "QPushButton { background-color: #1b5e20; color: #ffffff; "
                "border: 2px solid #4caf50; border-radius: 12px; "
                "padding: 16px; font-size: 16px; font-weight: bold; text-align: left; }"
            )
            self.quiz_feedback.setText("✅ Correct!")
            self.quiz_feedback.setStyleSheet("color: #81c784; font-size: 20px; font-weight: bold;")
        else:
            btn.setStyleSheet(
                "QPushButton { background-color: #b71c1c; color: #ffffff; "
                "border: 2px solid #e53935; border-radius: 12px; "
                "padding: 16px; font-size: 16px; font-weight: bold; text-align: left; }"
            )
            self.quiz_feedback.setText(f"❌ Wrong! The answer was: <b>{correct}</b>")
            self.quiz_feedback.setStyleSheet("color: #e94560; font-size: 18px; font-weight: bold;")

        self.quiz_next_btn.setVisible(True)

    def _on_input_submitted(self):
        q = self.quiz_data[self.current_q]
        user_input = self.quiz_input.text().strip().upper()
        correct = q['answer'].upper()

        if user_input == correct:
            self.quiz_score += 1
            self.quiz_feedback.setText("✅ Correct!")
            self.quiz_feedback.setStyleSheet("color: #81c784; font-size: 20px; font-weight: bold;")
        else:
            self.quiz_feedback.setText(
                f"❌ Wrong! The stroke for <b>{q['word']}</b> is: "
                f"<b style='color:#ffd54f'>{q['answer']}</b>"
            )
            self.quiz_feedback.setStyleSheet("color: #e94560; font-size: 18px; font-weight: bold;")

        self.quiz_input.setEnabled(False)
        self.quiz_next_btn.setVisible(True)

    def _next_question(self):
        self.current_q += 1
        self.quiz_input.setEnabled(True)
        self._show_question()

    def _show_results(self):
        total = len(self.quiz_data)
        pct = (self.quiz_score / total * 100) if total > 0 else 0

        self.results_score.setText(f"{self.quiz_score} / {total} ({pct:.0f}%)")

        if pct >= 90:
            grade = "A+"
            color = "#4caf50"
            msg = "Outstanding! You're a steno master! 🌟"
        elif pct >= 80:
            grade = "A"
            color = "#81c784"
            msg = "Excellent work! Almost perfect! 🎉"
        elif pct >= 70:
            grade = "B"
            color = "#64b5f6"
            msg = "Good job! Keep practicing! 💪"
        elif pct >= 60:
            grade = "C"
            color = "#ffd54f"
            msg = "Not bad! Review the lessons and try again. 📖"
        elif pct >= 50:
            grade = "D"
            color = "#ff9800"
            msg = "Needs improvement. Go through the lessons again. 🔁"
        else:
            grade = "F"
            color = "#e94560"
            msg = "Keep studying! Review the basics and try again. 📚"

        self.results_grade.setText(grade)
        self.results_grade.setStyleSheet(f"font-size: 72px; font-weight: bold; color: {color};")
        self.results_detail.setText(msg)

        self.quiz_stack.setCurrentIndex(1)

    def _retry_quiz(self):
        self.quiz_stack.setCurrentIndex(0)
        self._show_start_state()


# ==================== DICTIONARY PAGE ====================

class DictionaryPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(40, 32, 40, 32)

        # Title
        title = QLabel("📖 Steno Dictionary")
        title.setObjectName("titleLabel")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #e94560;")
        layout.addWidget(title)

        desc = QLabel(f"Browse {len(STENO_DICT)} words and their steno strokes")
        desc.setStyleSheet("font-size: 14px; color: #b0bec5; padding-bottom: 8px;")
        layout.addWidget(desc)

        # Search
        search_row = QHBoxLayout()

        search_label = QLabel("🔍 Search:")
        search_label.setStyleSheet("color: #b0bec5; font-size: 14px; font-weight: bold;")
        search_row.addWidget(search_label)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Type a word or stroke to search...")
        self.search_input.textChanged.connect(self._filter_dict)
        search_row.addWidget(self.search_input)

        self.clear_search_btn = QPushButton("✕ Clear")
        self.clear_search_btn.clicked.connect(lambda: self.search_input.clear())
        search_row.addWidget(self.clear_search_btn)

        layout.addLayout(search_row)

        # Filter buttons
        filter_row = QHBoxLayout()
        filter_label = QLabel("Filter:")
        filter_label.setStyleSheet("color: #b0bec5; font-size: 13px; font-weight: bold;")
        filter_row.addWidget(filter_label)

        self.filter_btns = QButtonGroup(self)
        for i, text in enumerate(["All", "Brief Forms", "Common", "Advanced"]):
            btn = QRadioButton(text)
            btn.setStyleSheet("color: #e0e0e0; font-size: 12px; padding: 2px 8px;")
            if i == 0:
                btn.setChecked(True)
            self.filter_btns.addButton(btn, i)
            filter_row.addWidget(btn)

        self.filter_btns.buttonClicked.connect(self._filter_dict)
        filter_row.addStretch()

        self.count_label = QLabel(f"Showing {len(STENO_DICT)} entries")
        self.count_label.setStyleSheet("color: #78909c; font-size: 12px;")
        filter_row.addWidget(self.count_label)

        layout.addLayout(filter_row)

        # Dictionary table
        self.dict_table = QListWidget()
        self.dict_table.setStyleSheet(
            "QListWidget { background-color: #16213e; border: 1px solid #2a3a5e; "
            "border-radius: 8px; padding: 8px; }"
            "QListWidget::item { padding: 10px 16px; border-bottom: 1px solid #1a2744; }"
            "QListWidget::item:hover { background-color: #1a2744; }"
        )
        self.dict_table.setAlternatingRowColors(True)
        layout.addWidget(self.dict_table)

        self._populate_dict()

    def _get_filtered_words(self):
        filter_id = self.filter_btns.checkedId()
        brief_forms = {
            'the', 'and', 'is', 'are', 'have', 'with', 'can', 'will', 'of',
            'it', 'in', 'to', 'had', 'do', 'be', 'he', 'we', 'go', 'not',
            'but', 'for', 'on', 'at', 'so', 'if', 'up', 'out', 'off', 'or',
            'her', 'was', 'were', 'his', 'this', 'that'
        }
        common = set(list(STENO_DICT.keys())[:80])

        if filter_id == 0:
            return list(STENO_DICT.keys())
        elif filter_id == 1:
            return [w for w in STENO_DICT if w in brief_forms]
        elif filter_id == 2:
            return [w for w in STENO_DICT if w in common]
        else:
            return [w for w in STENO_DICT if w not in common and w not in brief_forms]

    def _populate_dict(self, words=None):
        self.dict_table.clear()
        if words is None:
            words = list(STENO_DICT.keys())

        for word in sorted(words):
            stroke = STENO_DICT[word]
            item_text = f"  {word:<15}  →  {stroke}"
            self.dict_table.addItem(item_text)

        self.count_label.setText(f"Showing {len(words)} entries")

    def _filter_dict(self):
        search = self.search_input.text().strip().lower()
        words = self._get_filtered_words()

        if search:
            words = [
                w for w in words
                if search in w.lower() or search in STENO_DICT[w].lower()
            ]

        self._populate_dict(words)


# ==================== MAIN WINDOW ====================

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎓 Stenography Learning App")
        self.setMinimumSize(QSize(1100, 750))
        self.resize(1280, 850)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # ---- Sidebar ----
        sidebar = QWidget()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet(
            "background-color: #0a0f1e; border-right: 1px solid #1a2744;"
        )
        side_layout = QVBoxLayout(sidebar)
        side_layout.setSpacing(4)
        side_layout.setContentsMargins(8, 16, 8, 16)

        # Logo
        logo_label = QLabel("⌨️ StenoApp")
        logo_label.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: #e94560; "
            "padding: 12px 8px 4px 8px;"
        )
        side_layout.addWidget(logo_label)

        version_label = QLabel("v1.0 — Learn Stenography")
        version_label.setStyleSheet("font-size: 11px; color: #546e7a; padding: 0 8px 16px 8px;")
        side_layout.addWidget(version_label)

        # Nav buttons
        self.nav_buttons = []
        nav_items = [
            ("🏠", "Home", 0),
            ("📚", "Lessons", 1),
            ("⌨️", "Keyboard", 2),
            ("🎯", "Practice", 3),
            ("❓", "Quiz", 4),
            ("📖", "Dictionary", 5),
        ]

        for icon, text, page_idx in nav_items:
            btn = QPushButton(f"  {icon}  {text}")
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setProperty("page_idx", page_idx)
            btn.setStyleSheet(
                "QPushButton { "
                "  background-color: transparent; color: #90a4ae; "
                "  border: none; border-radius: 8px; "
                "  padding: 12px 16px; font-size: 14px; text-align: left; "
                "} "
                "QPushButton:hover { background-color: #1a2744; color: #e0e0e0; } "
                "QPushButton:checked { background-color: #0f3460; color: #64b5f6; font-weight: bold; }"
            )
            btn.clicked.connect(lambda checked, idx=page_idx: self._navigate(idx))
            side_layout.addWidget(btn)
            self.nav_buttons.append((btn, page_idx))

        side_layout.addStretch()

        # Footer
        footer = QLabel("Built with PySide6")
        footer.setStyleSheet("font-size: 10px; color: #37474f; padding: 8px;")
        footer.setAlignment(Qt.AlignCenter)
        side_layout.addWidget(footer)

        main_layout.addWidget(sidebar)

        # ---- Content area ----
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: #1a1a2e;")

        self.home_page = HomePage()
        self.lesson_page = LessonPage()
        self.keyboard_page = KeyboardPage()
        self.practice_page = PracticePage()
        self.quiz_page = QuizPage()
        self.dict_page = DictionaryPage()

        self.stack.addWidget(self.home_page)       # 0
        self.stack.addWidget(self.lesson_page)      # 1
        self.stack.addWidget(self.keyboard_page)    # 2
        self.stack.addWidget(self.practice_page)    # 3
        self.stack.addWidget(self.quiz_page)        # 4
        self.stack.addWidget(self.dict_page)        # 5

        main_layout.addWidget(self.stack)

        # Default page
        self._navigate(0)

    def _navigate(self, page_idx):
        self.stack.setCurrentIndex(page_idx)
        for btn, idx in self.nav_buttons:
            btn.setChecked(idx == page_idx)


# ==================== ENTRY POINT ====================

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Apply dark palette as base
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#1a1a2e"))
    palette.setColor(QPalette.WindowText, QColor("#e0e0e0"))
    palette.setColor(QPalette.Base, QColor("#16213e"))
    palette.setColor(QPalette.AlternateBase, QColor("#1a2744"))
    palette.setColor(QPalette.ToolTipBase, QColor("#16213e"))
    palette.setColor(QPalette.ToolTipText, QColor("#e0e0e0"))
    palette.setColor(QPalette.Text, QColor("#e0e0e0"))
    palette.setColor(QPalette.Button, QColor("#0f3460"))
    palette.setColor(QPalette.ButtonText, QColor("#e0e0e0"))
    palette.setColor(QPalette.BrightText, QColor("#e94560"))
    palette.setColor(QPalette.Highlight, QColor("#0f3460"))
    palette.setColor(QPalette.HighlightedText, QColor("#64b5f6"))
    app.setPalette(palette)

    # Apply stylesheet
    app.setStyleSheet(DARK_STYLESHEET)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()