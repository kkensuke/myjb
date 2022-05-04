# Markdown


>```
># Heading 1
>## Heading 2
>### Heading 3
>```
>
>># Heading 1
>>## Heading 2
>>### Heading 3
---


## horizontal rule
```
---
```
---


## list
>```
>- list item 1
>- list item 2
>- list item 3
>    - list item 3-1
>    - list item 3-2
>        - list item 3-2-1
>        * list item 3-2-2
>        + list item 3-2-3
>
>1. list item 1
>2. list item 2
>3. list item 3
>    1. list item 3-1
>    2. list item 3-2
>```
>
>>- list item 1
>>- list item 2
>>- list item 3
>>    - list item 3-1
>>    - list item 3-2
>>        - list item 3-2-1
>>        * list item 3-2-2
>>        + list item 3-2-3
>>
>>
>>1. list item 1
>>2. list item 2
>>3. list item 3
>>    1. list item 3-1
>>    2. list item 3-2
---

## Color
>```
><font color="red">赤い文字！！！</font>
>```
>><font color="red">赤い文字！！！</font>
---

## Code
>````
>```python
>import streamlit as st
>import numpy as np
>import pandas as pd
>```
>````
>>```python
>>import streamlit as st
>>import numpy as np
>>import pandas as pd
>>```
---

## Links
>```
>[Wikipedia: Viola–Jones object detection framework](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework)
>```
>>リンク
[Wikipedia: Viola–Jones object detection framework](https://en.wikipedia.org/wiki/Viola%E2%80%93Jones_object_detection_framework)
---

## Checkbox
>```
>- [ ] タスク1
>- [x] タスク2
>```
>>- [ ] タスク1
>>- [x] タスク2
---


## raw text, code, bold, italic, strikethrough
>````
>```
>asdf
>```
>
>`asdf`
>
>$\LaTeX$
>
>*asdf*
>_adsf_
>
>**asdf**
>__adsf__
>
>***asdf***
>___adsf___
>*__adsf__*
>~~asdf~~
>````
>>```
>>asdf
>>```
>>
>>`asdf`
>>
>>$\LaTeX$
>>
>>*asdf*
>>_adsf_
>>
>>**asdf**
>>__adsf__
>>
>>***asdf***
>>___adsf___
>>*__adsf__*
>>
>>~~asdf~~
---

## Latex
>```
>$$
>\left( \sum_{k=1}^n a_k b_k \right)^2 \leq
>\left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 >\right)
>$$
>```
>>$$
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq
\left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$

## Quote
>```
>> This is a quote.
>```
>> This is a quote.
---

## Table
>```
>| Header 1 | Header 2 | Header 3 |
>| :-------- | :--------: | --------: |
>| align=left | align=center | align=right |
>| cell 1   | cell 2   | cell 3   |
>| cell 4   | cell 5   | cell 6   |
>| caption |
>```
>>| Header 1 | Header 2 | Header 3 |
>>| :-------- | :--------: | --------: |
>>| align=left | align=center | align=right |
>>| cell 1   | cell 2   | cell 3   |
>>| cell 4   | cell 5   | cell 6   |
>>| caption |
---


## In-page link
>```
>[link to list](#list)
>```
>>[link to list](#list)
---


