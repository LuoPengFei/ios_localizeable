# iOS多语言Excel 与 Localizeable.string 互转
iOS多语言，读取Excel写入Localizeable.string文件

### 实现feature

- 读取Excel写入Localizeable.string文件
- 检查Localizeable.string文件格式化是否有错误


### 待添加
- Localizeable.string文件重复定义
- Localizeable.string文件介入百度/谷歌翻译api
- Localizeable.string文件导出为Excel

### 使用

Localizations为示例工程；
localizable_py 中为Python脚本
- localizeable 运行读取Excel文件
- localizable_error 检查 Localizeable.string文件 格式
- localizeable_r_excel Excel读取
- localizeable_w_excel Excel写入(待完成)
- utils 写了路径配置，目前路径常量运行需要修改一下。


运行localizeable ，会将text.xlsx中多语言文件写入Localizations为示例工程的 Localizeable.string文件，示例中目前支持多语言：简体、繁体、英文。
