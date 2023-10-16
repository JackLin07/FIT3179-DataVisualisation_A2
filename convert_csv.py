# import pandas as pd
import json

# Your CSV string
data = """
2000/1/1,5
2000/2/1,5.48
2000/3/1,5.5
2000/4/1,5.72
2000/5/1,5.98
2000/6/1,6
2000/7/1,6
2000/8/1,6.24
2000/9/1,6.25
2000/10/1,6.25
2000/11/1,6.25
2000/12/1,6.25
2001/1/1,6.25
2001/2/1,5.85
2001/3/1,5.55
2001/4/1,5.06
2001/5/1,5
2001/6/1,5
2001/7/1,5
2001/8/1,5
2001/9/1,4.78
2001/10/1,4.52
2001/11/1,4.5
2001/12/1,4.28
2002/1/1,4.25
2002/2/1,4.25
2002/3/1,4.25
2002/4/1,4.25
2002/5/1,4.45
2002/6/1,4.72
2002/7/1,4.75
2002/8/1,4.75
2002/9/1,4.75
2002/10/1,4.75
2002/11/1,4.75
2002/12/1,4.75
2003/1/1,4.75
2003/2/1,4.75
2003/3/1,4.75
2003/4/1,4.75
2003/5/1,4.75
2003/6/1,4.75
2003/7/1,4.75
2003/8/1,4.75
2003/9/1,4.75
2003/10/1,4.75
2003/11/1,4.98
2003/12/1,5.23
2004/1/1,5.25
2004/2/1,5.25
2004/3/1,5.25
2004/4/1,5.25
2004/5/1,5.25
2004/6/1,5.25
2004/7/1,5.25
2004/8/1,5.25
2004/9/1,5.25
2004/10/1,5.25
2004/11/1,5.25
2004/12/1,5.25
2005/1/1,5.25
2005/2/1,5.25
2005/3/1,5.49
2005/4/1,5.5
2005/5/1,5.5
2005/6/1,5.5
2005/7/1,5.5
2005/8/1,5.5
2005/9/1,5.5
2005/10/1,5.5
2005/11/1,5.5
2005/12/1,5.5
2006/1/1,5.5
2006/2/1,5.5
2006/3/1,5.5
2006/4/1,5.5
2006/5/1,5.73
2006/6/1,5.75
2006/7/1,5.75
2006/8/1,5.99
2006/9/1,6
2006/10/1,6
2006/11/1,6.19
2006/12/1,6.25
2007/1/1,6.25
2007/2/1,6.25
2007/3/1,6.25
2007/4/1,6.25
2007/5/1,6.25
2007/6/1,6.25
2007/7/1,6.25
2007/8/1,6.45
2007/9/1,6.5
2007/10/1,6.5
2007/11/1,6.7
2007/12/1,6.75
2008/1/1,6.75
2008/2/1,6.96
2008/3/1,7.22
2008/4/1,7.25
2008/5/1,7.25
2008/6/1,7.25
2008/7/1,7.25
2008/8/1,7.25
2008/9/1,7.02
2008/10/1,6.18
2008/11/1,5.33
2008/12/1,4.35
2009/1/1,4.25
2009/2/1,3.35
2009/3/1,3.25
2009/4/1,3.06
2009/5/1,3
2009/6/1,3
2009/7/1,3
2009/8/1,3
2009/9/1,3
2009/10/1,3.21
2009/11/1,3.48
2009/12/1,3.74
2010/1/1,3.75
2010/2/1,3.75
2010/3/1,3.98
2010/4/1,4.22
2010/5/1,4.48
2010/6/1,4.5
2010/7/1,4.5
2010/8/1,4.5
2010/9/1,4.5
2010/10/1,4.5
2010/11/1,4.73
2010/12/1,4.75
2011/1/1,4.75
2011/2/1,4.75
2011/3/1,4.75
2011/4/1,4.75
2011/5/1,4.75
2011/6/1,4.75
2011/7/1,4.75
2011/8/1,4.75
2011/9/1,4.75
2011/10/1,4.75
2011/11/1,4.51
2011/12/1,4.3
2012/1/1,4.25
2012/2/1,4.25
2012/3/1,4.25
2012/4/1,4.25
2012/5/1,3.77
2012/6/1,3.54
2012/7/1,3.5
2012/8/1,3.5
2012/9/1,3.5
2012/10/1,3.27
2012/11/1,3.25
2012/12/1,3.03
2013/1/1,3
2013/2/1,3
2013/3/1,3
2013/4/1,3
2013/5/1,2.8
2013/6/1,2.75
2013/7/1,2.75
2013/8/1,2.55
2013/9/1,2.5
2013/10/1,2.5
2013/11/1,2.5
2013/12/1,2.5
2014/1/1,2.5
2014/2/1,2.5
2014/3/1,2.5
2014/4/1,2.5
2014/5/1,2.5
2014/6/1,2.5
2014/7/1,2.5
2014/8/1,2.5
2014/9/1,2.5
2014/10/1,2.5
2014/11/1,2.5
2014/12/1,2.5
2015/1/1,2.5
2015/2/1,2.28
2015/3/1,2.25
2015/4/1,2.25
2015/5/1,2.04
2015/6/1,2
2015/7/1,2
2015/8/1,2
2015/9/1,2
2015/10/1,2
2015/11/1,2
2015/12/1,2
2016/1/1,2
2016/2/1,2
2016/3/1,2
2016/4/1,2
2016/5/1,1.77
2016/6/1,1.75
2016/7/1,1.75
2016/8/1,1.52
2016/9/1,1.5
2016/10/1,1.5
2016/11/1,1.5
2016/12/1,1.5
2017/1/1,1.5
2017/2/1,1.5
2017/3/1,1.5
2017/4/1,1.5
2017/5/1,1.5
2017/6/1,1.5
2017/7/1,1.5
2017/8/1,1.5
2017/9/1,1.5
2017/10/1,1.5
2017/11/1,1.5
2017/12/1,1.5
2018/1/1,1.5
2018/2/1,1.5
2018/3/1,1.5
2018/4/1,1.5
2018/5/1,1.5
2018/6/1,1.5
2018/7/1,1.5
2018/8/1,1.5
2018/9/1,1.5
2018/10/1,1.5
2018/11/1,1.5
2018/12/1,1.5
2019/1/1,1.5
2019/2/1,1.5
2019/3/1,1.5
2019/4/1,1.5
2019/5/1,1.5
2019/6/1,1.28
2019/7/1,1.02
2019/8/1,1
2019/9/1,1
2019/10/1,0.76
2019/11/1,0.75
2019/12/1,0.75
2020/1/1,0.75
2020/2/1,0.75
2020/3/1,0.43
2020/4/1,0.25
2020/5/1,0.25
2020/6/1,0.25
2020/7/1,0.25
2020/8/1,0.25
2020/9/1,0.25
2020/10/1,0.25
2020/11/1,0.11
2020/12/1,0.1
2021/1/1,0.1
2021/2/1,0.1
2021/3/1,0.1
2021/4/1,0.1
2021/5/1,0.1
2021/6/1,0.1
2021/7/1,0.1
2021/8/1,0.1
2021/9/1,0.1
2021/10/1,0.1
2021/11/1,0.1
2021/12/1,0.1
2022/1/1,0.1
2022/2/1,0.1
2022/3/1,0.1
2022/4/1,0.1
2022/5/1,0.33
2022/6/1,0.73
2022/7/1,1.28
2022/8/1,1.81
2022/9/1,2.25
2022/10/1,2.58
2022/11/1,2.84
2022/12/1,3.05
2023/1/1,3.1
2023/2/1,3.29
2023/3/1,3.54
2023/4/1,3.6
2023/5/1,3.83
2023/6/1,4.05
2023/7/1,4.1
2023/8/1,4.1
"""

# Split the string into lines and then into date and interest rate
lines = data.split("\n")
records = [line.split(",") for line in lines if line]

# Convert the data into a dictionary with date and interest rate
data_list = [{"date": date, "Interest Rate": float(rate)} for date, rate in records]

# Iterate through each record in data_list and print it
for record in data_list:
    print(
        f'{{"date": "{record["date"]}", "Interest Rate": "{record["Interest Rate"]}"}},'
    )

# print(f'{"date": "%s", "Interest Rate": "%s"}', data_list.date, data_list.rate)
# Convert the dictionary to JSON
# json_data = json.dumps(data_list, indent=2)

# Print the JSON data
# print(json_data[:3000])