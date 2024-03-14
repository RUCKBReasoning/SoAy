import jsonlines

dicts = {}

with jsonlines.open('prompt_jsonl/prompt_1101.jsonl', 'r') as f:
    for dict in f:
        dicts[dict['index']] = dict['prompt']
    f.close()

with jsonlines.open('prompt_json/prompt_dict_1101.json', 'w') as f:
    f.write(dicts)
    f.close()