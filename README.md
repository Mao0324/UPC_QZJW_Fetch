# UPC_QZJW_Fetch
用于中国石油大学（华东），UPC，查询其它同学成绩，理论上任意使用强智教务系统的都通用  
步骤：  
1.获取cookies  
使用任意浏览器，登录数字石大，进入教务系统  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/fca70f67-7ffb-47a5-913a-9a358dbaf5b3)  
在如图所示页面(或者教务系统任意页面)，按下F12，刷新页面  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/f19fd583-3c74-4b6e-83e1-459a33aa68bc)  
点击如图所示文件  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/99db6f26-9c37-4bd8-ae4b-b515c839c92c)  
复制如图所示cookies，备用  
2.获取课程唯一标识符  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/7b5e2a1d-d429-4273-9cf7-75d7828ab6aa)  
打开如图所示成绩查询页面，点击你要查询的课程的成绩，会弹出一个新页面  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/5699be85-36f3-43e1-92be-390813abac69)  
复制如图所示jx0404id=xxxx备用  
3.修改代码  
打开代码  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/50cb9c43-214d-491e-a40b-121869c4472a)  
修改此处xxxx为你要查询课程的唯一标识符，也就是第二步找到的  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/c2d9eaa5-e6ca-497d-a0a1-0d1d795c2276)  
修改此处为第一步获取到的cookies  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/a63cad3f-621c-4ccb-9291-39fe9f5f1fa4)  
修改此处为要查询的同学学号范围，以及文件名称  
运行程序  
在文件夹中会生成本课程学号范围同学成绩  
![image](https://github.com/Mao0324/UPC_QZJW_Fetch/assets/133934785/19cb193d-0e31-4c28-9986-3daa5242449b)  
声明：仅用于学习，不得用于其它用途，请遵守相关法律法规







