__author__ = 'onthego'

import pandas as pd

def exact_match(phrase,word):
    import re
    b = r'(\s|^|$)'
    res = re.match(b+word+b,phrase, flags = re.IGNORECASE)
    return bool(res) # returns true or false


def sale_frequency():

    work_book = all_sheets()



    date_record = CellRange(work_book[0],(1,1),(1660,1)).value

    sales_record = CellRange(work_book[0],(1,3),(1660,3)).value
    product_sales_price = CellRange(work_book[4],(1,1),(78,2)).value

    sales_list = []
    daily_sales_list = []
    total_daily_sales = 0
    total_daily_net_profit = 0
    product_revenue_and_net_profit_list = []
    product_revenue_and_net_profit_df = pd.DataFrame([("",0,0,0)],columns=["Product","Total Sales","Gross Sales","Net Profit"])
    daily_sales_counter = 0

    for n in range(1,len(date_record)):
        '''
        if n ==54:
            break
            '''
        if n == 1:


            product_revenue_and_net_profit_list.append([sales_record[n],0,0,0])

            counter = 1

            daily_sales_items = 1
        elif (date_record[n]) == (date_record[n-1]):
            '''
            print (str(n) +" " + str(date_record[n])+ " " + str(date_record[n-1]))
            '''
            '''
            print(n)
            print(sales_record[n])
            print(sales_record[n-1])
            print("")
            '''
            if exact_match(str(sales_record[n]),str(sales_record[n-1])) == True:

                counter+=1


            else:
                for m in range(0,len(product_sales_price)):
                    if exact_match(str(sales_record[n-1]),str(product_sales_price[m]))==True:

                        total_product_daily_sales = counter * product_sales_price[m+1]
                        '''
                        print(total_product_daily_sales)
                        '''

                        total_product_daily_net_profit = total_product_daily_sales *.1

                        
                        print(counter)
                        print(product_sales_price[m+1])
                        print(total_product_daily_sales)
                        print(total_product_daily_net_profit)
                        print(m)
                        print(product_sales_price[m])

                    ix_ = product_revenue_and_net_profit_df.ix[:, 0]
                    if (ix_ ==  product_sales_price[m]).any() == True :

                        product_revenue_and_net_profit_df.ix[:,:][(ix_ ==  product_sales_price[m])] = [
                            ix_[(ix_ ==  product_sales_price[m])],
                            product_revenue_and_net_profit_df.ix[:,1][(ix_ ==  product_sales_price[m])]+counter,
                            product_revenue_and_net_profit_df.ix[:,2][(ix_ ==  product_sales_price[
                                m])]+total_product_daily_sales,product_revenue_and_net_profit_df.ix[:,
                                                               3][(ix_ ==  product_sales_price[
                                m])]+total_product_daily_net_profit]
                    else:

                        product_revenue_and_net_profit_df.ix[(product_revenue_and_net_profit_df.shape[0]+1),:] = (
                            [product_sales_price[m],counter,total_product_daily_sales,
                             total_product_daily_net_profit]
                            )
                        
                        '''
                        print("")
                        print(sales_record[n-1])
                        print(m)
                        print(product_sales_price[m])
                        print(product_sales_price[m+1])

                        print("")
                        '''



                        for p in range(0,len(product_revenue_and_net_profit_list)):
                            if exact_match(str(product_sales_price[m]),str(product_revenue_and_net_profit_list[p][0])) \
                                    == \
                                    True:
                                product_revenue_and_net_profit_list[p][1] = product_revenue_and_net_profit_list[p][
                                                                                1]+ counter
                                product_revenue_and_net_profit_list[p][2] = product_revenue_and_net_profit_list[p][
                                                                                2]+ total_product_daily_sales
                                product_revenue_and_net_profit_list[p][3] = product_revenue_and_net_profit_list[p][
                                                                                3]+ total_product_daily_net_profit
                            else:
                                product_revenue_and_net_profit_list.append([product_sales_price[m ],counter,
                                                                            total_product_daily_sales,total_product_daily_net_profit])
                                break


                        total_daily_sales = total_daily_sales + total_product_daily_sales
                        total_daily_net_profit = total_daily_net_profit + total_product_daily_net_profit






                        break

                sales_list.append([date_record[n-1],sales_record[n-1],counter, int(total_product_daily_sales),
                                   int(total_product_daily_net_profit)])
                daily_sales_counter = counter + daily_sales_counter
                daily_sales_items +=1
                counter = 1
        else:
            daily_sales_list.append([date_record[n-1],daily_sales_counter,daily_sales_items,int(total_daily_sales),
                                     int(total_daily_net_profit)])
            counter = 1
            daily_sales_counter = 1
            daily_sales_items = 1
            total_daily_sales = 0
            total_daily_net_profit = 0
    Cell(work_book[1],(5,1)).table = sales_list
    Cell(work_book[2],(5,1)).table = daily_sales_list
    Cell(work_book[3],(5,1)).table = product_revenue_and_net_profit_list

if __name__ == "__main__":
    # this bit of code is to help time the different versions above.
#Don't worry
    # about understanding what it does for now, it's fairly python specific
    import timeit

    for fn in ["sale_frequency"]:
        print ("%s time (in seconds): " %fn)
        print (timeit.timeit(fn + "()", "from __main__ import "+fn, number=1))

    raise NotImplementedError # keep the python shell from dissapearing



