_str = input()
# _str = '5,0,3,8,6'
# _str = '1,1,1,0,6,12'
_list = _str.split(',')

# 逐一拆成兩邊
for n in range(1, len(_list)):
    ans = True
    # 左邊
    for l in _list[:n]:
        # 右邊
        for r in _list[n:]:
            # 若左邊其中一個數字大於右邊其中一個數字
            if l > r:
                # 結束重來
                ans = False
                break
                
        if not ans:
            break

    # 若左邊數字都小於右邊數字
    if ans:
        print(n)