def solution(files):
    answer = []
    nums = [str(i) for i in range(0, 10)]
    files_detail = []
    
    for file in files:
        head, number, tail = '', '', ''
        i = 0
        while file[i] not in nums:
            head += file[i]
            i += 1
        while i < len(file) and file[i] in nums:
            number += file[i]
            i += 1
        tail = file[i:]
        files_detail.append([head, number, tail])
        
    files_detail.sort(key = lambda x : (x[0].upper(), int(x[1])))
    for f in files_detail:
        answer.append(f[0] + f[1] + f[2])
    
    return answer