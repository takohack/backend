import json


# chapter = {"4月25日":"第六章:差分方程","4月14日":"第五章:复习",
#             "4月13日":"第四章:稳定性初步","4月07日":"第三章:线性微分方程组",
#             "4月06日":"第六章:线性微分方程","4月25日":"第六章:差分方程",
#             "4月25日":"第六章:差分方程"}


# chapter_dir = json.dumps(chapter,ensure_ascii=False)
# print(chapter_dir)
title = "title"
url = "url"
notice = {1:{title:"高等代数",url:"www.baidu.com"},2:{title:"ch03.ppt",url:"www.baidu.com"}}
notice_dir = json.dumps(notice,ensure_ascii=False)
print(notice_dir)