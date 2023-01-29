# OPTshare

Special thanks to [AKshare](https://github.com/akfamily/akshare) for the opportunity to learn from this project in terms of code and project development.

[OPTshare](https://github.com/yulu0131/optshare) is a Python-based option data interface library, designed to provide easy-to-use option data, index data, and market yield data.

The main source of [OPTshare](https://github.com/yulu0131/optshare) data is the official website and raw data published by [eastmoney](https://www.eastmoney.com/) financial website.

- Documentation: [文档链接](https://optshare.readthedocs.io/en/latest/) 

## Installation

```
pip install optshare --upgrade
```

## Usage
### Code

```python
import optshare

current_option_data = optshare.get_current_option()
print(current_option_data)
```
### Output

```
                代码               名称   最新价    涨跌额      涨跌幅     成交量       成交额  \
0       a2305p4500    豆一23年05月沽4500  50.0   49.5  9900.00     1.0     500.0   
1        i2305p510    铁矿石23年05月沽510   3.0    2.9  2900.00     1.0     300.0   
2       v2305c9000   PVC23年05月购9000  12.5   12.0  2400.00     4.0     247.0   
3       v2305c9200   PVC23年05月购9200  12.0   11.5  2300.00    23.0    1280.0   
4      p2305c12600  棕榈油23年05月购12600   9.5    9.0  1800.00  2407.0  197575.0   
...            ...              ...   ...    ...      ...     ...       ...   
11963   y2303p8100    豆油23年03月沽8100   0.5   -2.0   -80.00   133.0    1135.0   
11964   y2303p8400    豆油23年03月沽8400   3.0  -13.5   -81.82   942.0   46570.0   
11965   SR303P5400    白糖23年03月沽5400   0.5   -2.5   -83.33   656.0    6560.0   
11966   y2303p8300    豆油23年03月沽8300   1.5   -8.0   -84.21   874.0   19995.0   
11967   v2309c7000   PVC23年09月购7000  40.0 -312.5   -88.65     1.0     200.0   

           持仓量  行权价  剩余日      日增     昨结    今开  
0        183.0  NaN  NaN     0.0    0.5  50.0  
1        745.0  NaN  NaN     0.0    0.1   3.0  
2        211.0  NaN  NaN     0.0    0.5  12.0  
3        133.0  NaN  NaN    -7.0    0.5  10.5  
4      12173.0  NaN  NaN  1360.0    0.5   7.0  
...        ...  ...  ...     ...    ...   ...  
11963    742.0  NaN  NaN   -80.0    2.5   1.0  
11964    630.0  NaN  NaN   148.0   16.5   6.5  
11965   5193.0  NaN  NaN   -82.0    3.0   0.5  
11966   7134.0  NaN  NaN   -32.0    9.5   3.5  
11967      9.0  NaN  NaN     0.0  352.5  40.0  

[11968 rows x 13 columns]
```