from urllib import request
import json


with open("Default-SD1.5.json", "r", encoding="utf-8") as file:
    workflowJson = file.read()


def autoWorkflow():
    prompt_json = json.loads(workflowJson)

    prompt_json["8"]["inputs"]["text"] = "masterpiece best quality man"
    # set the seed for our KSampler node
    prompt_json["4"]["inputs"]["seed"] = 5

    data = {"prompt": prompt_json}
    body = json.dumps(data).encode("utf-8")
    # 4. 헤더 설정 (안정성을 위해 추가 추천)
    headers = {"Content-Type": "application/json"}
    req = request.Request("http://127.0.0.1:8188/prompt", data=body, headers=headers)

    with request.urlopen(req) as response:
        print("전송 완료:", response.status)  # 200이면 성공


autoWorkflow()