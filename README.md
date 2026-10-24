# research-html-ppt-skill

可切换模板的演示文稿制作技能，适用于 Codex 等支持 `SKILL.md` 的 Agent。

## 功能

- 内置科研蓝白模板，也可适配 HTML、PPTX、PDF 或图片参考。
- 将叙事、内容和视觉配置分离，支持制作过程中更换模板。
- 统一跨页术语、标题、图例和结论，区分共享事实与局部条件。
- 均匀布局、图像优先、简短图注，附带十种空白 HTML 版式。

这是制作指导和模板资源，不是独立的 PPTX 转换器，也没有运行时换肤按钮。PPTX/PDF 渲染需要宿主环境提供相应工具；空白 HTML 无需外部依赖。

## 目录

```text
skills/research-html-ppt/
  SKILL.md
  agents/openai.yaml
  references/
  assets/blank-template.html
scripts/validate.py
```

## 安装

下载或克隆本仓库，将 `skills/research-html-ppt` 整个目录复制到 `$CODEX_HOME/skills/`；未设置 CODEX_HOME 时使用 `~/.codex/skills/`。Windows 默认路径为 `%USERPROFILE%\.codex\skills\research-html-ppt`。不要仅复制 SKILL.md，也不要直接覆盖已有修改版。

也可让 Codex 的 skill-installer 从本仓库安装，技能路径指定为 `skills/research-html-ppt`。安装完成后在下一轮对话中调用。

## 使用

```text
使用 $research-html-ppt，按附件模板制作项目汇报，输出 HTML。
使用 $research-html-ppt，保留内容，将现有演示切换为新的极简模板。
使用 $research-html-ppt 制作 PPTX，统一术语与图例，避免长篇图注。
```

没有指定模板时，技能根据任务建立视觉方案，不会强制使用内置蓝白风格。复制 `assets/blank-template.html` 可离线浏览十种空白版式。

## 验证与贡献

运行 `python scripts/validate.py` 检查文件结构、内部链接、空白内容及模板引用。该检查不代替浏览器或 PPTX 渲染检查。提交改动时说明适用场景，并对受到影响的版式进行视觉验证。

发布内容只包含通用制作规范与空白模板，不包含原始研究汇报、实验数据或本机路径。

## 许可证

MIT，见 [LICENSE](LICENSE)。
