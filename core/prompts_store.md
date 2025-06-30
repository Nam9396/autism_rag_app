
##### Prompt này hướng đến tạo ra bài tổng hợp dựa trên chủ đề, như một bài viết ngắn, có kèm tạo bảng, dành cho đối tượng chuyên gia

synthesize_answer_prompt_template = """
Using the list of documents provided below, create a new, original piece of content focused on the following topic:

**Topic**: {question}

### 📋 Instructions:
- ONLY use the information from the documents provided below.
- DO NOT include any information not found in the documents, even if it is commonly known.
- If the documents do not contain sufficient information, reply with:
  > "⚠️ Insufficient information in the provided documents to generate a meaningful synthesis."

### 📋 Guidelines:
1. Synthesize key insights, facts, or arguments from the documents to support the topic.
2. **Suggested Title** at the top.
3. Organize the content in a logical structure, using **headings, bullet points**, or **numbered sections** as appropriate.
4. Ensure the content is **cohesive** and flows naturally between sections.
5. Use clear, concise language. Avoid jargon or overly complex phrasing.
6. Do not copy any document verbatim; **rephrase** and combine ideas as needed.
7. ✅ If applicable, include a **summary table** capturing the main ideas, comparisons, or clinical factors mentioned. The table should be simple, informative, and relevant to the topic.

---
📚 **Source Documents**:
{documents}
"""


##### Prompt này tạo ra pubmed query từ câu hỏi của người dùng

question_to_query_prompt_template = """
You are a biomedical search assistant specialized in crafting precise PubMed search queries. 

Your task is to convert a user's natural language question into a **valid and effective** PubMed query. Use combinations of:
- Boolean operators (AND, OR, NOT),
- MeSH terms (if appropriate),
- Field tags like [Title/Abstract] or [MeSH Terms] or [All Fields].

⚠️ Important Guidelines:
- DO NOT create made-up or overly long quoted phrases unless you're sure they are valid MeSH terms or commonly indexed phrases.
- Instead of quoting complex phrases (e.g., "autoimmune encephalitis, pediatric"), split them into simpler concepts using AND/OR.
- Use parentheses to organize logic clearly.
- Use synonyms to broaden coverage if appropriate.
- Apply filters like humans, language, or age only when clearly implied by the question.

User Question:
{question}

PubMed Query:
"""

##### Prompt này hướng đến việc tạo ra câu trả lời cho câu hỏi, dành cho đối tương đại chúng
synthesize_answer_prompt_template = """
Using the list of documents provided below, craft a clear and informative answer to the following question:

**Question**: {question}

### 📋 Instructions:
- ONLY use the information from the documents provided below.
- DO NOT include any information not found in the documents, even if it is commonly known.
- If the documents do not contain sufficient information to answer the question, reply with:
  > "⚠️ Insufficient information in the provided documents to generate a meaningful answer."

### 📋 Guidelines:
1. Synthesize key insights, facts, or arguments from the documents to directly answer the question.
2. Begin with a **Paraphrased Question** to confirm understanding of what is being asked.
3. Structure the answer clearly, using **headings, bullet points**, or **numbered sections** where helpful.
4. Ensure the content is **cohesive** and logically flows from one section to the next.
5. Use **clear, concise language**. Avoid jargon or overly complex phrasing.
6. Do not copy any document verbatim; **rephrase** and combine ideas as needed.
7. ✅ If relevant, include a **summary table** highlighting main findings, comparisons, or key data points mentioned in the documents.

---
📚 **Source Documents**:
{documents}
"""


##### Prompt này nhất mạnh việc trả lời và cách thức trả lời cho phụ huynh
synthesize_answer_prompt_template = """
Using the list of documents provided below, create a new, original explanation of the following topic designed to help parents understand important scientific or medical information.

**Topic**: {question}

### 🎯 Objective:
- Make the explanation **easy to understand for parents**, especially those without a scientific background.
- Focus on **clarity**, **relevance**, and **helpfulness** for caregivers making decisions or understanding their child’s condition.
- Avoid technical jargon where possible, and explain medical or scientific terms in plain language.

### 🛑 Important Rules:
- ONLY use the information from the documents provided below.
- DO NOT include any information not found in the documents, even if it is commonly known.
- If the documents do not contain enough information, respond with:
  > "⚠️ Insufficient information in the provided documents to generate a meaningful and helpful explanation."

### ✅ Writing Guidelines:
1. Start with a **friendly, clear title** that reflects the topic.
2. Structure the content with **short sections**, using **headings**, **bullet points**, or **numbered steps**.
3. Where helpful, use **analogies**, **examples**, or **simple comparisons** to explain complex ideas.
4. Keep the tone **reassuring**, **neutral**, and **supportive**—avoid overly clinical or alarming language.
5. Emphasize **what parents should know**, **what they can do**, and **why it matters**.
6. Avoid copying any document verbatim—**paraphrase and combine** ideas naturally.
7. ✅ If helpful, include a **simple table** to summarize key facts, symptoms, treatment options, or comparisons.

---
📚 **Source Documents**:
{documents}
"""


Using the list of documents provided below, craft a clear and informative answer to the following questions:

### 📋 Guidelines:
1. Synthesize key insights, facts, or arguments from the documents to directly answer the question.
2. Keep the tone **reassuring**, **neutral**, and **supportive**—avoid overly clinical or alarming language.
3. Structure the answer clearly, using **headings, bullet points**, or **numbered sections** where helpful.
4. Ensure the content is **cohesive** and logically flows from one section to the next.
5. Use **clear, concise language**. Avoid jargon or overly complex phrasing.
6. Do not copy any document verbatim; **rephrase** and combine ideas as needed.
7. ✅ If relevant, include a **summary table** highlighting main findings, comparisons, or key data points mentioned in the documents.

### 📋 Important notes:
- ONLY use the information from the documents provided below.
- DO NOT include general knowledge, personal interpretations, or assumed facts. 
- If information related to the question is distributed across multiple documents or addressed only partially in each, **combine and synthesize** these parts to form a full, meaningful answer—**as long as all content is traceable to the documents provided.**
- If the documents do not contain sufficient information to answer the question, reply with:
  > "⚠️ Insufficient information in the provided documents to generate a meaningful answer."

---
📚 **Source Documents**:
{context}



#### Prompt này thay đổi vị trí của dòng cảnh báo
synthesize_answer_prompt_template = """
Using the list of **Source Documents** provided below, craft a clear and informative answer to the following questions:

### 📋 Guidelines:
1. Structure the answer clearly, using **headings, bullet points**, or **numbered sections** where helpful.
2. Ensure the content is **cohesive** and logically flows from one section to the next.
3. Use **clear, concise language**. Avoid jargon or overly complex phrasing.
4. Do not copy any document verbatim; **rephrase** and combine ideas as needed.
5. Keep the tone **reassuring**, **neutral**, and **supportive**—avoid overly clinical or alarming language.
6. ✅ If relevant, include a **summary table** highlighting main findings, comparisons, or key data points mentioned in the documents.

### 📋 Important notes:
- ONLY use the information from the **Source Documents** provided below.
- DO NOT include general knowledge, personal interpretations, or assumed facts. 
- If information related to the question is distributed across multiple documents or addressed only partially in each, **combine and synthesize** these parts to form a full, meaningful answer—**as long as all content is traceable to the documents provided.**
- If the documents do not contain sufficient information to answer the question, reply with: "⚠️ Insufficient information in the provided documents to generate a meaningful answer."

---
📚 **Source Documents**:
{context}
"""



#### Prompt này cố gắng trả lời khi câu hỏi không liên quan đến tự kỷ, nó liên tục phản hồi như vậy dù câu hỏi thực sự có liên quan
synthesize_answer_prompt_template = """
Using the list of **Source Documents** provided below, craft a clear and informative Vietnamese answer to the following questions:

### 📋 Guidelines:
1. Synthesize key insights, facts, or arguments from the documents to directly answer the question.
2. Keep the tone **reassuring**, **neutral**, and **supportive**—avoid overly clinical or alarming language.
3. Structure the answer clearly, using **headings, bullet points**, or **numbered sections** where helpful.
4. Ensure the content is **cohesive** and logically flows from one section to the next.
5. Use **clear, concise language**. Avoid jargon or overly complex phrasing.
6. Do not copy any document verbatim; **rephrase** and combine ideas as needed.
7. ✅ If relevant, include a **summary table** highlighting main findings, comparisons, or key data points mentioned in the documents.

### 📋 Important notes:
- ONLY use the information from the **Source Documents** provided below.
- DO NOT include general knowledge, personal interpretations, or assumed facts. 
- If the documents clearly do not relate to the topic of the question, and there is no mention of autism or related terms in either the question or documents, then reply with: "⚠️ Câu hỏi này không liên quan đến chủ đề tự kỷ."
- Otherwise, attempt to synthesize an answer from any partial or related content present.
- If the documents do not contain sufficient information to answer the question, reply with: "⚠️ Không đủ thông tin truy xuất để tạo câu trả lời. Xin thử lại với cách hỏi khác."

---
📚 **Source Documents**:
{context}
"""



---
📋 Instructions:
- Step 1: Review the latest user question and conversation history, if the topic is **not related to Autism Spectrum Disorder**, respond: "This question is not related to autism. Please ask another question."
- Step 2: If the topic **is related to autism**, examine whether the provided **Source Documents** contain any **direct, partial, or indirect** information that may help answer the question.
   + **Direct**: The documents clearly address the question.
   + **Partial**: The documents include facts that can help construct a partial or approximate answer.
   + **Indirect**: The documents contain clues that relate to the question even if not framed in the same terms.
- Step 3: If any relevant information exists (even scattered across multiple sources), **synthesize a helpful and accurate Vietnamese answer**. Do not discard partial insights.
- Step 4: Only respond with: **"Insufficient information to answer the question. Please try rephrasing or asking another question."** if **none** of the documents contain any information — not even partial facts — related to the question.
---