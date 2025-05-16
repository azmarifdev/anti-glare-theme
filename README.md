# ✨ Anti-Glare Theme

## A Professional VS Code Theme for Low-Light Environments

[![Version](https://img.shields.io/badge/version-1.5.0-blue.svg)](https://marketplace.visualstudio.com/items?itemName=azmarifdev.anti-glare-theme)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/azmarifdev.anti-glare-theme)](https://marketplace.visualstudio.com/items?itemName=azmarifdev.anti-glare-theme)
[![Ratings](https://img.shields.io/visual-studio-marketplace/r/azmarifdev.anti-glare-theme?cacheSeconds=60)](https://marketplace.visualstudio.com/items?itemName=azmarifdev.anti-glare-theme)
[![GitHub](https://img.shields.io/github/license/azmarifdev/anti-glare-theme)](https://github.com/azmarifdev/anti-glare-theme/blob/main/LICENSE.md)

Anti-Glare is a professionally designed theme optimized for developers who code in <b>low-light environments</b>. Meticulously crafted to reduce eye strain during <b>night-time coding sessions</b>, this theme offers optimal contrast and carefully selected color palettes to enhance readability while maintaining a comfortable visual experience.

## 🔸 Table of Contents

-   [Features](#features)
-   [Theme Variants](#theme-variants)
-   [Installation](#installation)
-   [Activation](#activation)
-   [Recommended Configuration](#recommended-configuration)
-   [Included Settings](#included-settings)
-   [Productivity Enhancements](#productivity-enhancements)
    -   [ZSH Shell Integration](#zsh-shell-integration)
    -   [Starship Terminal Prompt](#starship-terminal-prompt)
-   [Release Notes](#release-notes)
-   [Feedback & Contributions](#feedback--contributions)
-   [License](#license)

## 🔸 Features

-   **Eye Comfort**: Designed specifically to reduce eye strain in low-light environments
-   **Multiple Variants**: Choose from three distinct theme styles with optional italics support
-   **Optimized Contrast**: Carefully balanced color schemes for readability without harshness
-   **Syntax Highlighting**: Enhanced syntax coloring for improved code comprehension
-   **UI Consistency**: Harmonious integration with VS Code's interface elements
-   **Productivity Settings**: Includes optimized editor configurations for efficient coding

## 🔸 Theme Variants

Anti-Glare Theme offers six different variants to match your personal preferences and coding style:

### Anti-Glare Official

Our flagship theme with a perfect balance of contrast and color harmony.

[![Official](https://i.postimg.cc/Xv01YgYL/official.png)](https://postimg.cc/XrQk2dFB)

### Anti-Glare Official Italics

The same balanced color scheme with added italics for comments and keywords.

[![Official Italics](https://i.postimg.cc/NGW6tjM7/official-italics.png)](https://postimg.cc/BtBLcs2X)

### Anti-Glare Moonlit

A softer variant with blue undertones for a more calming late-night experience.

[![Moonlit](https://i.postimg.cc/zfshrdDD/moonlit.png)](https://postimg.cc/mcSk3yFK)

### Anti-Glare Moonlit Italics

The Moonlit variant with elegant italics for enhanced code expression.

[![Moonlit Italics](https://i.postimg.cc/yNgR2qHr/moonlit-italics.png)](https://postimg.cc/67KTGmTd)

### Anti-Glare Nebula

A rich color scheme inspired by cosmic nebulae for a unique coding atmosphere.

[![Nebula](https://i.postimg.cc/BvkTvSp0/nebula.png)](https://postimg.cc/3yj4SHzS)

### Anti-Glare Nebula Italics

The Nebula variant with stylistic italics for additional code differentiation.

[![Nebula Italics](https://i.postimg.cc/ZRXVXP26/nebula-italics.png)](https://postimg.cc/MMb7QBWG)

## 🔸 Installation

You can install the Anti-Glare Theme through the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=azmarifdev.anti-glare-theme).

### Prerequisites

-   Visual Studio Code (version 1.16.0 or higher)

### Installation Methods

#### Via VS Code Marketplace

1. Open VS Code
2. Navigate to Extensions view by clicking the Extensions icon in the Activity Bar or pressing:
    - <img src="https://www.kernel.org/theme/images/logos/favicon.png" width=16 height=16/> Linux: `Ctrl+Shift+X`
    - <img src="https://developer.apple.com/favicon.ico" width=16 height=16/> macOS: `⌘+Shift+X`
    - <img src="https://www.microsoft.com/favicon.ico" width=16 height=16/> Windows: `Ctrl+Shift+X`
3. Search for `Anti-Glare Theme`
4. Click **Install**

#### Via Quick Open

1. Launch Quick Open:
    - <img src="https://www.kernel.org/theme/images/logos/favicon.png" width=16 height=16/> Linux: `Ctrl+P`
    - <img src="https://developer.apple.com/favicon.ico" width=16 height=16/> macOS: `⌘P`
    - <img src="https://www.microsoft.com/favicon.ico" width=16 height=16/> Windows: `Ctrl+P`
2. Paste the following command and press `Enter`:

```shell
ext install azmarifdev.anti-glare-theme
```

## 🔸 Activation

1. Launch Command Palette:
    - <img src="https://www.kernel.org/theme/images/logos/favicon.png" width=16 height=16/> Linux: `Ctrl+Shift+P`
    - <img src="https://developer.apple.com/favicon.ico" width=16 height=16/> macOS: `⌘+Shift+P`
    - <img src="https://www.microsoft.com/favicon.ico" width=16 height=16/> Windows: `Ctrl+Shift+P`
2. Type `Color Theme` and select `Preferences: Color Theme`
3. Select one of the Anti-Glare variants from the dropdown menu:
    - Anti-Glare - Official
    - Anti-Glare - Official - Italics
    - Anti-Glare - Moonlit
    - Anti-Glare - Moonlit - Italics
    - Anti-Glare - Nebula
    - Anti-Glare - Nebula - Italics

## 🔸 Recommended Configuration

To enhance your experience with Anti-Glare Theme, we recommend using these optimized font settings.

### Font Installation

Download and install our recommended fonts for the best visual experience:

-   [Download VS Code Optimized Fonts](https://github.com/azmarifdev/vsfonts/)

### Editor Configuration

Add the following settings to your `settings.json` file:

```json
{
    // Use a programming font with ligatures for code
    "editor.fontFamily": "Operator-Caska",

    // Use a nerd font for the terminal to support icons and special characters
    "terminal.fontFamily": "CaskaydiaCove Nerd Font Mono"
}
```

## 🔸 Included Settings

Anti-Glare Theme comes with carefully configured editor settings optimized for night-time coding sessions and productivity. These settings are automatically applied when you use the theme:

<details>
  <summary><b>🔹 Click to View Included Settings</b></summary>

```json
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

## 🔸 Productivity Enhancements

Enhance your development environment with these complementary tools that work perfectly with Anti-Glare Theme.

### ZSH Shell Integration

Boost your terminal productivity with ZSH's powerful features:

-   **Enhanced Tab Completion**: Context-aware suggestions
-   **Improved History Management**: Smart search through command history
-   **Advanced Globbing**: Powerful file pattern matching
-   **Spelling Correction**: Automatic correction of mistyped commands
-   **Theming Support**: Customizable prompt styles that complement Anti-Glare

[Installation Guide for ZSH Configuration](https://gist.github.com/azmarifdev/9c16c5a33e93aee05b35147fe7da1015)

### Starship Terminal Prompt

Enhance your terminal experience with Starship's modern, informative prompt:

-   **Context-Aware Information**: See relevant details based on your current directory
-   **Git Integration**: Instant visual feedback on repository status
-   **Performance Optimized**: Lightning fast even in large repositories
-   **Cross-Shell Compatibility**: Works across Bash, ZSH, and Fish
-   **Visual Harmony**: Clean design that pairs perfectly with Anti-Glare Theme

[Installation Guide for Starship](https://gist.github.com/azmarifdev/b74f508c07d0af6f4edbbb6e480b53c1)

## 🔸 Release Notes

See our [CHANGELOG.md](https://github.com/azmarifdev/anti-glare-theme/blob/main/CHANGELOG.md) for detailed information about each release.

### Latest Updates (v1.5.0)

-   Added improved syntax highlighting for TypeScript and React
-   Enhanced terminal color scheme for better readability
-   Fixed contrast issues in the activity bar and status bar
-   Optimized editor configurations for reduced eye strain

## 🔸 Feedback & Contributions

Your feedback helps make Anti-Glare Theme better! If you encounter issues or have suggestions:

-   [Report a bug](https://github.com/azmarifdev/anti-glare-theme/issues)
-   [Request a feature](https://github.com/azmarifdev/anti-glare-theme/issues)
-   [Submit a pull request](https://github.com/azmarifdev/anti-glare-theme/pulls)

## 🔸 License

This theme is released under the [MIT License](https://github.com/azmarifdev/anti-glare-theme/blob/main/LICENSE.md).

---

<div align="center">

### Connect with the Developer

[![Website](https://img.shields.io/badge/Website-6D4AFF?logo=write.as&logoColor=white&style=flat-square)](https://azmarif.dev/)
[![Email](https://img.shields.io/badge/Email-EA4335?logo=gmail&logoColor=white&style=flat-square)](mailto:contact@azmarif.dev)
[![Discord](https://img.shields.io/badge/Discord-7289DA?logo=discord&logoColor=white&style=flat-square)](https://discord.gg/PM8SWkRBBn)
[![X](https://img.shields.io/badge/X-000000?logo=x&logoColor=white&style=flat-square)](https://x.com/azmarifdev)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?logo=facebook&logoColor=white&style=flat-square)](https://facebook.com/azmarifdev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white&style=flat-square)](https://linkedin.com/in/azmarifdev)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white&style=flat-square)](https://www.youtube.com/@azmarifdev)

**Anti-Glare Theme** © 2023-2025 by [A. Z. M. Arif](https://azmarif.dev). All Rights Reserved.

</div>