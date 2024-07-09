# ✨ Anti-Glare Theme

It might be the best choice for those who can't see the code editor in <b>low light</b>. It's tailored to the needs of those of us who love to code late into the <b>night</b>.

## 🔸 Table of contents

-   [Theme Screenshots](#theme-screenshots)
-   [Getting started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Activate theme](#activate-theme)
-   [Recommended settings](#recommended-settings-for-a-better-experience)
-   [Included settings](#included-settings-for-a-better-experience)
-   [Additional Tips](#additional-tips)
    -   [ZSH Shell](#zsh-shell)
    -   [Starship](#starship)

## 🔸 Theme Screenshots

### 🔸 Anti-Glare - Official

[![official.png](https://i.postimg.cc/Xv01YgYL/official.png)](https://postimg.cc/XrQk2dFB)

### 🔸 Anti-Glare - Official - Italics

[![official-italics.png](https://i.postimg.cc/NGW6tjM7/official-italics.png)](https://postimg.cc/BtBLcs2X)

### 🔸 Anti-Glare - Moonlit

[![moonlit.png](https://i.postimg.cc/zfshrdDD/moonlit.png)](https://postimg.cc/mcSk3yFK)

### 🔸 Anti-Glare - Moonlit - Italics

[![moonlit-italics.png](https://i.postimg.cc/yNgR2qHr/moonlit-italics.png)](https://postimg.cc/67KTGmTd)

### 🔸 Anti-Glare - Nebula

[![nebula.png](https://i.postimg.cc/BvkTvSp0/nebula.png)](https://postimg.cc/3yj4SHzS)

### 🔸 Anti-Glare - Nebula - Italics

[![nebula-italics.png](https://i.postimg.cc/ZRXVXP26/nebula-italics.png)](https://postimg.cc/MMb7QBWG)

## 🔸 Getting started

You can install this awesome theme through the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=azmarifdev.anti-glare-theme).

### 🔸 Prerequisites

This theme is compatible for VS Code version <b>1.16.0+</b>

### 🔸 Installation

Launch _Quick Open_:

-   <img src="https://www.kernel.org/theme/images/logos/favicon.png" width=16 height=16/> <a href="https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf">Linux</a> `Ctrl+P`
-   <img src="https://developer.apple.com/favicon.ico" width=16 height=16/> <a href="https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf">macOS</a> `⌘P`
-   <img src="https://www.microsoft.com/favicon.ico" width=16 height=16/> <a href="https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf">Windows</a> `Ctrl+P`

Paste the following command and press `Enter`:

```shell
ext install anti-glare-theme
```

And pick the one by **A. Z. M. Arif** as author.

## 🔸 Activate theme

Launch _Quick Open_:

-   <img src="https://www.kernel.org/theme/images/logos/favicon.png" width=16 height=16/> <a href="https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf">Linux</a> `Ctrl + Shift + P`
-   <img src="https://developer.apple.com/favicon.ico" width=16 height=16/> <a href="https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf">macOS</a> `⌘ + Shift + P`
-   <img src="https://www.microsoft.com/favicon.ico" width=16 height=16/> <a href="https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf">Windows</a> `Ctrl + Shift + P`

Type `theme`, choose `Preferences: Color Theme`, and select <b> _Anti-Glare Theme_ </b> from the list. After activation, the theme will be activated.

## 🔸 Recommended settings for a better experience

First, _Download_ and _Install_ Recommended fonts from here: <b>[Click me](https://github.com/azmarifdev/vsfonts/)</b>

After that, add the following codes to the `settings.json`

```js
{
    // Controls the editor font family.
    "editor.fontFamily": "Operator-Caska",
    // Controls the terminal font family.
    "terminal.fontFamily": "CaskaydiaCove Nerd Font Mono"
}
```

## 🔸 Included settings for a better experience

I have included some required settings in this theme. Therefore, this theme will be more suitable for <b>night coding</b>. Here are the settings.

<details>
  <summary><b>🔴 Click me 🔰 </b></summary>

```js
{
    "editor.lineHeight": 2,
    "editor.cursorBlinking": "expand",
    "editor.cursorWidth": 2,
    "editor.fontSize": 14.5,
    "editor.hover.delay": 700,
    "editor.linkedEditing": true,
    "editor.roundedSelection": true,
    "editor.formatOnSave": true,
    "editor.mouseWheelScrollSensitivity": 2,
    "diffEditor.wordWrap": "on",
    "diffEditor.ignoreTrimWhitespace": true,
    "editor.accessibilitySupport": "off",
    "editor.find.addExtraSpaceOnTop": false,
    "editor.fontLigatures": true,
    "editor.find.cursorMoveOnType": true,
    "editor.formatOnType": true,
    "editor.formatOnPaste": true,
    "editor.renderLineHighlight": "none",
    "editor.scrollbar.verticalScrollbarSize": 8,
    "editor.scrollbar.horizontalScrollbarSize": 8,
    "editor.scrollbar.horizontal": "auto",
    "editor.smoothScrolling": true,
    "editor.scrollbar.scrollByPage": true,
    "editor.foldingImportsByDefault": true,
    "editor.minimap.renderCharacters": true,
    "editor.minimap.maxColumn": 50,
    "editor.minimap.showSlider": "always",
    "editor.minimap.size": "fill",
    "editor.cursorSmoothCaretAnimation": "on",
    "editor.overviewRulerBorder": false,
    "editor.hideCursorInOverviewRuler": true,
    "editor.bracketPairColorization.enabled": true,
    "editor.parameterHints.cycle": true,
    "editor.parameterHints.enabled": true,
    "editor.smoothScrolling": true,
    "output.smartScroll.enabled": true,
    "debug.console.fontSize": 13,
    "terminal.integrated.cursorWidth": 2,
    "terminal.integrated.cursorStyle": "underline",
    "terminal.integrated.cursorBlinking": true,
    "terminal.integrated.lineHeight": 1.2,
    "terminal.integrated.letterSpacing": 1,
    "terminal.integrated.fontSize": 13,
    "terminal.integrated.allowMnemonics": true,
    "terminal.integrated.copyOnSelection": false,
    "terminal.integrated.fastScrollSensitivity": 4,
    "terminal.explorerKind": "both",
    "terminal.integrated.enableMultiLinePasteWarning": "auto",
    "terminal.integrated.enableVisualBell": true,
    "terminal.sourceControlRepositoriesKind": "both",
    "accessibility.signals.terminalBell": {
        "sound": "off"
    }
}
```

</details>

## 🔸 Additional Tips

### 💠 ZSH Shell

If you want to use a powerful shell, you can use <b>ZSH</b>. It has some notable feature.

🔆 <b>Example:</b>

-   Enhanced Functionality
-   Programmable Completion
-   Themed Prompts
-   Extended File Globbing
-   Improved Variable Handling
-   Multi-line Editing
-   Spelling Correction and Autofill

So, if you want to install <b>ZSH</b> you can follow my GitHub gist. <b>[ZSH Gist](https://gist.github.com/azmarifdev/9c16c5a33e93aee05b35147fe7da1015)</b>

#

### 💠 <b>Starship</b>

<b>Starship</b> is a modern and feature-rich prompt designed for various shells, including Zsh, Bash, and Fish. It goes beyond a simple command line prompt by offering. It has some notable feature.

🔆 <b>Example:</b>

-   Sleek and Customizable Appearance
-   Blazing Fast Performance
-   Cross-Shell Compatibility
-   Contextual Information at a Glance
-   Feature-rich and Intelligent

So, if you want to install <b>Starship</b> you can follow my GitHub gist. <b>[Starship Gist](https://gist.github.com/azmarifdev/b74f508c07d0af6f4edbbb6e480b53c1) </b>

#

🌟 BTW, If you want to know about me or contact me, go here:

[![Website](https://img.shields.io/badge/Website-6D4AFF?logo=Write.as&logoColor=white)](https://azmarif.dev/azmarifdev/) [![Email](https://img.shields.io/badge/Email-EA4335?logo=Gmail&logoColor=white)](mailto:contact@azmarif.dev) [![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white)](https://discord.gg/PM8SWkRBBn) [![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)](https://facebook.com/azmarifdev) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/azmarifdev) [![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)](https://twitter.com/azmarifdev) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://www.youtube.com/@azmarifdev)

#
<p align="center">Copyright &copy; 2024 - A. Z. M. Arif</p>