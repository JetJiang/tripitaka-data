# 大藏经数据相关工作
- OCR Transform

    深度学习OCR识别的结果，以图片YB_22_713.jpg为例，其结果为YB_22_713.txt，表示《永乐北藏》第22册第713页的识别结果。
    
    这个结果需要转化为古籍平台系统可用的文件格式，包括切分信息和文本信息。
    
    其中，切分信息转化为json格式（见模板ocr-transform/template.json文件），结果文件目录及命名规则如：char-pos/YB/22/YB_22_713.json。转换时，需要用到切栏信息的辅助，切栏信息放在block-pos目录下。需要注意的是，OCR是在原图上进行处理，需要将坐标信息等比转化为宽度为1200的小图上。
    
    文本信息转化为txt格式，格式见ocr-transform/template.txt文件，结果文件目录及命名规则如：ocr-txt/YB/22/YB_22_713.txt。

    ocr-transform.py所完成的工作，就是这个转换过程。需要注意的是，图片命名除了三层结构，如YB_22_713.jpg，还有四层结构，如GL_1_1_1.jpg。程序要考虑这个兼容性。

- Page Txt Search

    针对一页图像生成的OCR文本ocr-txt进行文字校对时，为了快速找到OCR文本中的错误，我们需要从CBETA中找到该页藏经图像对应的藏经整经经文cbeta-sutra-txt，然后从中找到与该页ocr-txt匹配的cmp-txt，再用cmp-txt与ocr-txt进行对比，从而找到OCR文本中可能的错误。

    page-txt-search.py所完成的工作，就是从sutra-txt中找到与ocr-txt匹配的cmp-txt。

    这里以六十华严为例，其文本为T0278.txt，请找出LC_79_1_1.txt/LC_79_48_1.txt/QL_24_31.txt对应的cmp-txt，结果文件目录及命名规则如：cmp-txt/LC/79/1/LC_79_1_1.txt。

- Page Txt Compare

    在前叙的Page Txt Search基础上，需要进一步将OCR文本（ocr-txt）与比对文本（cmp-txt）进行比对，找出二者差异。

    针对文字差异（也叫异文），需要进一步查询异体字表variants-table.txt，看二者是否为异体字关系。如果是，则需要在比对结果文件cmp-result.json中指出来。json文件格式见page-txt-compare/template.json。
    
    page-txt-compare.py所完成的工作，就是这个比对过程。
    这里以六十华严为例，请对LC_79_1_1/LC_79_48_1/QL_24_31进行处理，结果文件目录及命名规则如：cmp-res/LC/79/1/LC_79_1_1.json。
