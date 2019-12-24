
cust_cols = 'c,d'
tag_cols = ''
label_cols = ''
year = 2019
start_month = 3
start_day = 15
end_month = 9
end_day = 15
label_start_month = 9
label_start_day = 16
label_end_month = 10
label_end_day = 15
q = 'select t1.mid_seq as mid_seq, '  + label_cols + cust_cols + '\
              case when t2.mid_seq is not null then 1 else 0 end as churn_label \
                from ( \
                    select  ' + tag_cols + ' mid_seq from cdp_order_tag \
                    where ((order_year=' + str(year)+ ' and order_month = ' + str(start_month) + ' and order_day >=' + str(start_day) + ' ) or \
                    (order_year=' + str(year)+ ' and order_month > ' + str(start_month) +'and order_month <'+str(end_month) +' ) or \
                    (order_year=' + str(year)+ ' and order_month = ' + str(end_month) + ' and order_day <=' + str(end_day) + ' )) \
                             and order_status="1" group by mid_seq) t1\
                left join (\
                    select '  + tag_cols +  '  mid_seq from cdp_order_tag \
                    where ((order_year=' + str(year)+ ' and order_month = ' + str(label_start_month) + ' and order_day >=' + str(label_start_day) + ' ) or \
                    (order_year=' + str(year)+ ' and order_month > ' + str(label_start_month) +'and order_month <'+str(label_end_month) +' ) or \
                    (order_year=' + str(year)+ ' and order_month = ' + str(label_end_month) + ' and order_day <=' + str(label_end_day) + ' )) \
                              and order_status="1" group by mid_seq) t2 \
                on  t1.mid_seq=t2.mid_seq'

print(q)