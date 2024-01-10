#requests 는 http 요청을 보내기 위한 외부 라이브러리
# requests 라이브러리는 웹 페이지의 콘텐츠를 가져오거나, API에 데이터를 전송하거나, 웹 기반 서비스와 상호작용하는 등 다양한 HTTP 요청을 손쉽게 처리할 수 있도록 도와줍니다.



import requests
from bs4 import BeautifulSoup
import openai
from tqdm import tqdm
import time

# 다수의 작업을 병렬로 실행할 수 있게하는 모듈
import concurrent.futures                        
import os


# https://platform.openai.com/docs/api-reference 에서 gtp api 발급받기 최소 5달러 결제해야함

openai.api_key = "secret_tell_me"

# 하이브 재무제표 주석 URL
url = 'https://dart.fss.or.kr/report/viewer.do?rcpNo=20231115000333&dcmNo=9501770&eleId=5&offset=88839&length=421456&dtd=dart3.xsd'

# HTTP 요청을 통해 웹 페이지의 내용을 가져옵니다.
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    part_length = len(text) // 11
    parts = [text[i * part_length: (i + 1) * part_length] for i in range(11)]

    # 주석1부터 주석11까지의 텍스트를 변수로 저장합니다.
    주석1 = parts[0]
    주석2 = parts[1]
    주석3 = parts[2]
    주석4 = parts[3]
    주석5 = parts[4]
    주석6 = parts[5]
    주석7 = parts[6]
    주석8 = parts[7]
    주석9 = parts[8]
    주석10 = parts[9]
    주석11 = parts[10]

    with open(f'H:\내 드라이브\web_project\single_pages\datas\hybe_data2\\joosuk_end.txt', 'w', encoding='utf-8') as file:
        file.write(text)

else:
    print("웹 페이지를 불러오는 데 실패했습니다.")

for i in tqdm(range(5), desc="Refining"):
    time.sleep(1)

# 메시지 정의
message = """
너는 이제부터 30년 경력의 회계사이다.
내용 시작 부분부터 요약해주되 스킵되는 내용이 없게 요약시켜줘. 예를 들어
//////////////
주주명
당분기말
전기말

보통주식수(주)
지분율(%)
보통주식수(주)
지분율(%)

방시혁
13,151,394
31.6
13,151,394
31.8
//////////////
같은 내용이 나오면 방시혁 주주는 보통주식수 13,151,394를 보유 하고 있습니다. 와 같이 요약해줘 주석은 총 11개가 있으므로 내용이 잘려있다. 내용이 연결되지 않으면 자연스럽게 마무리지어줘.
"""

def refine(output, temperature=0, max_tokens=4096):

    prompt = f"{message}\n내용 시작\n\n{output}"

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content



def process_annotation(annotation, index):
    result = refine(annotation)
    with open(f'H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data2\\gpt_output{index}.txt', 'w', encoding='utf-8') as file:
        file.write(result)
    return f"주석 {index} 결과:\n{result}\n"

all_annotations = [주석1, 주석2, 주석3, 주석4, 주석5, 주석6, 주석7, 주석8, 주석9, 주석10, 주석11]

# concurrent.futures의 ThreadPoolExecutor 클래스를 사용하여 각 주석을 병렬로 처리
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_annotation, annotation, i) for i, annotation in enumerate(all_annotations, start=1)]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())


# 요약 내용을 모두 합치는 코드 시작

#요약 파일이 모두 생성될 때까지 기다림
def wait_for_files(file_count, directory, prefix, timeout=60):
    start_time = time.time()
    while True:
        files = [f for f in os.listdir(directory) if f.startswith(prefix)]
        if len(files) >= file_count or (time.time() - start_time) > timeout:
            break
        time.sleep(5) # 5초마다 파일 개수 확인  

# 모든 파일의 내용을 합치는 함수
def combine_files(file_count, input_directory, input_prefix, output_file):
    combined_content = ""
    for i in range(1, file_count + 1):
        file_path = os.path.join(input_directory, f"{input_prefix}{i}.txt")
        with open(file_path, 'r', encoding='utf-8') as file:
            combined_content += file.read() + "\n" + "\n"

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(combined_content)

        

# 주석 파일 처리 후
input_directory = 'H:\\내 드라이브\\web_project\\single_pages\\datas\\hybe_data2'
input_prefix = 'gpt_output'
output_file = os.path.join(input_directory, 'gpt_output_end.txt')

# 파일이 모두 생성될 때까지 기다리기
wait_for_files(11, input_directory, input_prefix)

# 파일 내용 합치기
combine_files(11, input_directory, input_prefix, output_file)



