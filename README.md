<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Fat_Water_Separation_via_EPI_Team_2</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0 solid transparent;
  border-right: 0 solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0 solid transparent;
  border-bottom: 0 solid transparent;
}

/*
 * Lumino
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-CommandPalette-search {
  flex: 0 0 auto;
}

.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-DockPanel {
  z-index: 0;
}

.lm-DockPanel-widget {
  z-index: 0;
}

.lm-DockPanel-tabBar {
  z-index: 1;
}

.lm-DockPanel-handle {
  z-index: 2;
}

.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

.lm-Menu-item {
  display: table-row;
}

.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

.lm-MenuBar-item {
  box-sizing: border-box;
}

.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-SplitPanel-child {
  z-index: 0;
}

.lm-SplitPanel-handle {
  z-index: 1;
}

.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabPanel-tabBar {
  z-index: 1;
}

.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jp-Collapse-header {
  padding: 1px 12px;
  background-color: var(--jp-layout-color1);
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  text-transform: uppercase;
  user-select: none;
}

.jp-Collapser-icon {
  height: 16px;
}

.jp-Collapse-header-collapsed .jp-Collapser-icon {
  transform: rotate(-90deg);
  margin: auto 0;
}

.jp-Collapser-title {
  line-height: 25px;
}

.jp-Collapse-contents {
  padding: 0 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
  --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
  --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
  --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddAboveIcon {
  background-image: var(--jp-icon-add-above);
}

.jp-AddBelowIcon {
  background-image: var(--jp-icon-add-below);
}

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}

.jp-BellIcon {
  background-image: var(--jp-icon-bell);
}

.jp-BugDotIcon {
  background-image: var(--jp-icon-bug-dot);
}

.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}

.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}

.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}

.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}

.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}

.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}

.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}

.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}

.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}

.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}

.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}

.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}

.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}

.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}

.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}

.jp-CodeCheckIcon {
  background-image: var(--jp-icon-code-check);
}

.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}

.jp-CollapseAllIcon {
  background-image: var(--jp-icon-collapse-all);
}

.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}

.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}

.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}

.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}

.jp-DeleteIcon {
  background-image: var(--jp-icon-delete);
}

.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}

.jp-DuplicateIcon {
  background-image: var(--jp-icon-duplicate);
}

.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}

.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}

.jp-ErrorIcon {
  background-image: var(--jp-icon-error);
}

.jp-ExpandAllIcon {
  background-image: var(--jp-icon-expand-all);
}

.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}

.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}

.jp-FileIcon {
  background-image: var(--jp-icon-file);
}

.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}

.jp-FilterDotIcon {
  background-image: var(--jp-icon-filter-dot);
}

.jp-FilterIcon {
  background-image: var(--jp-icon-filter);
}

.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}

.jp-FolderFavoriteIcon {
  background-image: var(--jp-icon-folder-favorite);
}

.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}

.jp-HomeIcon {
  background-image: var(--jp-icon-home);
}

.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}

.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}

.jp-InfoIcon {
  background-image: var(--jp-icon-info);
}

.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}

.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}

.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}

.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}

.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}

.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}

.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}

.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}

.jp-LaunchIcon {
  background-image: var(--jp-icon-launch);
}

.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}

.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}

.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}

.jp-ListIcon {
  background-image: var(--jp-icon-list);
}

.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}

.jp-MoveDownIcon {
  background-image: var(--jp-icon-move-down);
}

.jp-MoveUpIcon {
  background-image: var(--jp-icon-move-up);
}

.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}

.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}

.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}

.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}

.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}

.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}

.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}

.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}

.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}

.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}

.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}

.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}

.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}

.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}

.jp-RunIcon {
  background-image: var(--jp-icon-run);
}

.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}

.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}

.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}

.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}

.jp-ShareIcon {
  background-image: var(--jp-icon-share);
}

.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}

.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}

.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}

.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}

.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}

.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}

.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}

.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}

.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}

.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}

.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}

.jp-UserIcon {
  background-image: var(--jp-icon-user);
}

.jp-UsersIcon {
  background-image: var(--jp-icon-users);
}

.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}

.jp-WordIcon {
  background-image: var(--jp-icon-word);
}

.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-TabBar .lm-TabBar-addButton {
  align-items: center;
  display: flex;
  padding: 4px;
  padding-bottom: 5px;
  margin-right: 1px;
  background-color: var(--jp-layout-color2);
}

.lm-TabBar .lm-TabBar-addButton:hover {
  background-color: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  width: var(--jp-private-horizontal-tab-width);
}

.lm-DockPanel-tabBar .lm-TabBar-content {
  flex: unset;
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}

/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}

.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}

.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}

.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}

.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}

.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}

.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}

.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}

.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}

/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}

.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}

.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}

.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}

.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}

.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}

.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}

/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

.jp-icon-dot[fill] {
  fill: var(--jp-warn-color0);
}

.jp-jupyter-icon-color[fill] {
  fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
}

.jp-notebook-icon-color[fill] {
  fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
}

.jp-json-icon-color[fill] {
  fill: var(--jp-json-icon-color, var(--jp-warn-color1));
}

.jp-console-icon-color[fill] {
  fill: var(--jp-console-icon-color, white);
}

.jp-console-icon-background-color[fill] {
  fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
}

.jp-terminal-icon-color[fill] {
  fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
}

.jp-terminal-icon-background-color[fill] {
  fill: var(
    --jp-terminal-icon-background-color,
    var(--jp-inverse-layout-color2)
  );
}

.jp-text-editor-icon-color[fill] {
  fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
}

.jp-inspector-icon-color[fill] {
  fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* stylelint-disable selector-max-class, selector-max-compound-selectors */

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}

.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* stylelint-enable selector-max-class, selector-max-compound-selectors */

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FormGroup-content fieldset {
  border: none;
  padding: 0;
  min-width: 0;
  width: 100%;
}

/* stylelint-disable selector-max-type */

.jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
  font-size: var(--jp-content-font-size2);
  border-color: var(--jp-input-border-color);
  border-style: solid;
  border-radius: var(--jp-border-radius);
  border-width: 1px;
  padding: 6px 8px;
  background: none;
  color: var(--jp-ui-font-color0);
  height: inherit;
}

.jp-FormGroup-content fieldset input[type='checkbox'] {
  position: relative;
  top: 2px;
  margin-left: 0;
}

.jp-FormGroup-content button.jp-mod-styled {
  cursor: pointer;
}

.jp-FormGroup-content .checkbox label {
  cursor: pointer;
  font-size: var(--jp-content-font-size1);
}

.jp-FormGroup-content .jp-root > fieldset > legend {
  display: none;
}

.jp-FormGroup-content .jp-root > fieldset > p {
  display: none;
}

/** copy of `input.jp-mod-styled:focus` style */
.jp-FormGroup-content fieldset input:focus,
.jp-FormGroup-content fieldset select:focus {
  -moz-outline-radius: unset;
  outline: var(--jp-border-width) solid var(--md-blue-500);
  outline-offset: -1px;
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FormGroup-content fieldset input:hover:not(:focus),
.jp-FormGroup-content fieldset select:hover:not(:focus) {
  background-color: var(--jp-border-color2);
}

/* stylelint-enable selector-max-type */

.jp-FormGroup-content .checkbox .field-description {
  /* Disable default description field for checkbox:
   because other widgets do not have description fields,
   we add descriptions to each widget on the field level.
  */
  display: none;
}

.jp-FormGroup-content #root__description {
  display: none;
}

.jp-FormGroup-content .jp-modifiedIndicator {
  width: 5px;
  background-color: var(--jp-brand-color2);
  margin-top: 0;
  margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
  flex-shrink: 0;
}

.jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
  background-color: var(--jp-error-color0);
  margin-right: 0.5em;
}

/* RJSF ARRAY style */

.jp-arrayFieldWrapper legend {
  font-size: var(--jp-content-font-size2);
  color: var(--jp-ui-font-color0);
  flex-basis: 100%;
  padding: 4px 0;
  font-weight: var(--jp-content-heading-font-weight);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-arrayFieldWrapper .field-description {
  padding: 4px 0;
  white-space: pre-wrap;
}

.jp-arrayFieldWrapper .array-item {
  width: 100%;
  border: 1px solid var(--jp-border-color2);
  border-radius: 4px;
  margin: 4px;
}

.jp-ArrayOperations {
  display: flex;
  margin-left: 8px;
}

.jp-ArrayOperationsButton {
  margin: 2px;
}

.jp-ArrayOperationsButton .jp-icon3[fill] {
  fill: var(--jp-ui-font-color0);
}

button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

/* RJSF form validation error */

.jp-FormGroup-content .validationErrors {
  color: var(--jp-error-color0);
}

/* Hide panel level error as duplicated the field level error */
.jp-FormGroup-content .panel.errors {
  display: none;
}

/* RJSF normal content (settings-editor) */

.jp-FormGroup-contentNormal {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
  margin-left: 7px;
  color: var(--jp-ui-font-color0);
}

.jp-FormGroup-contentNormal .jp-FormGroup-description {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-default {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
  font-size: var(--jp-content-font-size1);
  font-weight: normal;
  min-width: 120px;
}

.jp-FormGroup-contentNormal fieldset:not(:first-child) {
  margin-left: 7px;
}

.jp-FormGroup-contentNormal .field-array-of-string .array-item {
  /* Display `jp-ArrayOperations` buttons side-by-side with content except
    for small screens where flex-wrap will place them one below the other.
  */
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

/* RJSF compact content (metadata-form) */

.jp-FormGroup-content.jp-FormGroup-contentCompact {
  width: 100%;
}

.jp-FormGroup-contentCompact .form-group {
  display: flex;
  padding: 0.5em 0.2em 0.5em 0;
}

.jp-FormGroup-contentCompact
  .jp-FormGroup-compactTitle
  .jp-FormGroup-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
}

.jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
  padding-bottom: 0.3em;
}

.jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
  width: 100%;
  box-sizing: border-box;
}

.jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
  padding-bottom: 7px;
}

.jp-FormGroup-contentCompact
  .jp-objectFieldWrapper
  .jp-objectFieldWrapper
  .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

.jp-FormGroup-contentCompact ul.error-detail {
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  padding-inline-start: 1em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-SidePanel {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  overflow-y: auto;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
}

.jp-SidePanel-header {
  flex: 0 0 auto;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0;
  padding: 2px;
  text-transform: uppercase;
}

.jp-SidePanel-toolbar {
  flex: 0 0 auto;
}

.jp-SidePanel-content {
  flex: 1 1 auto;
}

.jp-SidePanel-toolbar,
.jp-AccordionPanel-toolbar {
  height: var(--jp-private-toolbar-height);
}

.jp-SidePanel-toolbar.jp-Toolbar-micro {
  display: none;
}

.lm-AccordionPanel .jp-AccordionPanel-title {
  box-sizing: border-box;
  line-height: 25px;
  margin: 0;
  display: flex;
  align-items: center;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  font-size: var(--jp-ui-font-size0);
}

.jp-AccordionPanel-title {
  cursor: pointer;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  text-transform: uppercase;
}

.lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
  user-select: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
  transform: rotate(-90deg);
  margin: auto 0;
  height: 16px;
}

.jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
  transform: rotate(0deg);
}

.lm-AccordionPanel .jp-AccordionPanel-toolbar {
  background: none;
  box-shadow: none;
  border: none;
  margin-left: auto;
}

.lm-AccordionPanel .lm-SplitPanel-handle:hover {
  background: var(--jp-layout-color3);
}

.jp-text-truncated {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent::before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent::after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper:not(.multiple) {
  height: 28px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.jp-mod-styled:not([multiple]) {
  height: 32px;
}

select.jp-mod-styled[multiple] {
  max-height: 200px;
  overflow-y: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
  font-family: var(--jp-ui-font-family);
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-switch-color, var(--jp-border-color1));
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 8;
  overflow-x: hidden;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0;
  margin: 0;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0 6px;
  margin: 0;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent > span {
  padding: 0;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-WindowedPanel-outer {
  position: relative;
  overflow-y: auto;
}

.jp-WindowedPanel-inner {
  position: relative;
}

.jp-WindowedPanel-window {
  position: absolute;
  left: 0;
  right: 0;
  overflow: visible;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

body {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

/* Disable native link decoration styles everywhere outside of dialog boxes */
a {
  text-decoration: unset;
  color: unset;
}

a:hover {
  text-decoration: unset;
  color: unset;
}

/* Accessibility for links inside dialog box text */
.jp-Dialog-content a {
  text-decoration: revert;
  color: var(--jp-content-link-color);
}

.jp-Dialog-content a:hover {
  text-decoration: revert;
}

/* Styles for ui-components */
.jp-Button {
  color: var(--jp-ui-font-color2);
  border-radius: var(--jp-border-radius);
  padding: 0 12px;
  font-size: var(--jp-ui-font-size1);

  /* Copy from blueprint 3 */
  display: inline-flex;
  flex-direction: row;
  border: none;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  text-align: left;
  vertical-align: middle;
  min-height: 30px;
  min-width: 30px;
}

.jp-Button:disabled {
  cursor: not-allowed;
}

.jp-Button:empty {
  padding: 0 !important;
}

.jp-Button.jp-mod-small {
  min-height: 24px;
  min-width: 24px;
  font-size: 12px;
  padding: 0 7px;
}

/* Use our own theme for hover styles */
.jp-Button.jp-mod-minimal:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Button.jp-mod-minimal {
  background: none;
}

.jp-InputGroup {
  display: block;
  position: relative;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border: none;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
  padding-bottom: 0;
  padding-top: 0;
  padding-left: 10px;
  padding-right: 28px;
  position: relative;
  width: 100%;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-size: 14px;
  font-weight: 400;
  height: 30px;
  line-height: 30px;
  outline: none;
  vertical-align: middle;
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input:disabled {
  cursor: not-allowed;
  resize: block;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input:disabled ~ span {
  cursor: not-allowed;
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color2);
}

.jp-InputGroupAction {
  position: absolute;
  bottom: 1px;
  right: 0;
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  cursor: not-allowed;
  resize: block;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
  cursor: not-allowed;
}

/* Use our own theme for hover and option styles */
/* stylelint-disable-next-line selector-max-type */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}

select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-StatusBar-Widget {
  display: flex;
  align-items: center;
  background: var(--jp-layout-color2);
  min-height: var(--jp-statusbar-height);
  justify-content: space-between;
  padding: 0 10px;
}

.jp-StatusBar-Left {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-StatusBar-Middle {
  display: flex;
  align-items: center;
}

.jp-StatusBar-Right {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
}

.jp-StatusBar-Item {
  max-height: var(--jp-statusbar-height);
  margin: 0 2px;
  height: var(--jp-statusbar-height);
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--jp-ui-font-color1);
  padding: 0 6px;
}

.jp-mod-highlighted:hover {
  background-color: var(--jp-layout-color3);
}

.jp-mod-clicked {
  background-color: var(--jp-brand-color1);
}

.jp-mod-clicked:hover {
  background-color: var(--jp-brand-color0);
}

.jp-mod-clicked .jp-StatusBar-TextItem {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-StatusBar-HoverItem {
  box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
}

.jp-StatusBar-TextItem {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  line-height: 24px;
  color: var(--jp-ui-font-color1);
}

.jp-StatusBar-GroupItem {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-Statusbar-ProgressCircle svg {
  display: block;
  margin: 0 auto;
  width: 16px;
  height: 24px;
  align-self: normal;
}

.jp-Statusbar-ProgressCircle path {
  fill: var(--jp-inverse-layout-color3);
}

.jp-Statusbar-ProgressBar-progress-bar {
  height: 10px;
  width: 100px;
  border: solid 0.25px var(--jp-brand-color2);
  border-radius: 3px;
  overflow: hidden;
  align-self: center;
}

.jp-Statusbar-ProgressBar-progress-bar > div {
  background-color: var(--jp-brand-color2);
  background-image: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
  background-size: 40px 40px;
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 14px;
  color: #fff;
  text-align: center;
  animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
}

.jp-Statusbar-ProgressBar-progress-bar p {
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: 10px;
  width: 100px;
}

@keyframes jp-Statusbar-ExecutionTime-progress-bar {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 40px 40px;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty::after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px 24px 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-content.jp-Dialog-content-small {
  max-width: 500px;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
  outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
  outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-checkbox {
  padding-right: 5px;
}

.jp-Dialog-checkbox > input:focus-visible {
  outline: 1px solid var(--jp-input-active-border-color);
  outline-offset: 1px;
}

.jp-Dialog-spacer {
  flex: 1 1 auto;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error {
  padding: 6px;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
  width: auto;
  padding: 10px;
  background: var(--jp-error-color3);
  border: var(--jp-border-width) solid var(--jp-error-color1);
  border-radius: var(--jp-border-radius);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  white-space: pre-wrap;
  word-wrap: break-word;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;
  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;
  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #a0f;
  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;
  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;
  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;
  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;
  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;
  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;
  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;
  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;
  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;
  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ff0;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;
  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;
  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;
  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;
  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;
  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;
  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0;
  padding: 0;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}

.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}

.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}

.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}

.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}

.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}

.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}

.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}

.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}

.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}

.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}

.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}

.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}

.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}

.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}

.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}

.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);

  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

/* stylelint-disable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0;
}

/* stylelint-enable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  table-layout: fixed;
  margin-left: auto;
  margin-bottom: 1em;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}

[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}

.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}

.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}

.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}

.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}

.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}

.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}

.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}

.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: var(--jp-ui-font-size0);
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-cursor-backdrop {
  position: fixed;
  width: 200px;
  height: 200px;
  margin-top: -100px;
  margin-left: -100px;
  will-change: transform;
  z-index: 100;
}

.lm-mod-drag-image {
  will-change: transform;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-lineFormSearch {
  padding: 4px 12px;
  background-color: var(--jp-layout-color2);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
  font-size: var(--jp-ui-font-size1);
}

.jp-lineFormCaption {
  font-size: var(--jp-ui-font-size0);
  line-height: var(--jp-ui-font-size1);
  margin-top: 4px;
  color: var(--jp-ui-font-color0);
}

.jp-baseLineForm {
  border: none;
  border-radius: 0;
  position: absolute;
  background-size: 16px;
  background-repeat: no-repeat;
  background-position: center;
  outline: none;
}

.jp-lineFormButtonContainer {
  top: 4px;
  right: 8px;
  height: 24px;
  padding: 0 12px;
  width: 12px;
}

.jp-lineFormButtonIcon {
  top: 0;
  right: 0;
  background-color: var(--jp-brand-color1);
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 4px 6px;
}

.jp-lineFormButton {
  top: 0;
  right: 0;
  background-color: transparent;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
}

.jp-lineFormWrapper {
  overflow: hidden;
  padding: 0 8px;
  border: 1px solid var(--jp-border-color0);
  background-color: var(--jp-input-active-background);
  height: 22px;
}

.jp-lineFormWrapperFocusWithin {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-lineFormInput {
  background: transparent;
  width: 200px;
  height: 100%;
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  line-height: 28px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
  font-family: var(--jp-ui-font-family);
  padding: 2px 1px;
  resize: none;
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  min-width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);

  --jp-private-document-search-button-height: 20px;
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-button-content svg {
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-input-wrapper:focus-within {
  border-color: var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button::before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 35px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-filter-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-filter-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled:hover {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 100%;
  display: grid;
  justify-content: start;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: stretch;
}

.jp-DocumentSearch-search-filter-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-filter {
  display: flex;
  align-items: center;
  user-select: none;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: auto 2px;
  padding: 1px 4px;
  height: calc(var(--jp-private-document-search-button-height) + 2px);
}

.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-ui-font-color1);

  /* height - 2 * (padding of wrapper) */
  line-height: calc(var(--jp-private-document-search-button-height) - 2px);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.cm-editor {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;

  /* Changed to auto to autogrow */
}

.cm-editor pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

.jp-CodeMirrorEditor {
  cursor: text;
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.cm-editor.jp-mod-readOnly .cm-cursor {
  display: none;
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.cm-searching,
.cm-searching span {
  /* `.cm-searching span`: we need to override syntax highlighting */
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.cm-searching::selection,
.cm-searching span::selection {
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.jp-current-match > .cm-searching,
.jp-current-match > .cm-searching span,
.cm-searching > .jp-current-match,
.cm-searching > .jp-current-match span {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.jp-current-match > .cm-searching::selection,
.cm-searching > .jp-current-match::selection,
.jp-current-match > .cm-searching span::selection {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.cm-trailingspace {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
  background-position: center left;
  background-repeat: repeat-x;
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .cm-ySelectionCaret {
  position: relative;
  border-left: 1px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -1px;
  font-size: 0.95em;
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 101;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .cm-ySelectionInfo {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser .jp-SidePanel-content {
  display: flex;
  flex-direction: column;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  flex-wrap: wrap;
  row-gap: 12px;
  border-bottom: none;
  height: auto;
  margin: 8px 12px 0;
  box-shadow: none;
  padding: 0;
  justify-content: flex-start;
}

.jp-FileBrowser-Panel {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0 2px;
  padding: 0 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0;
  padding-right: 2px;
  align-items: center;
  height: unset;
}

.jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
  width: 40px;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileSize-hidden {
  display: none;
}

.jp-FileBrowser .lm-AccordionPanel > h3:first-child {
  display: none;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-headerItem.jp-id-filesize {
  flex: 0 0 75px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-checkboxWrapper {
  /* Increases hit area of checkbox. */
  padding: 4px;
}

.jp-DirListing-header
  .jp-DirListing-checkboxWrapper
  + .jp-DirListing-headerItem {
  padding-left: 4px;
}

.jp-DirListing-content .jp-DirListing-checkboxWrapper {
  position: relative;
  left: -4px;
  margin: -4px 0 -4px -8px;
}

.jp-DirListing-checkboxWrapper.jp-mod-visible {
  visibility: visible;
}

/* For devices that support hovering, hide checkboxes until hovered, selected...
*/
@media (hover: hover) {
  .jp-DirListing-checkboxWrapper {
    visibility: hidden;
  }

  .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
  .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
    visibility: visible;
  }
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemText:focus {
  outline-width: 2px;
  outline-color: var(--jp-inverse-layout-color1);
  outline-style: solid;
  outline-offset: 1px;
}

.jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
  outline-color: var(--jp-layout-color1);
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-itemFileSize {
  flex: 0 0 90px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon::before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-OutputPrompt {
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-prompt {
  display: table-cell;
  vertical-align: top;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea .jp-RenderedText {
  padding-left: 1ch;
}

/**
 * Prompt overlay.
 */

.jp-OutputArea-promptOverlay {
  position: absolute;
  top: 0;
  width: var(--jp-cell-prompt-width);
  height: 100%;
  opacity: 0.5;
}

.jp-OutputArea-promptOverlay:hover {
  background: var(--jp-layout-color2);
  box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
  cursor: zoom-out;
}

.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
  cursor: zoom-in;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

.jp-TrimmedOutputs pre {
  background: var(--jp-layout-color3);
  font-size: calc(var(--jp-code-font-size) * 1.4);
  text-align: center;
  text-transform: uppercase;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/* Hide empty lines in the output area, for instance due to cleared widgets */
.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0;
  width: 100%;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;

  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;

  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0 0.25em;
  margin: 0 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input::placeholder {
  opacity: 0;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

.jp-Stdin-input:focus::placeholder {
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

@media print {
  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-OutputPrompt {
    display: table-row;
    text-align: left;
  }

  .jp-OutputArea-child .jp-OutputArea-output {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }
}

/* Trimmed outputs warning */
.jp-TrimmedOutputs > a {
  margin: 10px;
  text-decoration: none;
  cursor: pointer;
}

.jp-TrimmedOutputs > a:hover {
  text-decoration: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Table of Contents
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toc-active-width: 4px;
}

.jp-TableOfContents {
  display: flex;
  flex-direction: column;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  height: 100%;
}

.jp-TableOfContents-placeholder {
  text-align: center;
}

.jp-TableOfContents-placeholderContent {
  color: var(--jp-content-font-color2);
  padding: 8px;
}

.jp-TableOfContents-placeholderContent > h3 {
  margin-bottom: var(--jp-content-heading-margin-bottom);
}

.jp-TableOfContents .jp-SidePanel-content {
  overflow-y: auto;
}

.jp-TableOfContents-tree {
  margin: 4px;
}

.jp-TableOfContents ol {
  list-style-type: none;
}

/* stylelint-disable-next-line selector-max-type */
.jp-TableOfContents li > ol {
  /* Align left border with triangle icon center */
  padding-left: 11px;
}

.jp-TableOfContents-content {
  /* left margin for the active heading indicator */
  margin: 0 0 0 var(--jp-private-toc-active-width);
  padding: 0;
  background-color: var(--jp-layout-color1);
}

.jp-tocItem {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-tocItem-heading {
  display: flex;
  cursor: pointer;
}

.jp-tocItem-heading:hover {
  background-color: var(--jp-layout-color2);
}

.jp-tocItem-content {
  display: block;
  padding: 4px 0;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.jp-tocItem-collapser {
  height: 20px;
  margin: 2px 2px 0;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}

.jp-tocItem-collapser:hover {
  background-color: var(--jp-layout-color3);
}

/* Active heading indicator */

.jp-tocItem-heading::before {
  content: ' ';
  background: transparent;
  width: var(--jp-private-toc-active-width);
  height: 24px;
  position: absolute;
  left: 0;
  border-radius: var(--jp-border-radius);
}

.jp-tocItem-heading.jp-tocItem-active::before {
  background-color: var(--jp-brand-color1);
}

.jp-tocItem-heading:hover.jp-tocItem-active::before {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;

  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Hiding collapsers in print mode.

Note: input and output wrappers have "display: block" propery in print mode.
*/

@media print {
  .jp-Collapser {
    display: none;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-InputArea-editor {
  display: table-cell;
  overflow: hidden;
  vertical-align: top;

  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  display: table-cell;
  vertical-align: top;
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-InputArea-editor {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }

  .jp-InputPrompt {
    display: table-row;
    text-align: left;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: table;
  table-layout: fixed;
  width: 100%;
}

.jp-Placeholder-prompt {
  display: table-cell;
  box-sizing: border-box;
}

.jp-Placeholder-content {
  display: table-cell;
  padding: 4px 6px;
  border: 1px solid transparent;
  border-radius: 0;
  background: none;
  box-sizing: border-box;
  cursor: pointer;
}

.jp-Placeholder-contentContainer {
  display: flex;
}

.jp-Placeholder-content:hover,
.jp-InputPlaceholder > .jp-Placeholder-content:hover {
  border-color: var(--jp-layout-color3);
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

.jp-PlaceholderText {
  white-space: nowrap;
  overflow-x: hidden;
  color: var(--jp-inverse-layout-color3);
  font-family: var(--jp-code-font-family);
}

.jp-InputPlaceholder > .jp-Placeholder-content {
  border-color: var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0;
  margin: 0;

  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 24em;
  margin-left: var(--jp-private-cell-scrolling-output-offset);
  resize: vertical;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
  max-height: unset;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
  content: ' ';
  box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
  width: 100%;
  height: 100%;
  position: sticky;
  bottom: 0;
  top: 0;
  margin-top: -50%;
  float: left;
  display: block;
  pointer-events: none;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
  padding-top: 6px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
  left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  display: table-cell;
  width: 100%;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
.jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  font-size: var(--jp-code-font-size);
  position: absolute;
  background-color: transparent;
  background-size: 25px;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: top;
  background-image: var(--jp-icon-caret-down);
  right: 0;
  top: 0;
  bottom: 0;
}

.jp-collapseHeadingButton.jp-mod-collapsed {
  background-image: var(--jp-icon-caret-right);
}

/*
 set the container font size to match that of content
 so that the nested collapse buttons have the right size
*/
.jp-MarkdownCell .jp-InputPrompt {
  font-size: var(--jp-content-font-size1);
}

/*
  Align collapseHeadingButton with cell top header
  The font sizes are identical to the ones in packages/rendermime/style/base.css
*/
.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
  font-size: var(--jp-content-font-size5);
  background-position-y: calc(0.3 * var(--jp-content-font-size5));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
  font-size: var(--jp-content-font-size4);
  background-position-y: calc(0.3 * var(--jp-content-font-size4));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
  font-size: var(--jp-content-font-size3);
  background-position-y: calc(0.3 * var(--jp-content-font-size3));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
  font-size: var(--jp-content-font-size2);
  background-position-y: calc(0.3 * var(--jp-content-font-size2));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
  font-size: var(--jp-content-font-size1);
  background-position-y: top;
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
  font-size: var(--jp-content-font-size0);
  background-position-y: top;
}

/* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
  display: none;
}

.jp-Notebook.jp-mod-showHiddenCellsButton
  :is(.jp-MarkdownCell:hover, .jp-mod-active)
  .jp-collapseHeadingButton {
  display: flex;
}

/* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
  display: flex;
}

.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-showHiddenCellsButton {
  display: none;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Using block instead of flex to allow the use of the break-inside CSS property for
cell outputs.
*/

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
}

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: var(--jp-notebook-toolbar-padding);

  /* disable paint containment from lumino 2.0 default strict CSS containment */
  contain: style size !important;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

.jp-Toolbar-responsive-popup {
  position: absolute;
  height: fit-content;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: var(--jp-notebook-toolbar-padding);
  z-index: 1;
  right: 0;
  top: 0;
}

.jp-Toolbar > .jp-Toolbar-responsive-opener {
  margin-left: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-Notebook-ExecutionIndicator {
  position: relative;
  display: inline-block;
  height: 100%;
  z-index: 9997;
}

.jp-Notebook-ExecutionIndicator-tooltip {
  visibility: hidden;
  height: auto;
  width: max-content;
  width: -moz-max-content;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color1);
  text-align: justify;
  border-radius: 6px;
  padding: 0 5px;
  position: fixed;
  display: table;
}

.jp-Notebook-ExecutionIndicator-tooltip.up {
  transform: translateX(-50%) translateY(-100%) translateY(-32px);
}

.jp-Notebook-ExecutionIndicator-tooltip.down {
  transform: translateX(calc(-100% + 16px)) translateY(5px);
}

.jp-Notebook-ExecutionIndicator-tooltip.hidden {
  display: none;
}

.jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
  visibility: visible;
}

.jp-Notebook-ExecutionIndicator span {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  color: var(--jp-ui-font-color1);
  line-height: 24px;
  display: block;
}

.jp-Notebook-ExecutionIndicator-progress-bar {
  display: flex;
  justify-content: center;
  height: 100%;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * Execution indicator
 */
.jp-tocItem-content::after {
  content: '';

  /* Must be identical to form a circle */
  width: 12px;
  height: 12px;
  background: none;
  border: none;
  position: absolute;
  right: 0;
}

.jp-tocItem-content[data-running='0']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background: none;
}

.jp-tocItem-content[data-running='1']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background-color: var(--jp-inverse-layout-color3);
}

.jp-tocItem-content[data-running='0'],
.jp-tocItem-content[data-running='1'] {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Notebook-footer {
  height: 27px;
  margin-left: calc(
    var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
      var(--jp-cell-padding)
  );
  width: calc(
    100% -
      (
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
          var(--jp-cell-padding) + var(--jp-cell-padding)
      )
  );
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  color: var(--jp-ui-font-color3);
  margin-top: 6px;
  background: none;
  cursor: pointer;
}

.jp-Notebook-footer:focus {
  border-color: var(--jp-cell-editor-active-border-color);
}

/* For devices that support hovering, hide footer until hover */
@media (hover: hover) {
  .jp-Notebook-footer {
    opacity: 0;
  }

  .jp-Notebook-footer:focus,
  .jp-Notebook-footer:hover {
    opacity: 1;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-side-by-side-output-size: 1fr;
  --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

/* stylelint-disable selector-max-class */

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}

.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-ActiveCellTool {
  padding: 12px 0;
  display: flex;
}

.jp-ActiveCellTool-Content {
  flex: 1 1 auto;
}

.jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
  background: var(--jp-cell-editor-background);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  min-height: 29px;
}

.jp-ActiveCellTool .jp-InputPrompt {
  min-width: calc(var(--jp-cell-prompt-width) * 0.75);
}

.jp-ActiveCellTool-CellContent > pre {
  padding: 5px 4px;
  margin: 0;
  white-space: normal;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label,
.jp-NumberSetter label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0;
}

.jp-NumberSetter input {
  width: 100%;
  margin-top: 4px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Side-by-side Mode (.jp-mod-sideBySide)
|----------------------------------------------------------------------------*/
.jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
  margin-top: 3em;
  margin-bottom: 3em;
  margin-left: 5%;
  margin-right: 5%;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-output-size)
    );
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'header header header'
    'input handle output'
    'footer footer footer';
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-resized-cell)
    );
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
  grid-area: header;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
  grid-area: input;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
  /* overwrite the default margin (no vertical separation needed in side by side move */
  margin-top: 0;
  grid-area: output;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
  grid-area: footer;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
  grid-area: handle;
  user-select: none;
  display: block;
  height: 100%;
  cursor: ew-resize;
  padding: 0 var(--jp-cell-padding);
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
  content: '';
  display: block;
  background: var(--jp-border-color2);
  height: 100%;
  width: 5px;
}

.jp-mod-sideBySide.jp-Notebook
  .jp-CodeCell.jp-mod-resizedCell
  .jp-CellResizeHandle::after {
  background: var(--jp-border-color0);
}

.jp-CellResizeHandle {
  display: none;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
    0 1px 1px 0 var(--jp-shadow-penumbra-color),
    0 1px 3px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
    0 2px 2px 0 var(--jp-shadow-penumbra-color),
    0 1px 5px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
    0 4px 5px 0 var(--jp-shadow-penumbra-color),
    0 1px 10px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
    0 6px 10px 0 var(--jp-shadow-penumbra-color),
    0 1px 18px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
    0 8px 10px 1px var(--jp-shadow-penumbra-color),
    0 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
    0 12px 17px 2px var(--jp-shadow-penumbra-color),
    0 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
    0 16px 24px 2px var(--jp-shadow-penumbra-color),
    0 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
    0 20px 31px 3px var(--jp-shadow-penumbra-color),
    0 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
    0 24px 38px 3px var(--jp-shadow-penumbra-color),
    0 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-inverse-border-color: var(--md-grey-600);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;
  --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
    helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;
  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);
  --jp-content-link-color: var(--md-blue-900);
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);
  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);
  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);
  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);
  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;
  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);
  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;

  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-inverse-border-color);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #a2f;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #a2f;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /*
    RTC user specific colors.
    These colors are used for the cursor, username in the editor,
    and the icon of the user.
  */

  --jp-collaborator-color1: #ffad8e;
  --jp-collaborator-color2: #dac83d;
  --jp-collaborator-color3: #72dd76;
  --jp-collaborator-color4: #00e4d0;
  --jp-collaborator-color5: #45d4ff;
  --jp-collaborator-color6: #e2b1ff;
  --jp-collaborator-color7: #ff9de6;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);

  /* Button colors */
  --jp-accept-color-normal: var(--md-blue-700);
  --jp-accept-color-hover: var(--md-blue-800);
  --jp-accept-color-active: var(--md-blue-900);
  --jp-warn-color-normal: var(--md-red-700);
  --jp-warn-color-hover: var(--md-red-800);
  --jp-warn-color-active: var(--md-red-900);
  --jp-reject-color-normal: var(--md-grey-600);
  --jp-reject-color-hover: var(--md-grey-700);
  --jp-reject-color-active: var(--md-grey-800);

  /* File or activity icons and switch semantic variables */
  --jp-jupyter-icon-color: #f37626;
  --jp-notebook-icon-color: #f37626;
  --jp-json-icon-color: var(--md-orange-700);
  --jp-console-icon-background-color: var(--md-blue-700);
  --jp-console-icon-color: white;
  --jp-terminal-icon-background-color: var(--md-grey-800);
  --jp-terminal-icon-color: var(--md-grey-200);
  --jp-text-editor-icon-color: var(--md-grey-700);
  --jp-inspector-icon-color: var(--md-grey-700);
  --jp-switch-color: var(--md-grey-400);
  --jp-switch-true-position-color: var(--md-orange-900);
}
</style>
<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.cm-editor.cm-s-jupyter .highlight pre {
/* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
  padding: var(--jp-code-padding) 4px;
  margin: 0;

  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  color: inherit;

}

.jp-OutputArea-output pre {
  line-height: inherit;
  font-family: inherit;
}

.jp-RenderedText pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@page {
    margin: 0.5in; /* Margin for each printed piece of paper */
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}
</style>
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
<!-- End of mathjax configuration --><script type="module">
  document.addEventListener("DOMContentLoaded", async () => {
    const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
    // do not load mermaidjs if not needed
    if (!diagrams.length) {
      return;
    }
    const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.6.0/mermaid.esm.min.mjs")).default;
    const parser = new DOMParser();

    mermaid.initialize({
      maxTextSize: 100000,
      startOnLoad: false,
      fontFamily: window
        .getComputedStyle(document.body)
        .getPropertyValue("--jp-ui-font-family"),
      theme: document.querySelector("body[data-jp-theme-light='true']")
        ? "default"
        : "dark",
    });

    let _nextMermaidId = 0;

    function makeMermaidImage(svg) {
      const img = document.createElement("img");
      const doc = parser.parseFromString(svg, "image/svg+xml");
      const svgEl = doc.querySelector("svg");
      const { maxWidth } = svgEl?.style || {};
      const firstTitle = doc.querySelector("title");
      const firstDesc = doc.querySelector("desc");

      img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
      if (maxWidth) {
        img.width = parseInt(maxWidth);
      }
      if (firstTitle) {
        img.setAttribute("alt", firstTitle.textContent);
      }
      if (firstDesc) {
        const caption = document.createElement("figcaption");
        caption.className = "sr-only";
        caption.textContent = firstDesc.textContent;
        return [img, caption];
      }
      return [img];
    }

    async function makeMermaidError(text) {
      let errorMessage = "";
      try {
        await mermaid.parse(text);
      } catch (err) {
        errorMessage = `${err}`;
      }

      const result = document.createElement("details");
      result.className = 'jp-RenderedMermaid-Details';
      const summary = document.createElement("summary");
      summary.className = 'jp-RenderedMermaid-Summary';
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.innerText = text;
      pre.appendChild(code);
      summary.appendChild(pre);
      result.appendChild(summary);

      const warning = document.createElement("pre");
      warning.innerText = errorMessage;
      result.appendChild(warning);
      return [result];
    }

    async function renderOneMarmaid(src) {
      const id = `jp-mermaid-${_nextMermaidId++}`;
      const parent = src.parentNode;
      let raw = src.textContent.trim();
      const el = document.createElement("div");
      el.style.visibility = "hidden";
      document.body.appendChild(el);
      let results = null;
      let output = null;
      try {
        const { svg } = await mermaid.render(id, raw, el);
        results = makeMermaidImage(svg);
        output = document.createElement("figure");
        results.map(output.appendChild, output);
      } catch (err) {
        parent.classList.add("jp-mod-warning");
        results = await makeMermaidError(raw);
        output = results[0];
      } finally {
        el.remove();
      }
      parent.classList.add("jp-RenderedMermaid");
      parent.appendChild(output);
    }

    void Promise.all([...diagrams].map(renderOneMarmaid));
  });
</script>
<style>
  .jp-Mermaid:not(.jp-RenderedMermaid) {
    display: none;
  }

  .jp-RenderedMermaid {
    overflow: auto;
    display: flex;
  }

  .jp-RenderedMermaid.jp-mod-warning {
    width: auto;
    padding: 0.5em;
    margin-top: 0.5em;
    border: var(--jp-border-width) solid var(--jp-warn-color2);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .jp-RenderedMermaid figure {
    margin: 0;
    overflow: auto;
    max-width: 100%;
  }

  .jp-RenderedMermaid img {
    max-width: 100%;
  }

  .jp-RenderedMermaid-Details > pre {
    margin-top: 1em;
  }

  .jp-RenderedMermaid-Summary {
    color: var(--jp-warn-color2);
  }

  .jp-RenderedMermaid:not(.jp-mod-warning) pre {
    display: none;
  }

  .jp-RenderedMermaid-Summary > pre {
    display: inline-block;
    white-space: normal;
  }
</style>
<!-- End of mermaid configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="12">Team 2: Fat/Water Separation</font></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="6">Authors:</font><br/>
<font size="4">Amirhossein Sabour</font><br/>
<font size="4">Clare Thornton</font><br/>
<font size="4">Ahila Ramesh Rajamani</font><br/>
<font size="4">Esteban Pondicq Cassou</font></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="6">Libraries</font></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="6">Generating K-Space Data</font></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<ul>
<li><p>A simple case is assumed herein; data is obtained from imaging a slice of the sample containing fat and water <em>only</em>.</p>
</li>
<li><p>EPI data acquisition was two-fold in this experiment; (1) traversing forward through K-Space, and (2) traversing backwards through K-Space.</p>
<ul>
<li>i.e. From kx = 0 to 256 and ky = 0 to 256 in the forward traversal experiment, and kx = -256 to 0 and ky = -256 to 0 in the backwards traversal experiment.</li>
</ul>
</li>
<li><p>It was assumed that imaging was performed in the water's rotating frame of reference; thus, the water in the sample appears stationary, while some delay is induced by the fat.</p>
</li>
</ul>
<p>Variables:</p>
<ul>
<li><code>image_size</code> - size of the image in pixels.</li>
<li><code>fat_scalar</code> - used to control the size of the fat component of the signal.</li>
<li><code>water_scalar</code> - used to control the size of the water component of the signal.</li>
<li><code>scaling_factor</code> - used to scale the fat and water components of the signal based on selection of <code>fat_scalar</code> and <code>water_scalar</code>.</li>
<li><code>const</code> - a constant with units <code>1/s</code> dependent on the gyromagnetic ratio of protons in water or fat, and the magnetic field strength. In this example, they are assumed to be the same.</li>
<li><code>t</code> - a division of time with units <code>s</code> dependent on imaging speed.</li>
<li><code>phi</code> - phase associated with the fat component of the signal in water's rotating frame of reference.</li>
</ul>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">image_size</span> <span class="o">=</span> <span class="mi">256</span>
<span class="n">fat_scalar</span> <span class="o">=</span> <span class="mi">2</span>
<span class="n">water_scalar</span> <span class="o">=</span> <span class="mi">4</span>
<span class="n">scaling_factor</span> <span class="o">=</span> <span class="mi">1</span><span class="o">/</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">square</span><span class="p">(</span><span class="n">image_size</span><span class="o">/</span><span class="n">fat_scalar</span><span class="p">)</span><span class="o">/</span><span class="n">np</span><span class="o">.</span><span class="n">square</span><span class="p">(</span><span class="n">image_size</span><span class="o">/</span><span class="n">water_scalar</span><span class="p">))</span>
<span class="n">const</span> <span class="o">=</span> <span class="mf">1e6</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">create_kspace_data</span><span class="p">(</span><span class="nb">range</span><span class="p">:</span> <span class="nb">range</span><span class="p">,</span> <span class="n">tx</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">:</span>
    <span class="n">water_kspace</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="n">image_size</span><span class="p">,</span> <span class="n">image_size</span><span class="p">),</span> <span class="n">dtype</span> <span class="o">=</span> <span class="nb">complex</span><span class="p">)</span>
    <span class="n">fat_kspace</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="n">image_size</span><span class="p">,</span> <span class="n">image_size</span><span class="p">),</span> <span class="n">dtype</span> <span class="o">=</span> <span class="nb">complex</span><span class="p">)</span>
    <span class="n">phi</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="n">image_size</span><span class="p">,</span> <span class="n">image_size</span><span class="p">))</span>
    <span class="n">t</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">ky</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">kx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">:</span>
            <span class="n">phi_idx</span> <span class="o">=</span> <span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">t</span><span class="o">*</span><span class="n">const</span>
            <span class="n">fat_complex_exp</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="mi">1</span><span class="n">j</span><span class="o">*</span><span class="n">phi_idx</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">complex</span><span class="p">)</span>
            <span class="n">water_kspace</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span><span class="n">kx</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sinc</span><span class="p">((</span><span class="n">kx</span><span class="o">-</span><span class="mi">128</span><span class="p">)</span><span class="o">/</span><span class="n">water_scalar</span><span class="p">)</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sinc</span><span class="p">((</span><span class="n">ky</span><span class="o">-</span><span class="mi">128</span><span class="p">)</span><span class="o">/</span><span class="n">water_scalar</span><span class="p">)</span>
            <span class="n">fat_kspace</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span><span class="n">kx</span><span class="p">]</span><span class="o">=</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">sinc</span><span class="p">((</span><span class="n">kx</span><span class="o">-</span><span class="mi">128</span><span class="p">)</span><span class="o">/</span><span class="n">fat_scalar</span><span class="p">)</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sinc</span><span class="p">((</span><span class="n">ky</span><span class="o">-</span><span class="mi">128</span><span class="p">)</span><span class="o">/</span><span class="n">fat_scalar</span><span class="p">)</span> <span class="o">-</span> <span class="n">scaling_factor</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sinc</span><span class="p">((</span><span class="n">kx</span><span class="o">-</span><span class="mi">128</span><span class="p">)</span><span class="o">/</span><span class="n">water_scalar</span><span class="p">)</span><span class="o">*</span><span class="n">np</span><span class="o">.</span><span class="n">sinc</span><span class="p">((</span><span class="n">ky</span><span class="o">-</span><span class="mi">128</span><span class="p">)</span><span class="o">/</span><span class="n">water_scalar</span><span class="p">))</span><span class="o">*</span><span class="n">fat_complex_exp</span>
            <span class="n">phi</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span><span class="n">kx</span><span class="p">]</span> <span class="o">=</span> <span class="n">phi_idx</span>
            <span class="n">t</span> <span class="o">+=</span> <span class="n">tx</span>
    
    <span class="k">return</span> <span class="n">fat_kspace</span><span class="p">,</span> <span class="n">water_kspace</span><span class="p">,</span> <span class="n">phi</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="6">Plotting Corrupted Image Data</font></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<ul>
<li><p>The sample has been imaged in the water's rotating frame of reference, hence the introduction of some 2D delay to the fat component of the signal which needs to be resolved.</p>
</li>
<li><p>The water component of the signal appears stationary due to imaging in the water's rotating frame of reference.</p>
</li>
<li><p>This delay is reversed in each of the two datasets acquired through experimentation due to traversal of K-Space in opposite directions.</p>
</li>
<li><p>Given that the magnetic properties of fat and water are known, we may perform fat/water separation by solving a system of equations at each point in K-Space.</p>
</li>
</ul>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">inverse_fft</span><span class="p">(</span><span class="n">kspace</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">fft</span><span class="o">.</span><span class="n">ifftshift</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">fft</span><span class="o">.</span><span class="n">ifft2</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">fft</span><span class="o">.</span><span class="n">fftshift</span><span class="p">(</span><span class="n">kspace</span><span class="p">)))</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">plot_fat_water</span><span class="p">(</span><span class="n">fat_img</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">,</span> <span class="n">water_img</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">,</span> <span class="n">total_img</span><span class="p">:</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">,</span> <span class="n">title</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">:</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">fat_img</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">"Fat Component"</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">water_img</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">"Water Component"</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">total_img</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">"Total Image"</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">suptitle</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">colorbar</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">fat_kspace1</span><span class="p">,</span> <span class="n">water_kspace1</span><span class="p">,</span> <span class="n">phi1</span> <span class="o">=</span> <span class="n">create_kspace_data</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="n">image_size</span><span class="p">),</span> <span class="mf">1e-6</span><span class="p">)</span>
<span class="n">fat_kspace2</span><span class="p">,</span> <span class="n">water_kspace2</span><span class="p">,</span> <span class="n">phi2</span> <span class="o">=</span> <span class="n">create_kspace_data</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="n">image_size</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">),</span> <span class="mf">1e-6</span><span class="p">)</span>

<span class="n">kspace1</span> <span class="o">=</span> <span class="n">fat_kspace1</span> <span class="o">+</span> <span class="n">water_kspace1</span>
<span class="n">kspace2</span> <span class="o">=</span> <span class="n">fat_kspace2</span> <span class="o">+</span> <span class="n">water_kspace2</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">plot_fat_water</span><span class="p">(</span><span class="n">inverse_fft</span><span class="p">(</span><span class="n">fat_kspace1</span><span class="p">),</span> <span class="n">inverse_fft</span><span class="p">(</span><span class="n">water_kspace1</span><span class="p">),</span> <span class="n">inverse_fft</span><span class="p">(</span><span class="n">kspace1</span><span class="p">),</span> <span class="s1">'K-Space 1: Forward Traversal'</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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hMEZERERkRVhcEZERERkRRicEREREVkRBmdEREREVoTBGREREZEVYXBGREREZEUYnBERERFZEQZnRERERFaEwRkRERGRFWFwRkRERGRFGJwRERERWREGZ0RERERWhMEZERERkRVhcEZERERkRRicEREREVkRBmdEREREVoTBGREREZEVYXBGREREZEUYnBERERFZEQZnRERERFaEwRkRERGRFWFwRkRERGRFGJwRERERWRE7S2eAiIiIrE9ubi7y8/PNci0HBwc4OTmZ5VrVAYMzIiIiUsjNzYV/YxekXdeY5Xre3t44d+4cAzQDMTgjIiIihfz8fKRd1+BCqh9ca5nWAyr7jhaNg84jPz+fwZmBGJwRERGRXi61JLjUkky6hhamnV8dMTgjIiIivTRCC40w/RpkHI7WJCIiIrIirDkjIiIivbQQ0MK0qjNTz6+OGJwRERGRXlpoYWqjpOlXqH7YrElERERkRVhzRkRERHpphIBGmNYsaer51RGDMyIiItKLfc4sg82aRERERFaENWdERESklxYCGtacVToGZ0RERKQXmzUtg8EZERER6cUBAZbBPmdEREREVoQ1Z0RERKSX9n+bqdcg4zA4IyIiIr00ZhgQYOr51RGbNYmIiIisCGvOiIiISC+NKNpMvQYZh8EZERER6cU+Z5bBZk0iIiIiK8KaMyIiItJLCwkaSCZfg4zD4IyIiIj00oqizdRrkHHYrElERERkRVhzRkRERHppzNCsaer51RGDMyIiItKLwZllMDgjIiIivbRCglaYOCDAxPOrI/Y5IyIiIrIirDkjIiIivdisaRkMzoiIiEgvDVTQmNjIpjFTXqoTNmsSERERWRHWnBEREZFewgwDAgQHBBiNwRkRERHpxT5nlsFmTSIiIiIrwpozIiIi0ksjVNAIEwcEcG1NozE4IyIiIr20kKA1sZFNC0ZnxmJwRkRERHqxz5llsM8ZERERkRVhzRkRERHpZZ4+Z2zWNBaDMyIiItKrqM+ZiQufs1nTaGzWJCIiIrIirDkjIiIivbRmWFuTozWNx+CMiIiI9GKfM8tgsyYRERGRFWHNGREREemlhYqT0FoAgzMiIiLSSyMkaISJk9CaeH51xGZNIiIiIivCmjMiIiLSS2OG0ZoaNmsajTVnREREpJdWqMyyGWvRokXw8/ODk5MTgoODcfDgwXLTr1mz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2hX//PMPsrKyKnz/NWvWoHPnzqhdu7b8/G/evImwsDBoNBrs3btXkb5///6oV69ehdc1prxrNBps3boVEREReOSRR+T99evXx3/+8x/s27dPvp7O8OHDFeUgODgYQggMHz5c3qdWq9G2bdtSZR0AIiIi0KBBA/l1+/btERwcjE2bNgEArl27hqNHj2Lo0KGK2sHHH38czzzzjJyuuDfeeEPxunPnzrh165ac9++//x5arRYvv/yy4ll7e3sjICCg1MhcFxcXvPLKK/JrBwcHtG/fXu/9EFHVVq2aNdu3b693QMD9+/cRHx+PpKQkXLlyRdFnxZAPPH1cXV0BAHfu3DEo/YULF+Dj41Pqw03XbFoyGCnZVOrm5gYA8PX11bv/9u3biv0+Pj6oWbOmYt9jjz0GoKifTocOHXDhwgUEBARApVLG8IbmSReo6d777NmzEELggw8+wAcffAB9rl+/rvgQreiatkaSJISGhmLv3r3QarXYv38/PD090aRJEwBFwdnChQsBQA7Sigdn+/fvx5QpU5CcnFyqf1NWVpb88y7LmTNn8Mcff5QZcF2/fl3xuuTo5rIYU95v3LiBe/fuoWnTpqWONW/eHFqtFpcuXUKLFi3k/caUd31lIyAgoNS+xx57DN9++y2Af8tyWXn6+eefkZOTo/idKa9surq64syZMxBC6H1vAHJTv07Dhg0VAajumn/88Yfe84kqA5s1LaNaBWdlGTVqFJKSkhAbG4uQkBC4ublBkiRERkYqOkkbo0mTJrCzs5M76ZubWq02ar8oMajgYajovXXP8p133kF4eLjetLogxdBr2qJOnTrhxx9/xLFjx+T+ZjqhoaFyP8N9+/bBx8dHrl36+++/0b17dzRr1gyffPIJfH194eDggE2bNmHevHkGlVWtVotnnnkGEyZM0HtcF6DrFK+pK0+zZs0AAMeOHXsoUzwYU94rq2wYUt4lScLmzZv1pnVxcTHqekSWwLU1LYPBGYC1a9diyJAhmDt3rrwvNzcXmZmZinQlv9WWp0aNGnj66aexc+dOXLp0qdQ3/JIaN26M7du3486dO4ras1OnTsnHzenq1aulagL++usvAJCbSxs3bow//vgDWq1WUXv2oHnSBRn29vYICwszJfsKxvxcrEHx+c7279+vGN0YFBQER0dH7N69GykpKejdu7d87Mcff0ReXh42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gCRJiI2NxYwZM7BhwwYcO3YMgwcPho+PDyIiIgAAzZs3R8+ePTFixAgcPHgQ+/fvR0xMDCIjI+Hj4wMA+M9//gMHBwcMHz4cJ06cwOrVq/Hpp59i7Nixcl4+/PBDbN26Ff/88w+OHDmCV155BRcuXMBrr71m1DNgnzMiIiLSzwIrBAwYMAA3btxAXFwc0tLS0KZNG2zZskXufH/x4kWoVP/WLYWGhmLVqlWYPHkyJk2ahICAAKxbtw4tW7aU00yYMAE5OTkYOXIkMjMz0alTJ2zZskUxQezKlSsRExOD7t27Q6VSoX///pg/f7583M3NDVu3bkV0dDSCgoJQt25dxMXFKeZCu337NkaMGIG0tDTUrl0bQUFBOHDgAAIDA416BpznjIiIiBR085w99eRE2KlNnOdMk4tdR+INnueM2KxJREREZFXYrElERER6Gduhv6xrkHEYnBEREZF+Amboc2aWnFQrbNYkIiIisiKsOSMiIiL9LDBakxicERERUVm0ACQzXIOMwuCMiIiI9OKAAMtgnzMiIiIiK8KaMyIiItKPfc4sgsEZERER6cfgzCLYrElERERkRVhzRkRERPqx5swiGJwRERGRfpxKwyLYrElERERkRVhzRkRERHpxnjPLYHBGRERE+rHPmUWwWZOIiIjIirDmjIiIiPTTCkAyseZLy5ozYzE4IyIiIv3YrGkRDM6IiIioDGYIzsDgzFjsc0ZERERkRVhzRkRERPqxWdMiGJwRERGRfloBk5slOSDAaGzWJCIiIrIirDkjIiIi/YS2aDP1GmQUBmdERESkH/ucWQSbNYmIiIisCGvOiIiISD8OCLAIBmdERESkH5s1LYLNmkRERERWhDVnREREpJ+AGWrOzJKTaoXBGREREenHZk2LYHBGRERE+mm1AEycp0zLec6MxT5nRERERFaENWdERESkH5s1LYLBGREREenH4Mwi2KxJREREZEVYc0ZERET6cYUAi2BwRkRERHoJoYUQpo22NPX86ojNmkRERERWhDVnREREpJ8QpjdLckCA0RicERERkX7CDH3OGJwZjc2aRERERFaENWdERESkn1YLSCZ26OeAAKMxOCMiIiL92KxpEQzOiIiISC+h1UKYWHPGqTSMxz5nRERERFaENWdERESkH5s1LYLBGREREemnFYDE4KyysVmTiIiIyIqw5oyIiIj0EwKAqVNpsObMWAzOiIiISC+hFRAmNmsKBmdGY7MmERERkRVhzRkRERHpJ7QwvVmT85wZi8EZERER6cVmTctgsyYRERGRFWHNGREREelVKPJMbpYsRIGZclN9MDgjIiIiBQcHB3h7e2Nf2iazXM/b2xsODg5muVZ1IAk2BhMREVEJubm5yM/PN8u1HBwc4OTkZJZrVQcMzoiIiIisCAcEEBEREVkRBmdEREREVoTBGREREZEVYXBGREREZEUYnBERERFZEQZnRERERFaEwRkRERGRFfn/2I2xlH3NuUEAAAAASUVORK5CYII="/>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">plot_fat_water</span><span class="p">(</span><span class="n">inverse_fft</span><span class="p">(</span><span class="n">fat_kspace2</span><span class="p">),</span> <span class="n">inverse_fft</span><span class="p">(</span><span class="n">water_kspace2</span><span class="p">),</span> <span class="n">inverse_fft</span><span class="p">(</span><span class="n">kspace2</span><span class="p">),</span> <span class="s1">'K-Space 2: Backwards Traversal'</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmcAAAG1CAYAAAC8rFOoAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAABz1ElEQVR4nO3deVwU9f8H8NfuIocgICKXopASipoUKoIHpiReFWYmZalo0iGmaZqWR6bJL03FKzErJNNvHplXhiLeihemeaRZiVfihRyiXLuf3x/ExMhyrLuyC7yej8c8aj/zmZnPDCO893MqhBACRERERGQSlMYuABERERH9h8EZERERkQlhcEZERERkQhicEREREZkQBmdEREREJoTBGREREZEJYXBGREREZEIYnBERERGZEAZnRERERCaEwRkRPRaffPIJFAoFbt++beyi6GT58uVQKBRISUkxdlGqrZSUFCgUCixfvtzYRSEySQzOqFIV/eE7duyYLD0jIwPt2rWDpaUl4uPjSz3+1KlTePnll9G4cWNYWlqiQYMGeO6557Bw4cLHXfTHbv369RgwYACeeOIJ1K5dG97e3hg7dizS09P1Oq9CoZBt1tbW8PHxwYwZM3D//n3DFJ5kit7z8jYPDw9jF5WITJCZsQtAlJmZie7du+O3337DTz/9hB49emjNd/DgQTz77LNo1KgRhg8fDhcXF1y5cgWHDh3C/PnzMXLkyEouuWFFRETAzc0Nr7/+Oho1aoRTp05h0aJF2Lp1K44fPw4rK6tHPvdzzz2HQYMGAQDu3buHffv2YfLkyTh58iTWrl1rqFugf3Xu3BkrVqyQpb355pto164dIiIipDQbG5vKLhoRVQEMzsiosrKyEBISghMnTmD9+vXo2bNnqXk/++wz2NnZ4ejRo7C3t5ftu3nz5mMu6eO3bt06dOnSRZbm5+eHwYMHY+XKlXjzzTcf+dxPPvkkXn/9denz22+/jby8PKxfvx45OTmwtLR85HNXNRqNBnl5eY/1np944gk88cQTsrS3334bTzzxhOzn8LCCggJoNBqYm5s/trLpqjKeFxHJsVmTjObevXvo0aMHjh8/jh9//BG9e/cuM/9ff/2FFi1alAjMAMDJyUn2WaFQIDIyEitXroS3tzcsLS3h5+eHvXv3yvJdunQJ7777Lry9vWFlZYV69eqhf//+Wvsb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axc6dOgAtVqNc+fOYc2aNdi2bZtUy6dNjx498Pfff2P8+PHYv38/9u/fL+1zdnbGc889J33WdSqNP/74A99//z0A4P79+zh06BDi4uLQtGlTvPHGGwCAZs2aoUmTJvjggw9w7do12Nra4scff8Tdu3dLnG/BggXo2LEjnnnmGURERMDT0xMpKSn4+eefceLEiRL5lUolvv/+e4SGhuKVV17B1q1bpc7oQGEg9n//93+ws7NDq1atABQ2o3l7e+P8+fMYMmSI7Hy9e/fG3Llz0aNHD7z22mu4efMmFi9ejKZNm+K3334r93kAwPjx47FixQr06NEDo0aNkqbSaNy4sewccXFx+PLLL9G3b180adIEWVlZWLZsGWxtbdGrV68KXUtXffr0wfr169G3b1/07t0bFy9eRExMDHx8fKSazuIGDBiAhQsXYurUqWjVqhWaN28u26/vuwkUrnCQlpaGrl27omHDhrh06RIWLlwIX19f6Xp9+vTBp59+ivDwcAQGBuLUqVNYuXJliQl5iagcRhkjSjVW0VQa2qYl+OKLLwQA0adPH5Gfn19i/y+//CKGDh0qmjVrJmxsbIS5ublo2rSpGDlypLhx44YsLwAxYsQI8f333wsvLy9hYWEhnn76abFr1y5Zvrt374rw8HDh6OgobGxsREhIiDh37pxo3LixbNoDIYS4c+eOiIyMFA0aNBDm5uaiYcOGYvDgweL27dtSnry8PPH555+LFi1aCAsLC1G3bl3h5+cnpk2bJjIyMsp8NihlygsAIigoSJZXn6k0VCqVaNiwoYiIiCjx3M6ePSuCg4OFjY2NcHR0FMOHDxcnT57UOu3B6dOnRd++fYW9vb2wtLQU3t7eYvLkydL+4lNpFLl//74ICgoSNjY24tChQ1L6zz//LACInj17yq7x5ptvCgDim2++KXFf33zzjfSzbdasmYiNjZWu+fD9jxgxQuuz+e2330RQUJCwtLQUDRo0ENOnTxfffPON7NkeP35cvPrqq6JRo0bCwsJCODk5iT59+simaamI0qbSmD17dom8Go1GzJw5UzRu3Fh6d7ds2SIGDx4sGjdurDW/u7u7ACBmzJih9foVfTdLe17r1q0T3bt3F05OTsLc3Fw0atRIvPXWW+L69etSnpycHDF27Fjh6uoqrKysRIcOHURSUpIICgqSvcOcSoOobAohtLRDEFVxCoUCI0aMwKJFi4xdFCIiIp2wzxkRERGRCWFwRkRERGRCGJwRERERmRCO1qRqiV0piYioqmLNGREREZEJYXBGREREZEIYnBERERGZEAZnRERERCaEwRkRERGRCWFwRkRERGRCGJwRERERmRAGZ0REREQmhMEZERERkQlhcEZERERkQhicEREREZkQBmdEREREJoTBGREREZEJYXBGREREZEIYnBERERGZEAZnRERERCaEwRkRERGRCWFwRkRERGRCGJwRERERmRAGZ0REREQmhMEZERERkQlhcEZERERkQhicEREREZkQBmdEREREJoTBGREREZEJYXBGREREZEIYnBERERGZEDNjF4CIiIhMT05ODvLy8gxyLnNzc1haWhrkXDUBgzMiIiKSycnJgWdjG6TeVBvkfC4uLrh48SIDtApicEZEREQyeXl5SL2pxqVkD9jW0a8HVGaWBo39UpCXl8fgrIIYnBEREZFWNnUUsKmj0OscGuh3fE3E4IyIiIi0UgsN1EL/c5BuOFqTiIiIyISw5oyIiIi00kBAA/2qzvQ9viZicEZERERaaaCBvo2S+p+h5mGzJhEREZEJYc0ZERERaaUWAmqhX7OkvsfXRAzOiIiISCv2OTMONmsSERERmRDWnBEREZFWGgioWXNW6RicERERkVZs1jQOBmdERESkFQcEGAf7nBERERGZENacERERkVaafzd9z0G6YXBGREREWqkNMCBA3+NrIjZrEhEREZkQ1pwRERGRVmpRuOl7DtINgzMiIiLSin3OjIPNmkREREQmhDVnREREpJUGCqih0PscpBsGZ0RERKSVRhRu+p6DdMNmTSIiIiITwpozIiIi0kptgGZNfY+viRicERERkVYMzoyDwRkRERFppREKaISeAwL0PL4mYp8zIiIiIhPCmjMiIiLSis2axsHgjIiIiLRSQwm1no1sagOVpSZhsyYRERGRCWHNGREREWklDDAgQHBAgM4YnBEREZFW7HNmHGzWJCIiIjIhrDkjIiIirdRCCbXQc0AA19bUGYMzIiIi0koDBTR6NrJpwOhMVwzOiIiISCv2OTMO9jkjIiIiMiGsOSMiIiKtDNPnjM2aumJwRkRERFoV9jnTc+FzNmvqjM2aRERERCaENWdERESklcYAa2tytKbuGJwRERGRVuxzZhxs1iQiIiIyIaw5IyIi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"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="6">Performing the Fat/Water Separation</font></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>Formulation:</p>
<ul>
<li><p>$x_r$ and $x_i$ - real and imaginary components of K-Space 1</p>
</li>
<li><p>$y_r$ and $y_i$ - real and imaginary components of K-Space 2</p>
</li>
<li><p>$w_r$ and $w_i$ - real and imaginary components of the water component of the signal</p>
</li>
<li><p>$f_r$ and $f_i$ - real and imaginary components of the fat component of the signal</p>
</li>
<li><p>$\phi_1$ - phase associated with the fat in the water's rotating frame of reference in K-Space 1</p>
</li>
<li><p>$\phi_2$ - phase associated with the fat in the water's rotating frame of reference in K-Space 2</p>
</li>
</ul>
<p><br/></p>
<p>The equations for each K-Space may be written as:</p>
<p><br/></p>
<p>$$
  KSpace_1: x_r + jx_i = w_r + jw_i + (cos(\phi_1) + jsin(\phi_1))(f_r + jf_i)\\
$$</p>
<p>$$
  KSpace_2: y_r + jy_i = w_r + jw_i + (cos(\phi_2) + jsin(\phi_2))(f_r + jf_i)\\
$$</p>
<p><br/></p>
<p>It is noted that since the magnetic properties of fat and water are known, $\phi_1$ and $\phi_2$ are known; thus, the cosine and sine of each may be computed:</p>
<p><br/></p>
<p>$$
  cos(\phi_1) \rightarrow{} a \\
  cos(\phi_2) \rightarrow{} b \\
  sin(\phi_1) \rightarrow{} c \\
  sin(\phi_2) \rightarrow{} d
$$</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>Isolating for the real and imaginary components of each K-Space:</p>
<p><br/></p>
<p>$$KSpace_1:$$</p>
<p>$$
  x_r = w_r + af_r - cf_i\\
$$</p>
<p>$$
  x_i = w_i + cf_r + af_i\\
$$</p>
<p><br/></p>
<p>$$KSpace_2:$$</p>
<p>$$
  y_r = w_r + bf_r - df_i\\
$$</p>
<p>$$
  y_i = w_i + df_r + bf_i\\
$$</p>
<p><br/></p>
<p>Recall that the fat component of the signal was mixed with some complex exponential due to it being imaged within the water's rotating frame of reference. Per Euler's formula, for any real value of $\phi_1$ and $\phi_2$, the complex exponential may be written as:</p>
<p><br/></p>
<p>$$
  e^{j\phi_1} = cos(\phi_1) + jsin(\phi_1) \leftrightarrow{} a + jc
$$</p>
<p>$$
  e^{j\phi_2} = cos(\phi_2) + jsin(\phi_2) \leftrightarrow{} b + jd
$$</p>
<p><br/></p>
<p>Thus, the set of linear equations may be written in matrix format per the following. It is important to note that $x_r$, $x_i$, $y_r$, and $y_i$ are known values as they represent the real and imaginary components of each point in K-Space 1 and K-Space 2. As such, the set of equations must be  re-arranged such that we may resolve the water and fat components.</p>
<p><br/></p>
<p>$$
  \begin{bmatrix}
  x_r \\
  x_i \\
  y_r \\
  y_i
  \end{bmatrix}
  =
  \begin{bmatrix}
  1 &amp; 0 &amp; a &amp; -c \\
  0 &amp; 1 &amp; c &amp; a \\
  1 &amp; 0 &amp; b &amp; -d \\
  0 &amp; 1 &amp; d &amp; b
  \end{bmatrix}
  \begin{bmatrix}
  w_r \\
  w_i \\
  f_r \\
  f_i
  \end{bmatrix}
$$</p>
<p><br/></p>
<p>The system of equations may therefore be re-arranged per the following:</p>
<p><br/></p>
<p>$$
  \begin{bmatrix}
  w_r \\
  w_i \\
  f_r \\
  f_i
  \end{bmatrix}
  =
  \begin{bmatrix}
  1 &amp; 0 &amp; a &amp; -c \\
  0 &amp; 1 &amp; c &amp; a \\
  1 &amp; 0 &amp; b &amp; -d \\
  0 &amp; 1 &amp; d &amp; b
  \end{bmatrix}^{-1}
  \begin{bmatrix}
  x_r \\
  x_i \\
  y_r \\
  y_i
  \end{bmatrix}
$$</p>
<p><br/></p>
<p>The solution identified herein assumes the matrix is non-singular and thereby invertible. The system of equations is solved iteratively for each point in K-Space to resolve the fat and water components from the distorted image. As such, $x_r$, $x_i$, $y_r$, $y_i$ and the coefficient matrix represents data for a single point in K-Space; the values of a, b, c, and d vary depending on the position in K-Space.</p>
<p>The inverse of the coefficient matrix is computed through a multiplication of the matrix's adjugate or adjoint by the reciprocal of the absolute value of the matrix's determinant. For instance, given some matrix A:</p>
<p><br/></p>
<p>$$
A^{-1} = \frac{adj(A)}{\mid A \mid}
$$</p>
<p><br/></p>
<p>The system of equations was solved iteratively for each point in K-Space using <code>np.linalg.solve</code>.</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">fat_kspace_reconstructed</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="n">image_size</span><span class="p">,</span> <span class="n">image_size</span><span class="p">),</span> <span class="n">dtype</span> <span class="o">=</span> <span class="nb">complex</span><span class="p">)</span>
<span class="n">water_kspace_reconstructed</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="n">image_size</span><span class="p">,</span> <span class="n">image_size</span><span class="p">),</span> <span class="n">dtype</span> <span class="o">=</span> <span class="nb">complex</span><span class="p">)</span>

<span class="n">a</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">phi1</span><span class="p">)</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">phi2</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">phi1</span><span class="p">)</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">phi2</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="k">for</span> <span class="n">ky</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">image_size</span><span class="p">):</span>
  <span class="k">for</span> <span class="n">kx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">image_size</span><span class="p">):</span>

    <span class="n">x_r</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">real</span><span class="p">(</span><span class="n">kspace1</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">])</span>
    <span class="n">x_i</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">imag</span><span class="p">(</span><span class="n">kspace1</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">])</span>
    <span class="n">y_r</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">real</span><span class="p">(</span><span class="n">kspace2</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">])</span>
    <span class="n">y_i</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">imag</span><span class="p">(</span><span class="n">kspace2</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">])</span>

    <span class="n">constants</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">x_r</span><span class="p">,</span> <span class="n">x_i</span><span class="p">,</span> <span class="n">y_r</span><span class="p">,</span> <span class="n">y_i</span><span class="p">],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">float64</span><span class="p">)</span>

    <span class="n">coefficients</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span>
        <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">a</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">],</span> <span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">c</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">]],</span>
        <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">c</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">],</span> <span class="n">a</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">]],</span>
        <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">b</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">],</span> <span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="n">d</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">]],</span>
        <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">d</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">],</span> <span class="n">b</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">]]],</span> <span class="n">dtype</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">float64</span><span class="p">)</span>

    <span class="n">w_r</span><span class="p">,</span> <span class="n">w_i</span><span class="p">,</span> <span class="n">f_r</span><span class="p">,</span> <span class="n">f_i</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">solve</span><span class="p">(</span><span class="n">coefficients</span><span class="p">,</span> <span class="n">constants</span><span class="p">)</span>

    <span class="n">water_kspace_reconstructed</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">w_r</span> <span class="o">+</span> <span class="p">(</span><span class="mi">1</span><span class="n">j</span><span class="p">)</span><span class="o">*</span><span class="n">w_i</span><span class="p">)</span>
    <span class="n">fat_kspace_reconstructed</span><span class="p">[</span><span class="n">ky</span><span class="p">,</span> <span class="n">kx</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">f_r</span> <span class="o">+</span> <span class="p">(</span><span class="mi">1</span><span class="n">j</span><span class="p">)</span><span class="o">*</span><span class="n">f_i</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">kspace_total</span> <span class="o">=</span> <span class="n">water_kspace_reconstructed</span> <span class="o">+</span> <span class="n">fat_kspace_reconstructed</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="6">Plotting the Reconstructed Images</font></p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">plot_fat_water</span><span class="p">(</span><span class="n">inverse_fft</span><span class="p">(</span><span class="n">fat_kspace_reconstructed</span><span class="p">),</span> <span class="n">inverse_fft</span><span class="p">(</span><span class="n">water_kspace_reconstructed</span><span class="p">),</span> <span class="n">inverse_fft</span><span class="p">(</span><span class="n">kspace_total</span><span class="p">),</span> <span class="s1">'Reconstructed Image'</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p><font size="6">Limitations</font></p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>The approach identified herein assumes that the composition of the sample is entirely fat and water, which may not necessarily <em>always</em> hold in the context of real-world data. For instance, the sample may be composed of a mixture of tissues including fat, water, and air that may impede the ability of this approach to perform the separation or reconstruction. Furthermore, there are numerous image artifacts that may be induced via EPI. For instance, T2 decay results in substantial signal loss in the case where data is collected over long periods (i.e. long TE). Additionally, magnetic susceptibility differences between varies tissues may induce some additional gradient during imaging resulting in geometric distortion. These considerations are important in the context of real-world imaging; however, these considerations are not accounted for in this study.</p>
</div>
</div>
</div>
</div>
</main>
</body>
</html>
