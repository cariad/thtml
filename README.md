# thtml

[![CircleCI](https://circleci.com/gh/cariad/thtml/tree/main.svg?style=shield)](https://circleci.com/gh/cariad/thtml/tree/main)

CLI tool and Python package for converting text to HTML

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

<pre class="thtml">
  <code>
    <span class="fg-red">Hello</span> <span class="fg-green">world!</span>
  </code>
</pre>
<!-- markdownlint-enable MD033 -->
