# study_rag

# RAG：
RAG（Retrieval-Augmented Generation）是一种结合了信息检索和生成模型的技术。它通过检索相关文档或片段来增强生成模型的回答能力，从而提高回答的准确性和相关性。

# RAG的核心：

当大模型面对一个问题时，并非依赖其训练过程中“记住”的知识来回答，相反，它可以访问一个外部知识库或文档集，从中检索与当时问题相管的片段，将这些最新或特定领域的外部信息纳入“思考”，然后再尽心回答生成。

# RAG核心组件：
* 知识嵌入
* 检索器
* 生成器

# RAG的工作流程：
* 数据导入
* 文本分块
* 知识嵌入
* 向量存储
* 检索前处理
* 基于索引的检索
* 检索后处理
* 相应生成
* 系统评估
* 复杂检索策略和范式

# 环境搭建：
# 1. 安装python虚拟环境管理工具：
`curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh && bash Miniconda3-latest-MacOSX-arm64.sh`

默认安装后会每次启动终端时启动base环境，设置不打开conda

`conda config --set auto_activate_base false`

# 2. 创建虚拟环境 

`conda create -n rag_py3.12 python=3.12`

# 3. 激活虚拟环境

`conda activate rag_py3.12`

# 实战操作
# 1. 使用llamaindex搭建RAG

`pip install llama-index`




