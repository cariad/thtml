# Custom theming

A custom theme cane be specified as a dictionary in Python or YAML file on the command line.

The following scheme applies whether you're passing a dictionary or a YAML file.

## Default theme

The default theme can be found at [github.com/cariad/thtml/blob/main/thtml/themes/default.yml](https://github.com/cariad/thtml/blob/main/thtml/themes/default.yml)

## "class" type

Generally, a theme describes a library of CSS classes. Each class is described by this `class` type.

Each CSS class has the CSS properties you'd expect, plus some additional details about how it should be included in a render.

### "name" property

The `name` property prescribes the name of the CSS class. Do not prefix the name with a dot as you would in a stylesheet.

```yaml
name: thtml
```

### "headers" property

The `headers` property prescribes a list of strings that should be injected into the top of the stylesheet to satisfy the class' `styles`.

These would typically be `@import`, `@keyframes`, and other statements of the like.

These headers are injected only for classes that are included in the render.

```yaml
headers:
  - "@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400&display=swap');"
```

### "styles" property

The `variables` property prescribes the CSS styles to apply to the class. Do not end the statements with semicolons; these will be added during the render.

```yaml
styles:
  background: var(--black)
  color: var(--white)
```

### "variables" property

The `variables` property prescribes the names of [variables](#theme-variables) that need to be set to satisfy the class' `styles`.

```yaml
variables:
  - black
  - white
```

### Full "class" example

```yaml
name: thtml
headers:
  - "@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400&display=swap');"
variables:
  - black
  - default-font
  - white
styles:
  background: var(--black)
  border-radius: 1rem
  color: var(--white)
  font-family: var(--default-font)
  letter-spacing: 0.03rem
  padding: 2rem
  width: max-content
```

## Theme scheme

### Theme "defaults"

The `defaults` property prescribes a list of [`class`](#class-type) that should _always_ be included in the render.

Note that CSS variables will be injected into the first [`class`](#class-type) of this list during the render.

```yaml
defaults:
  - name: thtml
    headers:
      - "@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400&display=swap');"
    variables:
      - black
      - default-font
      - white
    styles:
      background: var(--black)
      color: var(--white)
      font-family: var(--default-font)
```

### Theme "variables"

The `variables` property prescribes the full library of CSS variables that can be added to the render.

A variable will be added only if it's marked as required by a [`class`](#class-type) during the render.

```yaml
variables:
  black: "#000"
  default-font: "'Roboto Mono'"
  white: "#CCC"
```

### Theme "classes"

The `classes` property prescribes the full library of [`class`](#class-type) that can be added to the render.

The [`class`](#class-type) names are significant, and describe all the supported ANSI escape codes. For example, `background-black` describes the CSS styling to apply to text described as having a "black background".

Refer to the [default theme](https://github.com/cariad/thtml/blob/main/thtml/themes/default.yml) for a full list of [`class`](#class-type) names.
