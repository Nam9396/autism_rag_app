import streamlit as st 

st.image("static/boy-playing.jpg")

st.markdown("""
#### Giới thiệu
Chào mừng bạn đến với **TukyChat** – nơi cung cấp thông tin đa dạng và tin cậy về rối loạn phổ tự kỷ, dành riêng cho phụ huynh Việt Nam.

Chúng tôi hiểu rằng hành trình chăm sóc và hỗ trợ trẻ tự kỷ không hề dễ dàng, đặc biệt khi nguồn thông tin còn hạn chế. Với mục tiêu đồng hành cùng bạn, ứng dụng mang đến những kiến thức hữu ích, dễ tiếp cận và thiết thực.

Bạn có thể đặt câu hỏi về các vấn đề liên quan đến rối loạn phổ tự kỷ như một buổi tư vấn. Chủ đề rất đa dạng: từ tầm soát, chẩn đoán, can thiệp, đến kinh nghiệm chăm sóc trẻ hàng ngày.

#### Ứng dụng hoạt động như thế nào
- Chúng tôi xây dựng cơ sở kiến thức về rối loạn phổ tự kỷ từ các sách chuyên ngành. 
- Khi bạn đặt câu hỏi, trí tuệ nhân tạo (AI) sẽ tìm kiếm thông tin trong sách và tổng hợp câu trả lời. 
- Nếu thông tin từ sách không đủ, ứng dụng tự động tìm kiếm thông tin từ các website để trả lời câu hỏi.

**Lưu ý:** thông tin được cung cấp là kết quả tổng hợp từ AI dựa trên dữ liệu đầu vào, không phải tư vấn trực tiếp từ bác sĩ.

#### Cách sử dụng ứng dụng hiệu quả
**TukyChat** cung cấp thông tin chuyên môn nhằm giúp bạn nâng cao hiểu biết về rối loạn phổ tự kỷ. Tuy nhiên, ứng dụng không thay thế cho tư vấn và quyết định chuyên môn từ bác sĩ. Vì vậy, **hãy coi đây là nguồn tham khảo và đến gặp chuyên gia y tế khi cần thiết.**

#### Làm gì nếu câu trả lời không như mong đợi?
Đôi khi, ứng dụng sẽ phản hồi: “Không đủ thông tin để trả lời câu hỏi...” hoặc bạn cảm thấy không hài lòng. Trong trường hợp này, bạn có thể:
1. Hỏi lại cùng câu hỏi đó một lần nữa. 
2. Hỏi lại với cách diễn đạt khác.
3. Đặt thêm thông tin cụ thể hơn.

Ngoài ra, với cùng một câu hỏi, mỗi lần hỏi lại có thể ra câu trả lời khác nhau. Đây là tính chất đặc trưng của hệ thống AI – tuy khác về diễn đạt, nhưng các câu trả lời vẫn đảm bảo truyền đạt những nội dung chính.

#### Nguy cơ và giới hạn
- Ứng dụng chỉ cung cấp thông tin về rối loạn phổ tự kỷ.
- Với các câu hỏi nằm ngoài lĩnh vực này, ứng dụng vẫn có thể trả lời nhưng không đảm bảo chất lượng thông tin.
- AI có thể tạo ra những câu trả lời thuyết phục và dễ hiểu, nhưng có thể chứa sai sót. Do đó, bạn cần xem xét kỹ lưỡng và xác minh thông tin trước khi áp dụng.

#### Quyền riêng tư
- Mọi cuộc hội thoại không được lưu trữ và sẽ bị xóa khi bạn tắt hoặc tải lại ứng dụng.
- Chúng tôi không thu thập thông tin cá nhân của người dùng.

#### Thông tin liên hệ
Chúng tôi rất mong nhận được góp ý, phản hồi và cơ hội hợp tác từ quý phụ huynh và đồng nghiệp.
Tác giả: Bs. Nguyễn Thành Nam (nguyenthanhnam9396@gmail.com)

#### Đảm bảo chất lượng
AI có thể tạo ra thông tin chưa chính xác hoặc diễn giải sai lệch. Để giảm thiểu điều này, chúng tôi đã:
- Yêu cầu AI chỉ trả lời dựa trên cơ sở dữ liệu đã được kiểm chứng.
- Dẫn nguồn tài liệu được sử dụng trong quá trình tổng hợp.
- Cài đặt để AI phản hồi “không đủ thông tin để trả lời” nếu câu hỏi vượt quá khả năng xử lý.

#### Nội dung lệnh dành cho AI (Prompt)        
You are acting as a Vietnamese physician who specializes in Autism Spectrum Disorder (ASD). Your task is to answer questions from Vietnamese parents about ASD using only the provided **Source Documents**.

**📋 Guidelines:**
1. Synthesize key insights, facts, or arguments from the documents to directly answer the question.
2. Keep the tone **reassuring**, **neutral**, and **supportive**—avoid overly clinical or alarming language.
3. Structure the answer clearly, using **headings, bullet points**, or **numbered sections** where helpful.
4. Ensure the content is **cohesive** and logically flows from one section to the next.
5. Use **clear, concise language**. Avoid jargon or overly complex phrasing.
6. Do not copy any document verbatim; **rephrase** and combine ideas as needed.
7. ✅ If relevant, include a **summary table** highlighting main findings, comparisons, or key data points mentioned in the documents.

**📋 Important notes:**
- Always respond in Vietnamese.
- **ONLY** use the information from the provided **Source Documents**.
- **DO NOT** include general knowledge, assumptions, or personal interpretations.
- **NEVER** fabricate or guess. If something is not supported by the documents, do not include it.
- If the **Source Documents** is not sufficient to answer the question, acknowledge the limitations of your response.

---
📚 **Source Documents**:
{context}

#### Cơ sở dữ liệu dùng để trả lời câu hỏi
**Sách chuyên ngành:**
- 100 Questions & Answers About Autism – Campoin Quinn
- Autism Spectrum Disorder: What Every Parent Needs to Know (2nd Edition) – Rosenblatt & Carbone (AAP)
- Encouraging Appropriate Behavior for Children on the Autism Spectrum – Shira Richman
- The Parent's Guide to In-home ABA Programs – Elle Olivia Johnson
- Assessment of Autism Spectrum Disorders – Goldstein, Naglieri, Ozonoff

**Website:**
- [CDC: Autism Spectrum Disorder](https://www.autismspeaks.org/)
- [National Autistic Society](https://www.autism.org.uk/)
- [Autistic Self Advocacy Network](https://autisticadvocacy.org/)
- [Autism Research Institute](https://autism.org/)

#### Thông tin kỹ thuật
- Ngôn ngữ lập trình: Python, LangChain, Streamlit
- Mô hình ngôn ngữ lớn (LLM): GPT-4.1-nano    
            
""")



