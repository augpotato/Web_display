import streamlit as st

# markdown
st.markdown('Streamlit Demo')

# 设置网页标题
st.title('一个傻瓜式构建可视化 web的 Python 神器 -- streamlit')

# 展示一级标题
st.header('1. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')


# 展示一级标题
st.header('2. 使用')

# 展示二级标题
st.subheader('2.1 生成 Markdown 文档')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')

'''
st.sidebar.title("图像检测参数调节器")  # 侧边栏
app_mode = st.sidebar.selectbox("切换页面模式:",
                                ["Run the app", "Show instructions", "Show the source code"])

# 展示栏目三
if app_mode == "Run the app":
    # readme_text.empty()      # 刷新页面
    st.markdown('---')
    st.markdown('## YOLOv3 检测结果:')

# 展示栏目一
elif app_mode == "Show instructions":
    st.sidebar.success('To continue select "Run the app".')
# 展示栏目二
'''