# -*- coding: utf-8 -*-
"""
@Time ： 2025/7/21 07:08
@Auth ： 浮生半日闲
@File ： 01
@IDE ： PyCharm
@Motto：Code changes Everything
"""

from langchain_community.document_loaders import TextLoader, DirectoryLoader, UnstructuredImageLoader
from llama_index.core import SimpleDirectoryReader
from unstructured.partition.text import partition_text
from unstructured.partition.ppt import partition_ppt

if __name__ == "__main__":
    # loader = TextLoader("res/西游记/第一回.txt")
    # docs = loader.load()
    # print(docs)

    # # 指定特定加载器，异常跳过
    # loader = DirectoryLoader("res", show_progress=True, silent_errors=True, loader_cls=TextLoader)
    # docs = loader.load()
    # print(f"文档数量：{len(docs)}")

    # loader = DirectoryLoader("res", glob="**/*.txt", show_progress=True, use_multithreading=True)
    # docs = loader.load()
    # print(f"txt 文档数量：{len(docs)}")

    # # 指定特定加载器，解析速度更快
    # loader = DirectoryLoader("res", glob="**/*.txt", loader_cls=TextLoader)
    # docs = loader.load()
    # print(f"txt 文档数量：{len(docs)}")

    # dir_reader = SimpleDirectoryReader("res")
    # documents = dir_reader.load_data(show_progress=True)
    # print(f"文档数量：{len(documents)}")
    # print(documents[0])

    # text = "res/西游记/第一回.txt"
    # text = "res/知识星球/粥左罗-爆发式成长思维-1.md"
    # elements = partition_text(text)
    # for i,element in enumerate(elements):
    #     print(f"\n--- Element{i + 1} ---")
    #     print(f"元素类型： {element.__class__.__name__}")
    #     print(f"文本内容： {element.text}")
    #     if hasattr(element, 'metadata'):
    #         print(f"元数据：")
    #         metadata = vars(element.metadata)
    #         valid_metadata = {k: v for k, v in metadata.items() if not k.startswith('_') and v is not None}
    #         for key, value in valid_metadata.items():
    #             print(f"  {key}: {value}")

    # image_path = "res/情绪卡片-600x600.png"
    # loader = UnstructuredImageLoader(image_path, mode="elements", ocr_languages="chi_sim")
    # data = loader.load()
    # print(data)

    ppt_elements = partition_ppt(filename="res/2024.5.7KISSABC全国教育研讨会.pptx")
    for element in ppt_elements:
        print(element.text)
