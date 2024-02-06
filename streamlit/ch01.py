import streamlit as st
import streamlit.components.v1 as components

def main():
    st.markdown("## Chapter 00: 기본")

    st.title("Title: st.title")
    st.header("Header: st.header")
    st.subheader("subheader: st.subheader")
    
    st.write("st.writer를 이용해서 print()을 사용할 수 있다.")
    st.write("-" * 50)
    
    a, b = 1, 2
    st.write(f'a + b = {a+b}')

    st.markdown("## Chapter 01: st.markdown")

    st.write("https://docs.streamlit.io/library/api-reference/text/st.markdown")
    #https://docs.streamlit.io/library/api-reference/text/st.markdown
    
    st.write("st.markdown()을 사용해서 마크다운 문법으로 텍스트와 정보를 표현할 수 있다. 아래는 예시")
    st.write("-" * 50)
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)

    st.markdown("""
# Part 1.
                -색상 테스트: ~~~
## Chapter 1. 수식
- 피타고라스 정리: :red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:
                """)
    st.markdown("## Chapter 2. \n"
            "- Streamlit is **_really_ cool**.\n"
            "   * This text is :blue[colored blue], and this is **:red[colored] ** and bold.")

    st.write("-" * 50)

    st.markdown("HTML CSS 마크다운 적용도 가능하다.")
    html_css = """
    <style>
        table.customTable {
        width: 100%;
        background-color: #FFFFFF;
        border-collapse: collapse;
        border-width: 2px;
        border-color: #7ea8f8;
        border-style: solid;
        color: #000000;
        }
    </style>
    <table class="customTable">
      <thead>
        <tr>
          <th>이름</th>
          <th>나이</th>
          <th>직업</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Evan</td>
          <td>25</td>
          <td>데이터 분석가</td>
        </tr>
        <tr>
          <td>Sara</td>
          <td>25</td>
          <td>프로덕트 오너</td>
        </tr>
      </tbody>
    </table>
    """
    st.markdown(html_css, unsafe_allow_html=True)
    st.write(" ")
    st.markdown("""     
        외부에서 style.css 파일을 불러오고 string으로 변환
        string으로 변환한 것을 기존 HTML로 접목할 수 있다.
""")

    st.write("-" * 50)

    st.markdown("HTML JS Streamlit 적용도 가능함")
    js_code = """ 
    <h3>Hi</h3>
    <script>
    function sayHello() {
        alert('Hello from JavaScript in Streamlit Web');
    }
    </script>
    <button onclick="sayHello()">Click me</button>
    """
    components.html(js_code)


if __name__ == "__main__":
    main()