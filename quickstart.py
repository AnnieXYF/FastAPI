from fastapi import FastAPI #第一个fastapi 是一个包第二个Fastapi 是一个类
import uvicorn
app=FastAPI()

@ app.get("/") #执行根路径返回数据 （@app.get("/") 装饰器告诉 FastAPI，当收到对根 URL ("/") 的 GET 请求时，应该执行后面的函数 home。）
async def home(): # def 前加上async 表示异步
    return{"user_id":1001}

@ app.get("/shop")
async def shop():
    return{"shop":"goods information"}
# 执行语言：uvicorn B_fastapi_quickstart:app --reload
# 这是一个简单的web 应用，利用web框架+自己写的业务逻辑 （对应的是响应程序）

# 等同于执行语言code ：uvicorn B_fastapi_quickstart:app --reload
if __name__ == '__main__':
    uvicorn.run("quickstart:app",port=8080,reload=True)


# fastapi 可以提供接口文档进行测试 ：http://127.0.0.1:8080/docs