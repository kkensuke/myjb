---
substitutions:
  key1: "I'm a **substitution**"
  key2: |
    ```{note}
    {{ key1 }}
    ```
  image: |
    ```{image} ../programming/github/img/GitHub-flow.png
    :alt: image
    :width: 200px
    ```
---
#  MyST

% This file provide you the MyST syntax.

>## Heading
>```
># Heading level 1
>## Heading level 2
>### Heading level 3
>#### Heading level 4
>##### Heading level 5
>###### Heading level 6
>```
>>
>># Heading level 1
>>## Heading level 2
>>### Heading level 3
>>#### Heading level 4
>>##### Heading level 5
>>###### Heading level 6
>>


## Target headers
>```
>(target)=
>### target
>...
>see [target](target)
>```
(target)=
### target
...
see [target](target)

## Quote
>```
>> this is a quote
>```
>>this is a quote


## End line
>```
>This is the end of some text.
>---
>```
>>This is the end of some text.
>>---

## Line comment
>```
>% This is a line comment.
>```
>>% This is a line comment.
## Block break
>```
>This is an example of
>+++ {"meta": "data"}
>a block break
>```
>>This is an example of
>>+++ {"meta": "data"}
>>a block break

## List
>```
>1. First item
>2. Second item
>    * First sub-item
>    * Second sub-item
>      * Third subsub-item
>```
>>1. First item
>>2. Second item
>>    * First sub-item
>>    * Second sub-item
>>      * Third subsub-item

## Table
>````
>```{list-table} This table title
>:header-rows: 1
>:name: example-table
>
>* - Training
>  - Validation
>* - 0
>  - 5
>* - 13720
>  - 2744
>```
>````
>
```{list-table} This table title
:header-rows: 1
:name: example-table

* - Training
  - Validation
* - 0
  - 5
* - 13720
  - 2744
```


## admonition
>````
>```{admonition} This is a title
>An example of an admonition with a title.
>```
>````
>```{admonition} This is a title
>An example of an admonition with a title.
>```

>````
>```{note} Notes require **no** arguments,
>so content can start here.
>```
>````
>```{note}
>Notes require **no** arguments,
>so content can start here.
>```

>````
>```{warning} Warnings require **no** arguments,
>so content can start here.
>```
>````
>```{warning}
>Warnings
>```

>````
>```{tip}
>Tip
>```
>````
>```{tip}
>Tip
>```

>````
>```{caution}
>Caution
>```
>````
>```{caution}
>Caution
>```

>````
>```{attention}
>Attention
>```
>````
>```{attention}
>Attention
>```

>````
>```{danger}
>Danger
>```
>````
>```{danger}
>Danger
>```

>````
>```{error}
>Error
>```
>````
>```{error}
>Error
>```

>````
>```{hint}
>hint
>```
>````
>```{hint}
>hint
>```


>````
>```{important}
>Important
>```
>````
>```{important}
>Important
>```

>````
>```{seealso}
>see also
>```
>````
>```{seealso}
>see also
>```

>```
>{fa}`check, text-success mr-1` This is an example of Roles (check mark & success color).
>```
>>{fa}`check, text-success mr-1` This is an example of Roles (check mark & success color).

>```
>{fa}`check, text-info mr-1` This is an example of Roles (check mark & info color).
>```
>>{fa}`check, text-info mr-1` This is an example of Roles (check mark & info color).


### Figure parameters

The following options are supported:

`scale` : integer percentage
: Uniformly scale the figure. The default is “100” which indicates no scaling. The symbol “%” is optional.

`width` : length or percentage
: You can set the figure width in the following units: “em”, “ex”, “px”,“in” ,“cm”, “mm”, “pt”, “pc”, “%”.

`height` : length
: You can set the figure height in the following units: “em”, “ex”, “px”, “in”, “cm”, “mm”, “pt”, “pc”.

`alt` : text
: Text to be displayed if the figure cannot be displayed or if the reader is using assistive technologies. Generally entails a short description of the figure.

`align` : “left”, “center”, or “right”
: Align the figure left, center, or right. Default alignment is center.

`name` : text
: A unique identifier for your figure that you can use to reference it with {ref} or {numref} roles. Cannot contain spaces or special characters.

`figclass` : text
: Value of the figure’s class attribute which can be used to add custom CSS or JavaScript. Predefined options include:

## Math
>```
>This is an example of an
>inline equation $z=\sqrt{x^2+y^2}$.
>```
>>This is an example of an
>>inline equation $z=\sqrt{x^2+y^2}$.

>```
>$$
>z=\sqrt{x^2+y^2}
>$$ (mylabel)
>equation ref: {eq}`mylabel`
>```
>>$$z=\sqrt{x^2+y^2}$$ (mylabel)
>>equation ref: {eq}`mylabel`



## Executable code

<!--
```{code-cell} ipython3
note = "Python syntax highlighting"
print(note)
```
-->

## Reference documents

>```
>See {doc}`../programming/alias` for more information.
>```
>>See {doc}`../programming/alias` for more information.

## Toggle
>`````
>````{toggle}
>```python
>print('hello')
>```
>````
>`````
>>````{toggle}
>>```python
>>print('hello')
>>```
>>````

## Margin
>````
>```{margin} **My margin title**
>Here is my margin content, it is pretty cool!
>```
>````
>>```{margin} **My margin title**
>>Here is my margin content, it is pretty cool!
>>```
---

>```
>:::{tip}
>:class: margin toggle
>This note will be in the margin!
>:::
>```
>>:::{tip}
>>:class: margin toggle
>>This note will be in the margin!
>>:::
---

% :class: toggle = :class: dropdown?

>````
>``{figure} ./gitHub/img/GitHub-flow.png
>---
>figclass: margin
>alt: My figure text
>name: myfig4
>---
>And here is my figure caption
>```
>````
>>```{figure} ../programming/github/img/GitHub-flow.png
>>---
>>figclass: margin
>>alt: My figure text
>>name: myfig4
>>---
>>And here is my figure caption
>>```

<!--
```{typescript}
asdf
asdf
asdf
```
-->


## Panel
https://sphinx-panels.readthedocs.io/en/latest/#panels-usage

>`````
>````{panels}
>Panel header 1
>^^^
>Panel body 1
>+++
>Panel footer 1
>---
>
>Panel header 2
>^^^
>Panel body 2
>+++
>Panel footer 2
>````
>`````
>>````{panels}
>>Panel header 1
>>^^^
>>Panel body 1
>>+++
>>Panel footer 1
>>---
>>
>>Panel header 2
>>^^^
>>Panel body 2
>>+++
>>Panel footer 2
>>````

## Badge
>```
>{badge}`primary,badge-primary`
>{badge}`primary,badge-primary badge-pill`
>
>{badge}`primary,badge-primary`
>{badge}`secondary,badge-secondary`
>{badge}`info,badge-info`
>{badge}`success,badge-success`
>{badge}`danger,badge-danger`
>{badge}`warning,badge-warning`
>{badge}`light,badge-light`
>{badge}`dark,badge-dark`
>```
>>{badge}`primary,badge-primary`
>>{badge}`primary,badge-primary badge-pill`
>>
>>{badge}`primary,badge-primary`
>>{badge}`secondary,badge-secondary`
>>{badge}`info,badge-info`
>>{badge}`success,badge-success`
>>{badge}`danger,badge-danger`
>>{badge}`warning,badge-warning`
>>{badge}`light,badge-light`
>>{badge}`dark,badge-dark`


%{link-badge}`https://example.com,cls=badge-primary text-white,tooltip=a tooltip`
%{link-badge}`https://example.com,"my, text",cls=badge-dark text-white`
%{link-badge}`panels/usage,my reference,ref,badge-success text-white,hallo`

### dropdown
>`````
>````{dropdown}
>:animate: fade-in-slide-down
>```
>git add .
>git commit -m "update"
>git push origin main
>```
>````
>`````
>>````{dropdown}
>>:animate: fade-in-slide-down
>>```
>>git add .
>>git commit -m "update"
>>git push origin main
>>```
>>````

% fade-in, fade-in-slide-down : fade in for the first time
>````
>```{admonition} Click the button to reveal!
>:class: dropdown
>Some hidden toggle content!
>```
>````
>
>>```{admonition} Click the button to reveal!
>>:class: dropdown
>>Some hidden toggle content!
>>```
## Definition lists
>```
>Term 1
>: Definition
>
>Term 2
>: Definition
>```
>>Term 1
>>: Definition
>>
>>Term 2
>>: Definition

>````
>```{glossary}
>Term one
>  An indented explanation of term 1
>
>A second term
>  An indented explanation of term2
>```
>````
>>```{glossary}
>>Term one
>>  An indented explanation of term 1
>>
>>A second term
>>  An indented explanation of term2
>>```

>````
>```{epigraph}
>Here is a cool quotation.
>
>-- Jo the Jovyan
>```
>````
>>```{epigraph}
>>Here is a cool quotation.
>>
>>-- Jo the Jovyan
>>```

### tabs

ex1
>````
>```{tabbed} Tab 1 title
>My first tab
>```
>
>```{tabbed} Tab 2 title
>My second tab with `some code`!
>```
>````
>>```{tabbed} Tab 1 title
>>My first tab
>>```
>>
>>```{tabbed} Tab 2 title
>>My second tab with `some code`!
>>```


ex2
>`````
>````{tabbed} c++
>
>```{code-block} c++
>
>int main(const int argc, const char **argv) {
>  return 0;
>}
>```
>````
>
>````{tabbed} python
>
>```{code-block} python
>
>def main():
>    return
>```
>````
>
>````{tabbed} java
>
>```{code-block} java
>
>class Main {
>    public static void main(String[] args) {
>    }
>}
>```
>````
>
>````{tabbed} julia
>
>```{code-block} julia
>
>function main()
>end
>```
>````
>
>````{tabbed} fortran
>
>```{code-block} fortran
>
>PROGRAM main
>END PROGRAM main
>```
>````
>`````
>
>>````{tabbed} c++
>>
>>```{code-block} c++
>>
>>int main(const int argc, const char **argv) {
>>  return 0;
>>}
>>```
>>````
>>
>>````{tabbed} python
>>
>>```{code-block} python
>>
>>def main():
>>    return
>>```
>>````
>>
>>````{tabbed} java
>>
>>```{code-block} java
>>
>>class Main {
>>    public static void main(String[] args) {
>>    }
>>}
>>```
>>````
>>
>>````{tabbed} julia
>>
>>```{code-block} julia
>>
>>function main()
>>end
>>```
>>````
>>
>>````{tabbed} fortran
>>
>>```{code-block} fortran
>>
>>PROGRAM main
>>END PROGRAM main
>>```
>>````

## key

To use a substitution, first add front-matter content to the top of a page like so:
````
---
substitutions:
  image: |
    ```{image} Programming/GitHub/img/GitHub-flow.png
    :alt: image
    :width: 200px
    ```
---
````
and use like this: `{{image}}`

{{image}}


### Define substitutions for your whole book

You can also define book-level substitution variables with the following configuration:

```
parse:
  myst_substitutions:
    key0: global-value
```
global value: {{key0}}


### Formatting substitutions
The original key1: {{ key1 }}
{{ key1 | replace("a substitution", "the best substitution")}}

```
substitutions:
  repo_url: [my repo url](https://github.com/executablebooks/jupyter-book)
```

## Footnotes
>```
>This is a footnote[^mylabel].
>[^mylabel]: My footnote text.
>```
>>This is a footnote[^mylabel].
>>[^mylabel]: My footnote text.
## Custom \<div> blocks
>````
>```{div} my-class
>**Some content.**
>```
>````
>>```{div} my-class
>>**Some content.**
>>```
## Check for missing references

You can check for missing references when building a Jupyter Book. To do so, use the following options:
```
jupyter-book build -W -n --keep-going docs/
```

## Layout
full-width
>````
>```{note}
>:class: full-width
>Here's a note that will take the full width
>```
>````
>>```{note}
>>:class: full-width
>>Here's a note that will take the full width
>>```

## Proofs, Theorems, and Algorithms

This is not currently a default package in jupyter-book as is a relatively new package.
```
pip install sphinx-proof
```

It needs to be enabled through the _config.yml after installation.

```
sphinx:
  extra_extensions:
    - sphinx_proof
```

https://sphinx-proof.readthedocs.io/en/latest/syntax.html

# Build and publish outputs
## Store code outputs and insert into content
https://jupyterbook.org/content/executable/output-insert.html

## Generate a badge for your book
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](<https://github.com/kk564/jb-test.git>)
Additionally, you can generate a badge directly from [shields.io](https://shields.io/). Here’s the URL to auto-generate the badge above, using a base64-encoded version of the Jupyter Book logo. Feel free to modify this as you wish!

## Build a PDF using LaTeX

### Book Style PDF

To build a PDF of your project using LaTeX, use the following command:
```
jupyter-book build mybookname/ --builder pdflatex [--individualpages]

or
jb build mybookname/ --builder pdflatex [--individualpages]
```

<!--
````{note}
If you would just like to generate the latex file you may use:
```
jb build mybookname/ --builder latex
```
````
-->

## Check external links in your book

If you’d like to make sure that the links outside of your book are valid, run the Sphinx link checker with Jupyter Book. This will check each of your external links and ensure that they resolve.

Note that you must ensure each link is the right target, the link checker will only ensure that it resolves.
To run the link checker, use the following command:
```
jupyter-book build mybookname/ --builder linkcheck
```
It will print the status of each link in your book so that you may resolve any incorrect links later on.

## Configuring to Improve Accessibility

Declaring the primary language used in your book assists screen reader and browser translation tools.

Language can be configured by providing the appropriate language code to the language option, under sphinx configuration in your _config.yml file:
```
sphinx:
  config:
    language: en
```


## Defining TeX macros

You can add LaTeX macros for the whole book by defining them under the Macros option of the TeX block. For example, the following two macros have been pre-defined in the Sphinx configuration
```
sphinx:
  config:
    mathjax_config:
      TeX:
        Macros:
          "N": "\\mathbb{N}"
          "floor": ["\\lfloor#1\\rfloor", 1]
          "bmat" : ["\\left[\\begin{array}"]
          "emat" : ["\\end{array}\\right]"]
```
You can also define TeX macros for a specific file by introducing them at the beginning of the file under a math directive. For example

````
```{math}
\newcommand\N{\mathbb{N}}
\newcommand\floor[1]{\lfloor#1\rfloor}
\newcommand{\bmat}{\left[\begin{array}}
\newcommand{\emat}{\end{array}\right]}
```
````


## API reference from docstrings


