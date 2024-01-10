import json
import os

path = os.getcwd()

def find_data(chart,param):
    with open(f'{path}/single_pages/datas/hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    for i in range(int(len(json_data['list']))):
        if json_data['list'][i]['sj_div'] == chart and json_data['list'][i]['account_nm'] == param:
            return [json_data['list'][i]['bfefrmtrm_amount'], json_data['list'][i]['frmtrm_amount'], json_data['list'][i]['thstrm_amount']]

def find_label():
    
    with open(f'{path}/single_pages/datas/hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        return [json_data['list'][0]['bfefrmtrm_nm'],json_data['list'][0]['frmtrm_nm'],json_data['list'][0]['thstrm_nm']]

def find_BS():
    BS_dict = {}
    with open(f'{path}/single_pages/datas\hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            for i in range(int(len(json_data['list']))):
                if json_data['list'][i]['sj_div'] == 'BS':
                    BS_dict[json_data['list'][i]['account_nm']] = [
                        json_data['list'][i]['thstrm_amount'],
                        json_data['list'][i]['frmtrm_amount'],
                        json_data['list'][i]['bfefrmtrm_amount']
                        ]
    return BS_dict

class find_Iv:
    
    def Debt_Ratios():
        data_dict = {}
        data1_list = []
        data2_list = []
        data3_list = []
        result_dict = {}
        with open(f'{path}/single_pages/datas/hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            for i in range(int(len(json_data['list']))):
                if json_data['list'][i]['account_nm'] == '부채총계':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
                elif json_data['list'][i]['account_nm'] == '자산총계':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
            for f_amount, s_amount in zip(data_dict['부채총계'],data_dict['자산총계']):
                data1_list.append(f_amount/(s_amount+f_amount))
                data2_list.append(s_amount/(s_amount+f_amount))
                data3_list.append((f_amount/s_amount))
            result_dict['부채'] = data1_list
            result_dict['자산'] = data2_list
            result_dict['부채비율'] = data3_list
        return result_dict

    def Net_Profit_Margin():
        data_dict = {}
        data1_list = []
        data2_list = []
        data3_list = []
        result_dict = {}
        with open(f'{path}/single_pages/datas/hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            for i in range(int(len(json_data['list']))):
                if json_data['list'][i]['account_nm'] == '당기순이익':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
                elif json_data['list'][i]['account_nm'] == '매출액':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
            for f_amount, s_amount in zip(data_dict['당기순이익'],data_dict['매출액']):
                data1_list.append(f_amount/(s_amount+f_amount))
                data2_list.append(s_amount/(s_amount+f_amount))
                data3_list.append((f_amount/s_amount))
            result_dict['당기순이익'] = data1_list
            result_dict['매출액'] = data2_list
            result_dict['순이익률'] = data3_list
        return result_dict
    
    def Current_Ratio():
        data_dict = {}
        data1_list = []
        data2_list = []
        data3_list = []
        result_dict = {}
        with open(f'{path}/single_pages/datas/hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            for i in range(int(len(json_data['list']))):
                if json_data['list'][i]['account_nm'] == '유동자산':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
                elif json_data['list'][i]['account_nm'] == '유동부채':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
            for f_amount, s_amount in zip(data_dict['유동자산'],data_dict['유동부채']):
                data1_list.append(f_amount/(s_amount+f_amount))
                data2_list.append(s_amount/(s_amount+f_amount))
                data3_list.append((f_amount/s_amount))
            result_dict['유동자산'] = data1_list
            result_dict['유동부채'] = data2_list
            result_dict['유동비율'] = data3_list
        return result_dict
    
    def Quick_Ratio():
        data_dict = {}
        data1_list = []
        data2_list = []
        data3_list = []
        result_dict = {}
        with open(f'{path}/single_pages/datas/hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            for i in range(int(len(json_data['list']))):
                if json_data['list'][i]['account_nm'] == '유동자산':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
                elif json_data['list'][i]['account_nm'] == '재고자산':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
                elif json_data['list'][i]['account_nm'] == '유동부채':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
            for f_amount, s_amount, t_amount in zip(data_dict['유동자산'],data_dict['재고자산'],data_dict['유동부채']):
                data1_list.append((f_amount - s_amount)/((f_amount - s_amount)+t_amount))
                data2_list.append(t_amount/((f_amount - s_amount)+t_amount))
                data3_list.append((f_amount - s_amount)/t_amount)
            result_dict['유동자산-재고자산'] = data1_list
            result_dict['유동부채'] = data2_list
            result_dict['당좌비율'] = data3_list
        return result_dict
    def ROE():
        data_dict = {}
        data1_list = []
        data2_list = []
        data3_list = []
        result_dict = {}
        with open(f'{path}/single_pages/datas/hybe_data/hybe2023.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            for i in range(int(len(json_data['list']))):
                if json_data['list'][i]['account_nm'] == '당기순이익':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
                elif json_data['list'][i]['account_nm'] == '자본총계':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
                elif json_data['list'][i]['account_nm'] == '부채총계':
                    data_dict[json_data['list'][i]['account_nm']] = [
                        int(json_data['list'][i]['thstrm_amount']),
                        int(json_data['list'][i]['frmtrm_amount']),
                        int(json_data['list'][i]['bfefrmtrm_amount'])
                        ]
            for f_amount, s_amount, t_amount in zip(data_dict['당기순이익'],data_dict['자본총계'],data_dict['부채총계']):
                data1_list.append(f_amount / (f_amount + (s_amount-t_amount)))
                data2_list.append((s_amount-t_amount) / (f_amount + (s_amount-t_amount)))
                data3_list.append(f_amount / (s_amount-t_amount))
            result_dict['당기순이익'] = data1_list
            result_dict['자기자본'] = data2_list
            result_dict['자기자본이익률'] = data3_list
        return result_dict