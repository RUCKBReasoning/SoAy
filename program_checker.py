from model import *
import traceback

aminer_api = aminer_soay()

def generate_result_from_process(process):
    global searchPerson 
    global searchPublication
    global getCoauthors 
    global getPersonInterest
    global getPersonPubs
    global getPersonBasicInfo
    global getPublication
    searchPerson = aminer_api.searchPersonComp
    searchPublication = aminer_api.searchPublication
    getCoauthors = aminer_api.getCoauthors
    getPersonInterest = aminer_api.getPersonInterest
    getPersonPubs = aminer_api.getPersonPubs
    getPersonBasicInfo = aminer_api.getPersonBasicInfo
    getPublication = aminer_api.getPublication
    # print('generated process: \n', process)   
    try: 
        # final_result = ''
        exec(process, globals())
        result = final_result
        return result
    except Exception as e:
        error_info = traceback.format_exc()
        print(error_info)
        return 'exe error'
    
if __name__ == "__main__":
    print("请输入多行代码，结束输入时请输入'eoc'并回车：")
    lines = []
    while True:
        line = input()
        if line == 'eoc':
            break
        lines.append(line)

    code = '\n'.join(lines)
    print("输入的代码是：{}".format(code))
    result = generate_result_from_process(process = code)
    print('代码执行结果:\n {}'.format(result))