# 6 题目打包格式

DOMjudge支持以zip包格式导入和导出题目数据

基本格式遵循[problemformat.org](http://www.problemarchive.org/wiki/index.php/Problem_Format)上的题目格式规范。基本规范请参照上述网站。

最重要的是，DOMjudge定义了一些扩展：
* `domjudge-problem.ini`（必须）：元数据文件，参见下方。
* `problem.{pdf,html,txt}`（可选）：分发给参赛选手的题目陈述（题面）。文件扩展名可以是三个之一。如果有多个符合的文件，则使用其中一个。

`domjudge-problem.ini` 文件包含形如 `key = value` 的键值对。`=` 两端的空白符可选，值可以用引号包裹，以便包含换行。允许的关键字如下（这些关键字直接对应裁判后台的设置）：
* `probid` - 题目的短名（如 "A"）
* `name` - 题目显示的名字
* `allow_submit` - 允许提交这个题目，不允许将会使题目对队伍和对外隐藏
* `allow_judge` - 允许评判这个题目
* `timelimit` - 时间限制（秒，每个测试点）
* `special_run` - 专门的允许脚本的可执行ID(executable id)
* `special_compare` - 专门的比较脚本的可执行ID(executable id)
* `points` - 题目的分数（默认为1）
* `color` - 题目的 CSS 颜色规范

从 `jury/problems.php` 总览页面导入新的题目时`probid` 关键字是必须的，但在导入到现有题目时它会被忽略。其余剩余关键字都是可选的，若存在则覆盖当前值，否则保留当前值或默认值。测试数据文件会添加到已有的一组测试点中，因此上载仅包含测试用例文件的zip文件，可以轻松地将测试用例添加到已经配置好的题目中。当 `allow_submit` 是 `1` 时，若存在任何标程都会被自动提交。