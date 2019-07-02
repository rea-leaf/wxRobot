class Order:
    def __init__(self, is_start):
        self.is_start = is_start
        self.data = {}
        self.split_key = '######'

    # 获取订餐数据
    def get_order_data(self, data):

        order_data = ''
        split_key = self.split_key
        if data:
            sum = 0
            summsg = ''
            namemsg = ''
            for key in data:
                values = data[key].split(split_key)
                u_name = values[0]
                num = int(values[1])
                if num > 0:
                    sum = sum + num
                    summsg = '\n\n' + '----------汇总---------- ' + '\n总共 ' + str(sum) + '份 \n'
                    if namemsg == '':
                        namemsg = u_name
                    else:
                        namemsg = namemsg + ',' + u_name
                    order_data = order_data + '\n' + u_name + '     订' + str(num) + '份'
        if order_data == '':
            order_data = '\n今天无人订餐呦!'
        else:
            order_data = order_data + summsg + namemsg
        return order_data

    # 订餐
    def ordering(self, name, user_name, order_msg):
        if self.is_start:
            split_key = self.split_key
            data = self.data
            value = 0
            if user_name in data:
                value = int(data[user_name].split(split_key)[1])
            if ('1' == order_msg):
                data[user_name] = name + split_key + str(value + 1)
            elif ('-1' == order_msg):
                data[user_name] = name + split_key + str(value - 1)
            else:
                return
            order_data = self.get_order_data(data)
            ret = '@' + name + ' 已经收到 \n  -------当前订餐信息----\n ' + order_data + ' \n\n\n ps: 订餐规则(可以累计):\n 1 订餐 \n -1 取消订餐'
            return ret

    # 结束订餐
    def order_end(self):
        data = self.data
        self.is_start = False
        return self.get_order_data(data)


order1 = Order(True)
msg = order1.ordering('陈华富', 't44', '1')
print(msg)
msg = order1.ordering('周宁宁', 't55', '1')
print(msg)
order1.order_end()
msg = order1.ordering('陈华富', 't44', '-1')
print(msg)
