# thtml

CLI tool and Python package for converting text to HTML

```text
This is just a text code block.

It's here so I can check out the style.
```

<!-- markdownlint-disable MD033 -->
<div style="font-family: monospace;">
  <span style="color: #f00;">Hello</span> <span style="color: #0f0;">world!</span>
</div>
<!-- markdownlint-enable MD033 -->

This one uses CSS:

<!-- markdownlint-disable MD033 -->
<style type="text/css">
  .thtml {
    font-family: monospace;
  }

  .thtml .fg-red {
    color: #f00;
  }

  .thtml .fg-green {
    color: #0f0;
  }
</style>

<!-- "nohighlight" prevents highlight.js taking over the styling -->

<pre class="nohighlight thtml">
  <code>
    <span class="fg-red">Hello</span> <span class="fg-green">world!</span>
  </code>
</pre>
<!-- markdownlint-enable MD033 -->
