
def avg_data(year):
    temp_i=0
    average=[]
    for rows in pd.read_csv(f'./Data/AQI/aqi{year}.csv',chunksize=24):
        add_var=0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var+=i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i !='---' and i!='InVld':
                    temp=float(i)
                    add_var+=temp
        avg=add_var/24
        temp_i+=1

        average.append(avg)
    return average
