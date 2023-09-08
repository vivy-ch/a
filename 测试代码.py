import requests
url='https://haoma.baidu.com/api/v1/search'
JSON = {"data":"10fc699faa7d324762b52643ee377ccf4c48bb5174cc3ae3bf21fdb7b2c4c071c00436aa5ef2840b79edc8576e656c292345e7837790e5dd4e98f0d9ef59a0dad128f6953f09e3ac5049d582d78e28e0e67058243f36ad7cc7970f64c9b77ed962a6d9341ee94aff265ebd3ccb3f8925b188e8fc7f6152e587634711e6fd481f","key_id":"47","sign":"392955cf","page":1,"size":10,"search":"4008180280","user_search":"null"}


headers = {
     'Accept':'application/json, text/plain, */*'
    ,'Accept-Encoding':'gzip, deflate, br'
    ,'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    ,'Connection':'keep-alive'
    ,'Content-Length':'361'
    ,'Content-Type':'application/json;charset=UTF-8'
    ,'Cookie':'BAIDUID=A481276D7F923D57BD0450B26B62A1FB:FG=1; BAIDUID_BFESS=A481276D7F923D57BD0450B26B62A1FB:FG=1; __sec_t_key=08393d95-9e26-479b-b9ba-b192d34f4a14; Hm_lvt_71927aaa06a0dc9d2d16f927f1f6937f=1693984535; __bid_n=18a6958b30792961b66bea; BMAP_SECKEY=CFllOUQ3Q1SfFwyXjReIW7xTGdZmMGVHVX1rY5UfEd1rGUw3Q6440B6lrP2YNN43hbAFxem17eyNQCpa9KFnnjatB88gtLFP9Dmy0i_-GzWh4Y_0hcIMW10ws837FfNYFUH15C0X5Ry5TEr4ghLdKX7lIr9OYElcf5v9n_o2OAfwf1WEB2fSqf-LrJgDBFaN; RT="z=1&dm=baidu.com&si=a8f31caf-2a75-418e-960e-969c6d96b76e&ss=lm7enj8k&sl=6&tt=40ff&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; SECKEY_ABVK=CFllOUQ3Q1SfFwyXjReIW0In36+yNWr43vccxX1InGQ%3D; Hm_lpvt_71927aaa06a0dc9d2d16f927f1f6937f=1693984931; ab_sr=1.0.1_ZTgxOGI0ZGQ4ZDIzOGQ0MDMyZjE1Y2YyNTZkNTJmYWUyMmRiNDI3N2RkYTJhMDRhZWVmMmMwYWQ5ZTRlZmI4Mjg3YjI4YWQ2NDkzOTI5ZWIwMTk3YmZiMTYxYzA0ODJkOThiMTRmYTVkYjVjZWQyZmQ5NDllM2M2ZWRiMWUwYjRmZmRiYzNmZTAxNThjZjNjZmNiZmFmMDhlMTk4YmQ1Mg=='
    ,'Host':'haoma.baidu.com'
    ,'Origin':'https://haoma.baidu.com'
    ,'Referer':'https://haoma.baidu.com/phoneSearch?search=4008180280'
    ,'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"'
    ,'Sec-Ch-Ua-Mobile':'?0'
    ,'Sec-Ch-Ua-Platform':'"Windows"'
    ,'Sec-Fetch-Dest':'empty'
    ,'Sec-Fetch-Mode':'cors'
    ,'Sec-Fetch-Site':'same-origin'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

res = requests.post(url=url,data=JSON,headers=headers,verify=False)

print(res.status_code)

print(res.text)